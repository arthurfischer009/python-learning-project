#!/usr/bin/env python3
"""
Test clean token extraction based on the actual popup structure
"""

def parse_popup_content(popup_content):
    """
    Parse the popup content to extract clean token holdings
    """
    lines = popup_content.split('\n')

    # Find the table section with token data
    current_holdings = []

    # Look for the pattern in the popup data
    # From our debug output, we know the structure includes lines like:
    # GIGA
    # 27d
    # +$0.083489...
    # $2.62K...

    i = 0
    while i < len(lines) - 3:
        line = lines[i].strip()

        # Look for token names (uppercase, 2-10 chars)
        if (line.isupper() and
            2 <= len(line) <= 10 and
            line.isalpha() and
            line not in ['USD', 'ALL', 'NEW']):  # Filter out common non-tokens

            token_name = line

            # Look ahead for balance information
            # Typically 3-4 lines down we find the balance
            for j in range(1, 8):  # Check next few lines
                if i + j < len(lines):
                    balance_line = lines[i + j].strip()

                    # Look for current balance (not sold all, not 0.00)
                    if ('$' in balance_line and
                        'sold all' not in balance_line.lower() and
                        not balance_line.startswith('$0.00') and
                        not balance_line.startswith('0.00')):

                        # Extract the dollar amount
                        import re
                        dollar_match = re.search(r'\$([0-9,.]+[KMB]?)', balance_line)
                        if dollar_match:
                            amount = dollar_match.group(1)

                            # Convert to float for filtering
                            try:
                                numeric_value = float(amount.replace('K', '000').replace('M', '000000').replace(',', ''))
                                if numeric_value > 0.01:  # Only meaningful balances
                                    current_holdings.append(f"{token_name}: ${amount}")
                                    break
                            except:
                                continue
        i += 1

    return current_holdings

# Test with the actual popup content from our debug
test_content = """
GIGA
27d
+$0.083489
0%
+$111.88
+4.39%
+$111.96
+2.17%
$2.62K
226K
$5.17K
$0.015032
$2.66K
$0.022664
65.9%
ye
29d
-$12.31
-12.32%
Holding
-$12.31
-12.32%
$87.59
143K
$99.9
$0.0369647
$0.00
-
100%
House
36d
Sold all
-$46.79
-4.93%
-$46.79
-4.93%
$0.00
0.00
$949.55
$0.015117
$902.76
$0.014372
0.00%
POPCAT
75d
-$0.0917851
-43.5%
+$140.91
+6.4%
+$140.91
+6.4%
$0.0923182
0.08100
$2.20K
$0.41033
$2.34K
$0.43659
1.86e-11%
"""

if __name__ == "__main__":
    print("Testing clean token extraction...")
    tokens = parse_popup_content(test_content)

    print(f"\nFound {len(tokens)} current token holdings:")
    for token in tokens:
        print(f"  - {token}")