#!/usr/bin/env python3
"""
Enhanced multi-wallet tracker that clicks PnL popup for detailed data
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import pandas as pd
from datetime import datetime

def get_detailed_wallet_data(wallet_address, driver):
    """
    Get detailed portfolio data by clicking on Holdings PnL popup
    """
    url = f"https://jup.ag/portfolio/{wallet_address}"

    try:
        print(f"📊 Loading wallet: {wallet_address[:8]}...")

        driver.get(url)
        time.sleep(8)  # Wait for main page to load

        # Get basic page text first
        basic_text = driver.find_element(By.TAG_NAME, "body").text

        portfolio_data = {
            'wallet': wallet_address,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'net_worth': 'N/A',
            'holdings_pnl': 'N/A',
            'jup_holdings': 'N/A',
            'detailed_pnl_data': 'N/A',
            'status': 'success'
        }

        # Extract basic data
        lines = basic_text.split('\n')
        for i, line in enumerate(lines):
            if 'Net Worth' in line and i+1 < len(lines):
                portfolio_data['net_worth'] = lines[i+1].strip()
            elif 'Holdings PnL' in line and i+1 < len(lines):
                portfolio_data['holdings_pnl'] = lines[i+1].strip()
            elif 'JUP Holdings' in line and i+1 < len(lines):
                portfolio_data['jup_holdings'] = lines[i+1].strip()

        # Now try to click on Holdings PnL for detailed data
        print(f"🔍 Looking for Holdings PnL clickable element...")

        try:
            # Try different ways to find the Holdings PnL clickable element
            pnl_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Holdings PnL')]")

            if pnl_elements:
                print(f"   Found {len(pnl_elements)} PnL elements, trying to click...")

                # Try clicking the first clickable one
                for element in pnl_elements:
                    try:
                        # Check if element is clickable
                        if element.is_enabled() and element.is_displayed():
                            print(f"   Clicking on PnL element...")
                            driver.execute_script("arguments[0].click();", element)
                            time.sleep(5)  # Wait for popup

                            # Get the updated page content (should include popup)
                            popup_content = driver.find_element(By.TAG_NAME, "body").text

                            # Extract detailed PnL info
                            if len(popup_content) > len(basic_text):
                                print(f"   ✅ Got detailed popup data! ({len(popup_content)} vs {len(basic_text)} chars)")
                                portfolio_data['detailed_pnl_data'] = popup_content

                                # Show first 500 chars of new content
                                new_content = popup_content[len(basic_text):]
                                print(f"   📝 New popup content preview: {new_content[:200]}...")
                            else:
                                print(f"   ⚠️ No additional content detected")

                            break
                    except Exception as click_error:
                        print(f"   ❌ Click failed: {click_error}")
                        continue
            else:
                print(f"   ⚠️ No Holdings PnL elements found")

        except Exception as popup_error:
            print(f"   ❌ Popup extraction failed: {popup_error}")

        return portfolio_data

    except Exception as e:
        print(f"❌ Error with wallet {wallet_address[:8]}: {e}")
        return {
            'wallet': wallet_address,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'net_worth': 'ERROR',
            'holdings_pnl': 'ERROR',
            'jup_holdings': 'ERROR',
            'detailed_pnl_data': 'ERROR',
            'status': f'error: {str(e)}'
        }

def track_wallets_with_popup_data(wallet_addresses):
    """
    Track multiple wallets with detailed popup data
    """
    print(f"🚀 Starting enhanced tracking for {len(wallet_addresses)} wallets...")

    # Set up Chrome driver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    results = []

    try:
        driver = webdriver.Chrome(options=chrome_options)

        for i, wallet in enumerate(wallet_addresses, 1):
            print(f"\n[{i}/{len(wallet_addresses)}] Processing wallet...")
            wallet_data = get_detailed_wallet_data(wallet, driver)
            results.append(wallet_data)

            # Small delay between requests
            time.sleep(3)

        driver.quit()

    except Exception as e:
        print(f"❌ Driver error: {e}")
        try:
            driver.quit()
        except:
            pass

    # Convert to DataFrame
    df = pd.DataFrame(results)
    return df

def display_enhanced_summary(df):
    """
    Display enhanced summary including popup data
    """
    print("\n" + "="*80)
    print("📊 ENHANCED MULTI-WALLET PORTFOLIO SUMMARY")
    print("="*80)

    for index, row in df.iterrows():
        print(f"\n🔹 Wallet: {row['wallet'][:8]}...{row['wallet'][-8:]}")
        print(f"   Net Worth: {row['net_worth']}")
        print(f"   Holdings PnL: {row['holdings_pnl']}")
        print(f"   JUP Holdings: {row['jup_holdings']}")
        print(f"   Status: {row['status']}")
        print(f"   Checked: {row['timestamp']}")

        # Show if we got detailed data
        if row['detailed_pnl_data'] != 'N/A' and row['detailed_pnl_data'] != 'ERROR':
            print(f"   ✅ Got detailed PnL data ({len(str(row['detailed_pnl_data']))} chars)")
        else:
            print(f"   ⚠️ No detailed PnL data")

    print("\n" + "="*80)

if __name__ == "__main__":
    # Test with the wallet that has PnL data
    wallets_to_track = [
        "61rVn8zeoikzFuT2cuXAd3Qv9RxhMDvG52xL4LHLv7Nu",  # The one with $2.2M PnL
    ]

    # Track all wallets with popup data
    results_df = track_wallets_with_popup_data(wallets_to_track)

    # Display results
    display_enhanced_summary(results_df)

    # Save to CSV
    csv_filename = f"enhanced_portfolio_tracking_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    results_df.to_csv(csv_filename, index=False)
    print(f"\n💾 Results saved to: {csv_filename}")

    # Show sample of detailed data if available
    for index, row in results_df.iterrows():
        if row['detailed_pnl_data'] != 'N/A' and row['detailed_pnl_data'] != 'ERROR':
            print(f"\n📋 Sample detailed data for {row['wallet'][:8]}:")
            print("-" * 50)
            print(str(row['detailed_pnl_data'])[:1000] + "...")
            break