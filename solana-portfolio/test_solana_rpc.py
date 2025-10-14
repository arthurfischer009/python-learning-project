#!/usr/bin/env python3
"""
Test direct Solana RPC for wallet token accounts
"""

import requests
import json

def test_solana_rpc():
    print("Testing Solana RPC for wallet data...")

    wallet_address = "61rVn8zeoikzFuT2cuXAd3Qv9RxhMDvG52xL4LHLv7Nu"

    # Free Solana RPC endpoints
    rpc_urls = [
        "https://api.mainnet-beta.solana.com",
        "https://solana-api.projectserum.com",
    ]

    for rpc_url in rpc_urls:
        try:
            print(f"\n=== Testing RPC: {rpc_url} ===")

            # Get token accounts for the wallet
            payload = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "getTokenAccountsByOwner",
                "params": [
                    wallet_address,
                    {
                        "programId": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"  # SPL Token program
                    },
                    {
                        "encoding": "jsonParsed"
                    }
                ]
            }

            response = requests.post(
                rpc_url,
                headers={"Content-Type": "application/json"},
                json=payload,
                timeout=10
            )

            print(f"Status: {response.status_code}")

            if response.status_code == 200:
                data = response.json()
                if "result" in data and "value" in data["result"]:
                    token_accounts = data["result"]["value"]
                    print(f"✅ Found {len(token_accounts)} token accounts!")

                    # Show first few token accounts
                    for i, account in enumerate(token_accounts[:3]):
                        token_data = account["account"]["data"]["parsed"]["info"]
                        mint = token_data["mint"]
                        balance = token_data["tokenAmount"]["uiAmount"]
                        print(f"  Token {i+1}: {mint[:8]}... Balance: {balance}")

                    return True
                else:
                    print(f"❌ Unexpected response: {data}")
            else:
                print(f"❌ Failed: {response.status_code}")

        except Exception as e:
            print(f"❌ Error: {e}")

    return False

if __name__ == "__main__":
    test_solana_rpc()