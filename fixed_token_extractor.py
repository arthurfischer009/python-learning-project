#!/usr/bin/env python3
"""
Fixed token extractor that properly gets the detailed popup data
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

def extract_detailed_portfolio_data(wallet_address):
    """
    Extract detailed portfolio data including token holdings
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

        # Get basic page content first
        basic_content = driver.find_element(By.TAG_NAME, "body").text
        print("=== BASIC PAGE CONTENT ===")
        print(basic_content[:500])

        # Now try to click on Holdings PnL to get detailed popup
        print("\n=== ATTEMPTING TO CLICK HOLDINGS PNL ===")

        try:
            # Try multiple selectors to find the clickable PnL element
            possible_selectors = [
                "//*[contains(text(), 'Holdings PnL')]",
                "//*[contains(text(), '$') and contains(text(), 'PnL')]",
                "//div[contains(@class, 'pnl') or contains(@class, 'holdings')]",
                "//*[text()='Holdings PnL']/..",
            ]

            clicked = False
            for selector in possible_selectors:
                try:
                    elements = driver.find_elements(By.XPATH, selector)
                    print(f"Found {len(elements)} elements with selector: {selector}")

                    for i, element in enumerate(elements):
                        try:
                            if element.is_displayed() and element.is_enabled():
                                print(f"Attempting to click element {i+1}")

                                # Try different click methods
                                try:
                                    element.click()
                                    clicked = True
                                    print("✅ Standard click successful!")
                                    break
                                except:
                                    try:
                                        driver.execute_script("arguments[0].click();", element)
                                        clicked = True
                                        print("✅ JavaScript click successful!")
                                        break
                                    except:
                                        print("❌ Click failed")
                                        continue
                        except Exception as e:
                            print(f"❌ Element {i+1} click error: {e}")
                            continue

                    if clicked:
                        break

                except Exception as e:
                    print(f"❌ Selector error: {e}")
                    continue

            if clicked:
                print("🎉 Successfully clicked! Waiting for popup...")
                time.sleep(10)  # Give more time for popup to load

                # Get updated page content
                detailed_content = driver.find_element(By.TAG_NAME, "body").text
                print("\n=== DETAILED POPUP CONTENT ===")
                print(detailed_content)

                # Extract token holdings from detailed content
                tokens = extract_tokens_from_content(detailed_content)
                return {
                    'basic_content': basic_content,
                    'detailed_content': detailed_content,
                    'tokens': tokens,
                    'click_success': True
                }
            else:
                print("❌ Could not click Holdings PnL")
                return {
                    'basic_content': basic_content,
                    'detailed_content': None,
                    'tokens': [],
                    'click_success': False
                }

        except Exception as e:
            print(f"❌ Popup extraction error: {e}")
            return {
                'basic_content': basic_content,
                'detailed_content': None,
                'tokens': [],
                'click_success': False
            }

        driver.quit()

    except Exception as e:
        print(f"❌ General error: {e}")
        try:
            driver.quit()
        except:
            pass
        return None

def extract_tokens_from_content(content):
    """
    Extract token holdings from the detailed content
    """
    tokens = []

    # Look for patterns like "GIGA $2.61K", "JTO $67.59", etc.
    patterns = [
        r'([A-Z]{2,10})\s*\$([0-9,.]+[KMB]?)',  # "GIGA $2.61K"
        r'\$([0-9,.]+[KMB]?)\s*([A-Z]{2,10})',  # "$2.61K GIGA"
        r'([A-Z]{2,10})\s*([0-9,.]+)\s*\$',     # "GIGA 1000 $"
    ]

    for pattern in patterns:
        matches = re.findall(pattern, content)
        for match in matches:
            if len(match) == 2:
                # Format: (token, amount) or (amount, token)
                if match[0].replace('.', '').replace(',', '').isdigit():
                    tokens.append(f"{match[1]}: ${match[0]}")
                else:
                    tokens.append(f"{match[0]}: ${match[1]}")

    # Remove duplicates
    return list(set(tokens))

if __name__ == "__main__":
    # Test with the wallet from the screenshot
    wallet = "A1N45nJh8eRn2zhXxP7SkqNKvR6rPXhbVgKzBGBxKEm8"
    result = extract_detailed_portfolio_data(wallet)

    if result:
        print(f"\n{'='*60}")
        print("FINAL RESULTS:")
        print(f"{'='*60}")
        print(f"Click successful: {result['click_success']}")
        print(f"Tokens found: {len(result['tokens'])}")
        for token in result['tokens']:
            print(f"  - {token}")
    else:
        print("❌ Failed to extract data")