#!/usr/bin/env python3
"""
Debug token detection - see what Jupiter actually shows
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import re

def debug_token_detection(wallet_address):
    """
    Debug what content we get from Jupiter for token detection
    """
    url = f"https://jup.ag/portfolio/{wallet_address}"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        time.sleep(10)

        # Get page content
        page_text = driver.find_element(By.TAG_NAME, "body").text

        print("=== FULL PAGE CONTENT ===")
        print(page_text)
        print("\n" + "="*60)

        # Try different token patterns
        patterns = [
            r'(\d+\.?\d*)\s+([A-Z]{2,10})\b',     # "41.08 SOL"
            r'(\d+\.?\d*)\s*([A-Z]{3,6})',        # "41.08SOL" or "41.08 SOL"
            r'([A-Z]{2,6})\s*(\d+\.?\d*)',        # "SOL 41.08"
            r'(\d+[\.,]\d+)\s*([A-Z]{2,6})',      # "41,08 SOL" (comma decimal)
        ]

        for i, pattern in enumerate(patterns):
            print(f"\n--- PATTERN {i+1}: {pattern} ---")
            matches = re.findall(pattern, page_text)
            print(f"Found {len(matches)} matches:")
            for match in matches[:10]:  # Show first 10
                print(f"  {match}")

        # Look for specific sections that might contain tokens
        print("\n--- SEARCHING FOR SPECIFIC SECTIONS ---")

        # Look for lines containing common token names
        lines = page_text.split('\n')
        token_lines = []

        common_tokens = ['SOL', 'USDC', 'USDT', 'BTC', 'ETH', 'BONK', 'WIF', 'JUP', 'RAY', 'ORCA']

        for line in lines:
            for token in common_tokens:
                if token in line and any(char.isdigit() for char in line):
                    token_lines.append(line.strip())
                    break

        print("Lines with potential token data:")
        for line in token_lines:
            print(f"  '{line}'")

        driver.quit()

    except Exception as e:
        print(f"Error: {e}")
        try:
            driver.quit()
        except:
            pass

if __name__ == "__main__":
    # Test with both wallets
    wallets = [
        "A1N45nJh8eRn2zhXxP7SkqNKvR6rPXhbVgKzBGBxKEm8",
        "FXtjTqbZdKBwG38NVoKNnZAUUGDJXRy27ta7L4SB9Fvk"
    ]

    for wallet in wallets:
        print(f"\n{'='*60}")
        print(f"TESTING WALLET: {wallet}")
        print('='*60)
        debug_token_detection(wallet)