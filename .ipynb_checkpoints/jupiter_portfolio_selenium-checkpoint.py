#!/usr/bin/env python3
"""
Get Jupiter portfolio data using Selenium - the working version!
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def get_jupiter_portfolio_data(wallet_address):
    """
    Get portfolio data from Jupiter using Selenium (with all PnL and values)
    """
    url = f"https://jup.ag/portfolio/{wallet_address}"

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in background
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    try:
        print(f"📊 Fetching portfolio data for: {wallet_address}")
        print(f"🔗 URL: {url}")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)

        # Wait for portfolio data to load
        print("⏳ Waiting for portfolio data to load...")
        time.sleep(10)

        # Extract portfolio data
        page_text = driver.find_element(By.TAG_NAME, "body").text

        # Find portfolio elements
        portfolio_data = {}

        # Look for dollar amounts and portfolio values
        elements = driver.find_elements(By.XPATH, "//*[contains(text(), '$') or contains(text(), 'SOL') or contains(text(), 'PnL')]")

        portfolio_values = []
        for element in elements:
            text = element.text.strip()
            if text and '$' in text:
                portfolio_values.append(text)

        # Extract specific metrics from visible text
        lines = page_text.split('\n')
        for i, line in enumerate(lines):
            if 'Net Worth' in line and i+1 < len(lines):
                portfolio_data['net_worth'] = lines[i+1]
            elif 'Holdings PnL' in line and i+1 < len(lines):
                portfolio_data['holdings_pnl'] = lines[i+1]
            elif 'JUP Holdings' in line and i+1 < len(lines):
                portfolio_data['jup_holdings'] = lines[i+1]

        portfolio_data['all_dollar_values'] = portfolio_values
        portfolio_data['wallet'] = wallet_address
        portfolio_data['timestamp'] = time.strftime('%Y-%m-%d %H:%M:%S')

        # Show first 500 characters of what we can see
        print(f"\n📝 First 500 characters of page text:")
        print(page_text[:500])

        driver.quit()

        print("\n✅ Portfolio data extracted successfully!")
        return portfolio_data

    except Exception as e:
        print(f"❌ Error: {e}")
        try:
            driver.quit()
        except:
            pass
        return None

if __name__ == "__main__":
    # Test the function
    wallet_address = "61rVn8zeoikzFuT2cuXAd3Qv9RxhMDvG52xL4LHLv7Nu"
    portfolio_data = get_jupiter_portfolio_data(wallet_address)

    if portfolio_data:
        print("\n" + "="*50)
        print("📊 PORTFOLIO SUMMARY")
        print("="*50)
        for key, value in portfolio_data.items():
            print(f"{key}: {value}")
    else:
        print("Failed to get portfolio data")