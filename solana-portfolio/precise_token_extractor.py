#!/usr/bin/env python3
"""
Precise token extractor for trading journal - gets actual current USD balances
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import re

def extract_current_balances(popup_content):
    """
    Extract actual current USD balances from Jupiter popup
    Based on the table structure: Token -> Balance column
    """
    current_holdings = []
    lines = popup_content.split('\n')

    # Find tokens that are NOT "Sold all" and have current balances
    i = 0
    while i < len(lines) - 10:
        line = lines[i].strip()

        # Look for token names
        if (line.isupper() and
            2 <= len(line) <= 10 and
            line.isalpha() and
            line not in ['USD', 'ALL', 'NEW', 'HOLDING', 'SOLD', 'PRICE', 'LAST', 'BALANCE']):

            token_name = line

            # Check if this token is sold (look for "Sold all" in next few lines)
            is_sold = False
            for check_j in range(1, 5):
                if i + check_j < len(lines) and 'sold all' in lines[i + check_j].lower():
                    is_sold = True
                    break

            if not is_sold:
                # Look for the Balance column value
                # In the table structure, balance appears after several fields
                for j in range(1, 15):
                    if i + j < len(lines):
                        balance_line = lines[i + j].strip()

                        # Look for USD balance format - typically $X.XXK or $XX.XX
                        # Must be a standalone balance, not part of PnL calculation
                        balance_match = re.match(r'^\$([0-9,.]+[KMB]?)$', balance_line)
                        if balance_match:
                            amount = balance_match.group(1)
                            try:
                                # Convert to float for validation
                                if 'K' in amount:
                                    num_val = float(amount.replace('K', '').replace(',', '')) * 1000
                                elif 'M' in amount:
                                    num_val = float(amount.replace('M', '').replace(',', '')) * 1000000
                                else:
                                    num_val = float(amount.replace(',', ''))

                                # Only include meaningful balances (> $1)
                                if num_val > 1:
                                    current_holdings.append(f"{token_name}: ${amount}")
                                    break
                            except:
                                continue

                        # Also look for regular dollar amounts
                        if balance_line.startswith('$') and len(balance_line) < 20:
                            regular_match = re.match(r'^\$([0-9,.]+)$', balance_line)
                            if regular_match:
                                amount = regular_match.group(1)
                                try:
                                    if float(amount.replace(',', '')) > 10:  # > $10
                                        current_holdings.append(f"{token_name}: ${amount}")
                                        break
                                except:
                                    continue
        i += 1

    return current_holdings

def test_trading_journal_extraction(wallet_address):
    """
    Test extraction for trading journal purposes
    """
    url = f"https://jup.ag/portfolio/{wallet_address}"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        time.sleep(8)

        # Click Holdings PnL for detailed view
        pnl_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Holdings PnL')]")
        if pnl_elements:
            for element in pnl_elements:
                if element.is_enabled() and element.is_displayed():
                    driver.execute_script("arguments[0].click();", element)
                    time.sleep(8)
                    break

        # Get detailed content
        popup_content = driver.find_element(By.TAG_NAME, "body").text

        # Extract trading journal data
        holdings = extract_current_balances(popup_content)

        # Also extract key metrics for trading journal
        metrics = {}
        lines = popup_content.split('\n')
        for i, line in enumerate(lines):
            if 'Holdings' in line and i+1 < len(lines) and '$' in lines[i+1]:
                metrics['total_holdings'] = lines[i+1].strip()
            elif 'Total PnL' in line and i+1 < len(lines):
                metrics['total_pnl'] = lines[i+1].strip()
            elif 'Win Rate' in line and i+1 < len(lines):
                metrics['win_rate'] = lines[i+1].strip()
            elif 'Realised PnL' in line and i+1 < len(lines):
                metrics['realised_pnl'] = lines[i+1].strip()

        driver.quit()

        return {
            'wallet': wallet_address,
            'current_holdings': holdings,
            'metrics': metrics,
            'status': 'success'
        }

    except Exception as e:
        print(f"Error: {e}")
        try:
            driver.quit()
        except:
            pass
        return None

if __name__ == "__main__":
    print("🎯 Testing Trading Journal Extraction...")

    # Test with the wallet that has known holdings
    wallet = "A1N45nJh8eRn2zhXxP7SkqNKvR6rPXhbVgKzBGBxKEm8"
    result = test_trading_journal_extraction(wallet)

    if result:
        print(f"\n📊 Trading Journal Data for: {result['wallet'][:8]}...")
        print(f"{'='*50}")

        print("\n💰 Current Holdings:")
        for holding in result['current_holdings']:
            print(f"  - {holding}")

        print("\n📈 Key Metrics:")
        for key, value in result['metrics'].items():
            print(f"  - {key}: {value}")

        print(f"\n✅ Status: {result['status']}")
    else:
        print("❌ Failed to extract trading journal data")