#!/usr/bin/env python3
"""
Extract ONLY current holdings - no historical data
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import re

def extract_only_current_holdings(popup_content):
    """
    Extract ONLY tokens with current meaningful balances
    Exclude sold positions and tiny amounts
    """
    current_holdings = []
    lines = popup_content.split('\n')

    # Strategy: Look for tokens that are NOT marked as "Sold all"
    # and have a Balance column value > $10
    i = 0
    while i < len(lines) - 15:
        line = lines[i].strip()

        # Find token names
        if (line.isupper() and
            2 <= len(line) <= 10 and
            line.isalpha() and
            line not in ['USD', 'ALL', 'NEW', 'HOLDING', 'SOLD', 'PRICE', 'LAST', 'BALANCE', 'TOTAL']):

            token_name = line

            # Check the next several lines for "Sold all" indicator
            is_sold = False
            current_balance = None

            # Look ahead for status and balance
            for j in range(1, 20):
                if i + j >= len(lines):
                    break

                check_line = lines[i + j].strip()

                # If we find "Sold all", this token has no current holdings
                if 'sold all' in check_line.lower():
                    is_sold = True
                    break

                # Look for the balance amount in the Balance column
                # This should be a standalone $X.XX amount
                if re.match(r'^\$[0-9,.]+[KMB]?$', check_line):
                    balance_amount = check_line

                    # Extract numeric value
                    amount_str = balance_amount.replace('$', '').replace(',', '')
                    try:
                        if 'K' in amount_str:
                            numeric_value = float(amount_str.replace('K', '')) * 1000
                        elif 'M' in amount_str:
                            numeric_value = float(amount_str.replace('M', '')) * 1000000
                        else:
                            numeric_value = float(amount_str)

                        # Only consider meaningful current balances
                        if numeric_value > 50:  # More than $50 to filter out dust
                            current_balance = balance_amount
                            break

                    except ValueError:
                        continue

            # Only add if not sold and has meaningful current balance
            if not is_sold and current_balance:
                current_holdings.append(f"{token_name}: {current_balance}")

        i += 1

    return current_holdings

def test_current_holdings_only(wallet_address):
    """
    Test extraction of current holdings only
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

        print("=== DEBUGGING: Looking for current holdings only ===")

        # Find the table section
        lines = popup_content.split('\n')
        for i, line in enumerate(lines):
            if line.strip() in ['GIGA', 'ALCH', 'POPCAT', 'ye']:
                print(f"\nFound token: {line.strip()}")
                # Show next 10 lines to understand structure
                for j in range(1, 11):
                    if i + j < len(lines):
                        print(f"  +{j}: {lines[i + j].strip()}")

        # Extract current holdings
        holdings = extract_only_current_holdings(popup_content)

        driver.quit()

        return holdings

    except Exception as e:
        print(f"Error: {e}")
        try:
            driver.quit()
        except:
            pass
        return []

if __name__ == "__main__":
    print("🎯 Testing CURRENT Holdings Only Extraction...")

    wallet = "A1N45nJh8eRn2zhXxP7SkqNKvR6rPXhbVgKzBGBxKEm8"
    holdings = test_current_holdings_only(wallet)

    print(f"\n💰 CURRENT Holdings Found:")
    if holdings:
        for holding in holdings:
            print(f"  - {holding}")
    else:
        print("  - No current holdings detected")

    print(f"\n📊 Should match screenshot: GIGA: $2.62K, ye: $87.59")