#!/usr/bin/env python3
"""
Quick test to see if we can scrape Jupiter portfolio data
"""

import requests
from bs4 import BeautifulSoup

def test_jupiter_scraping():
    print("Testing Jupiter portfolio scraping...")

    wallet_address = "61rVn8zeoikzFuT2cuXAd3Qv9RxhMDvG52xL4LHLv7Nu"
    url = f"https://jup.ag/portfolio/{wallet_address}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        print(f"Fetching: {url}")
        response = requests.get(url, headers=headers, timeout=10)
        print(f"Status code: {response.status_code}")
        print(f"Content length: {len(response.text)} characters")

        # Parse with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        print(f"Page title: {soup.title.string if soup.title else 'No title'}")

        # Get visible text
        page_text = soup.get_text()
        print(f"Visible text length: {len(page_text)} characters")

        # Show first 500 characters
        print("\n=== FIRST 500 CHARACTERS ===")
        print(page_text[:500])

        # Look for portfolio keywords
        keywords = ['SOL', 'balance', 'token', 'portfolio', 'value']
        print(f"\n=== KEYWORD SEARCH ===")
        for keyword in keywords:
            count = response.text.lower().count(keyword.lower())
            print(f"'{keyword}': {count} times")

        return True

    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    test_jupiter_scraping()