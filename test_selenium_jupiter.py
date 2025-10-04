#!/usr/bin/env python3
"""
Test Selenium to scrape Jupiter portfolio data with all PnL and values
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

def scrape_jupiter_portfolio_selenium():
    print("Testing Selenium scraping of Jupiter portfolio...")

    wallet_address = "61rVn8zeoikzFuT2cuXAd3Qv9RxhMDvG52xL4LHLv7Nu"
    url = f"https://jup.ag/portfolio/{wallet_address}"

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in background
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    try:
        print(f"Opening Jupiter portfolio page: {url}")

        # Create webdriver (this will auto-download ChromeDriver if needed)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)

        print("Waiting for page to load...")
        # Wait for the page to load and portfolio data to appear
        wait = WebDriverWait(driver, 20)

        # Wait for portfolio content to load (look for common portfolio elements)
        time.sleep(10)  # Give extra time for JavaScript to load data

        print("Page loaded! Getting page content...")

        # Get all text content
        page_source = driver.page_source
        page_text = driver.find_element(By.TAG_NAME, "body").text

        print(f"Page source length: {len(page_source)} characters")
        print(f"Visible text length: {len(page_text)} characters")

        # Look for portfolio keywords in the visible text
        keywords = ['SOL', 'USDC', '$', 'balance', 'total', 'PnL', '%', 'portfolio']
        print(f"\n=== KEYWORD SEARCH IN VISIBLE TEXT ===")
        for keyword in keywords:
            count = page_text.lower().count(keyword.lower())
            print(f"'{keyword}': {count} times")

        # Show first 1000 characters of visible text
        print(f"\n=== FIRST 1000 CHARACTERS OF VISIBLE TEXT ===")
        print(page_text[:1000])

        # Try to find specific portfolio elements
        print(f"\n=== LOOKING FOR PORTFOLIO ELEMENTS ===")
        try:
            # Look for common portfolio element patterns
            elements = driver.find_elements(By.XPATH, "//*[contains(text(), '$') or contains(text(), 'SOL') or contains(text(), 'USDC')]")
            print(f"Found {len(elements)} elements with $ or token symbols")

            for i, element in enumerate(elements[:10]):  # Show first 10
                text = element.text.strip()
                if text and len(text) < 100:  # Skip very long texts
                    print(f"  {i+1}: {text}")

        except Exception as e:
            print(f"Error finding elements: {e}")

        driver.quit()
        return True

    except Exception as e:
        print(f"Error: {e}")
        try:
            driver.quit()
        except:
            pass
        return False

if __name__ == "__main__":
    scrape_jupiter_portfolio_selenium()