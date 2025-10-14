#!/usr/bin/env python3
"""
Track multiple Solana wallets using Jupiter portfolio data
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd
from datetime import datetime

def get_single_wallet_data(wallet_address, driver):
    """
    Get portfolio data for a single wallet using existing driver
    """
    url = f"https://jup.ag/portfolio/{wallet_address}"

    try:
        print(f"📊 Checking wallet: {wallet_address[:8]}...")

        driver.get(url)
        time.sleep(8)  # Wait for data to load

        # Get page text
        page_text = driver.find_element(By.TAG_NAME, "body").text

        # Extract portfolio data
        portfolio_data = {
            'wallet': wallet_address,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'net_worth': 'N/A',
            'holdings_pnl': 'N/A',
            'jup_holdings': 'N/A',
            'status': 'success'
        }

        # Parse the text to find values
        lines = page_text.split('\n')
        for i, line in enumerate(lines):
            if 'Net Worth' in line and i+1 < len(lines):
                portfolio_data['net_worth'] = lines[i+1].strip()
            elif 'Holdings PnL' in line and i+1 < len(lines):
                portfolio_data['holdings_pnl'] = lines[i+1].strip()
            elif 'JUP Holdings' in line and i+1 < len(lines):
                portfolio_data['jup_holdings'] = lines[i+1].strip()

        return portfolio_data

    except Exception as e:
        print(f"❌ Error with wallet {wallet_address[:8]}: {e}")
        return {
            'wallet': wallet_address,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'net_worth': 'ERROR',
            'holdings_pnl': 'ERROR',
            'jup_holdings': 'ERROR',
            'status': f'error: {str(e)}'
        }

def track_multiple_wallets(wallet_addresses):
    """
    Track multiple wallets and return results as DataFrame
    """
    print(f"🚀 Starting tracking for {len(wallet_addresses)} wallets...")

    # Set up Chrome driver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    results = []

    try:
        driver = webdriver.Chrome(options=chrome_options)

        for i, wallet in enumerate(wallet_addresses, 1):
            print(f"\n[{i}/{len(wallet_addresses)}] Processing wallet...")
            wallet_data = get_single_wallet_data(wallet, driver)
            results.append(wallet_data)

            # Small delay between requests
            time.sleep(2)

        driver.quit()

    except Exception as e:
        print(f"❌ Driver error: {e}")
        try:
            driver.quit()
        except:
            pass

    # Convert to DataFrame for nice display
    df = pd.DataFrame(results)
    return df

def display_portfolio_summary(df):
    """
    Display a nice summary of all portfolios
    """
    print("\n" + "="*80)
    print("📊 MULTI-WALLET PORTFOLIO SUMMARY")
    print("="*80)

    for index, row in df.iterrows():
        print(f"\n🔹 Wallet: {row['wallet'][:8]}...{row['wallet'][-8:]}")
        print(f"   Net Worth: {row['net_worth']}")
        print(f"   Holdings PnL: {row['holdings_pnl']}")
        print(f"   JUP Holdings: {row['jup_holdings']}")
        print(f"   Status: {row['status']}")
        print(f"   Checked: {row['timestamp']}")

    print("\n" + "="*80)

    # Calculate totals (if possible)
    successful_wallets = df[df['status'] == 'success']
    print(f"✅ Successfully checked: {len(successful_wallets)} wallets")
    print(f"❌ Errors: {len(df) - len(successful_wallets)} wallets")

if __name__ == "__main__":
    # Example wallet addresses to track
    wallets_to_track = [
        "61rVn8zeoikzFuT2cuXAd3Qv9RxhMDvG52xL4LHLv7Nu",  # The one we tested
        "9QEHSyTqyRNDSvbYtFjqR2e5UXNfvjpAcEdTqAjSwVmH",  # Another one
        # Add more wallet addresses here
    ]

    # Track all wallets
    results_df = track_multiple_wallets(wallets_to_track)

    # Display results
    display_portfolio_summary(results_df)

    # Save to CSV
    csv_filename = f"portfolio_tracking_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    results_df.to_csv(csv_filename, index=False)
    print(f"\n💾 Results saved to: {csv_filename}")