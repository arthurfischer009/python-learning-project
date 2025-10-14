#!/usr/bin/env python3
"""
Test Solana Tracker API for portfolio data
"""

import requests
import json

def test_solana_tracker_api():
    print("Testing Solana Tracker API...")

    wallet_address = "61rVn8zeoikzFuT2cuXAd3Qv9RxhMDvG52xL4LHLv7Nu"
    base_url = "https://data.solanatracker.io"

    # Test different endpoints
    endpoints = [
        f"/wallet/{wallet_address}/basic",  # Basic wallet info
        f"/wallet/{wallet_address}",        # Full wallet tokens
        f"/wallet/{wallet_address}/trades", # Recent trades
    ]

    for endpoint in endpoints:
        try:
            print(f"\n=== Testing: {endpoint} ===")
            url = base_url + endpoint

            response = requests.get(url, timeout=10)
            print(f"Status: {response.status_code}")

            if response.status_code == 200:
                data = response.json()
                print(f"✅ Success! Data preview:")
                print(json.dumps(data, indent=2)[:500] + "...")
            else:
                print(f"❌ Failed: {response.status_code}")
                print(f"Response: {response.text[:200]}")

        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_solana_tracker_api()