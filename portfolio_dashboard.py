#!/usr/bin/env python3
"""
Solana Portfolio Dashboard - Web interface for tracking multiple wallets
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Set page configuration
st.set_page_config(
    page_title="Solana Portfolio Dashboard",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

def get_wallet_data(wallet_address, driver):
    """
    Get detailed portfolio data for a single wallet
    """
    url = f"https://jup.ag/portfolio/{wallet_address}"

    try:
        driver.get(url)
        time.sleep(8)

        # Get basic page content
        basic_text = driver.find_element(By.TAG_NAME, "body").text

        portfolio_data = {
            'wallet': wallet_address,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'net_worth': 'N/A',
            'holdings_pnl': 'N/A',
            'jup_holdings': 'N/A',
            'win_rate': 'N/A',
            'total_txns': 'N/A',
            'avg_pnl_per_asset': 'N/A',
            'current_tokens': [],
            'token_count': 0,
            'status': 'success'
        }

        # Extract basic data
        lines = basic_text.split('\n')
        for i, line in enumerate(lines):
            if 'Net Worth' in line and i+1 < len(lines):
                portfolio_data['net_worth'] = lines[i+1].strip()
            elif 'Holdings PnL' in line and i+1 < len(lines):
                portfolio_data['holdings_pnl'] = lines[i+1].strip()
            elif 'JUP Holdings' in line and i+1 < len(lines):
                portfolio_data['jup_holdings'] = lines[i+1].strip()

        # Extract current token holdings
        try:
            # Look for token symbols and amounts in the text
            tokens_found = []

            # Common patterns for token holdings
            import re

            # Pattern for "41.08 SOL", "7.4625 USDC", etc.
            token_pattern = r'(\d+\.?\d*)\s+([A-Z]{2,10})\b'
            token_matches = re.findall(token_pattern, basic_text)

            for amount, token in token_matches:
                if float(amount) > 0 and token not in ['NEW', 'BUG']:  # Filter out noise
                    tokens_found.append(f"{amount} {token}")

            # Remove duplicates and limit to reasonable number
            unique_tokens = list(set(tokens_found))[:10]
            portfolio_data['current_tokens'] = unique_tokens
            portfolio_data['token_count'] = len(unique_tokens)

        except Exception as e:
            portfolio_data['current_tokens'] = []
            portfolio_data['token_count'] = 0

        # Try to click PnL popup for detailed data
        try:
            pnl_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'Holdings PnL')]")
            if pnl_elements:
                for element in pnl_elements:
                    if element.is_enabled() and element.is_displayed():
                        driver.execute_script("arguments[0].click();", element)
                        time.sleep(8)  # Give more time for popup

                        # Get detailed popup content
                        popup_content = driver.find_element(By.TAG_NAME, "body").text

                        # Extract additional metrics from popup
                        popup_lines = popup_content.split('\n')
                        for i, line in enumerate(popup_lines):
                            if 'Win Rate' in line and i+1 < len(popup_lines):
                                portfolio_data['win_rate'] = popup_lines[i+1].strip()
                            elif 'Txns' in line and i+1 < len(popup_lines):
                                portfolio_data['total_txns'] = popup_lines[i+1].strip()
                            elif 'Avg PnL per Asset' in line and i+1 < len(popup_lines):
                                portfolio_data['avg_pnl_per_asset'] = popup_lines[i+1].strip()

                        # Extract ONLY current token holdings - Trading Journal Precision
                        current_holdings = []
                        lines = popup_content.split('\n')

                        i = 0
                        while i < len(lines) - 15:
                            line = lines[i].strip()

                            # Look for token names
                            if (line.isupper() and
                                2 <= len(line) <= 10 and
                                line.isalpha() and
                                line not in ['USD', 'ALL', 'NEW', 'HOLDING', 'SOLD', 'PRICE', 'LAST', 'BALANCE', 'TOTAL']):

                                token_name = line

                                # The current balance is always at position +8 in Jupiter's table format
                                if i + 8 < len(lines):
                                    balance_line = lines[i + 8].strip()

                                    # Check if it's a valid balance format
                                    import re
                                    if re.match(r'^\$[0-9,.]+[KMB]?$', balance_line):
                                        amount_str = balance_line.replace('$', '').replace(',', '')

                                        try:
                                            # Convert to numeric for filtering
                                            if 'K' in amount_str:
                                                numeric_value = float(amount_str.replace('K', '')) * 1000
                                                display_amount = amount_str
                                            elif 'M' in amount_str:
                                                numeric_value = float(amount_str.replace('M', '')) * 1000000
                                                display_amount = amount_str
                                            else:
                                                numeric_value = float(amount_str)
                                                display_amount = amount_str

                                            # Only include meaningful current balances (> $50 to filter out dust)
                                            if numeric_value > 50:
                                                current_holdings.append(f"{token_name}: ${display_amount}")

                                        except ValueError:
                                            pass

                            i += 1

                        portfolio_data['current_tokens'] = current_holdings
                        portfolio_data['token_count'] = len(portfolio_data['current_tokens'])

                        break
        except Exception as e:
            portfolio_data['current_tokens'] = []
            portfolio_data['token_count'] = 0

        return portfolio_data

    except Exception as e:
        return {
            'wallet': wallet_address,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'net_worth': 'ERROR',
            'holdings_pnl': 'ERROR',
            'jup_holdings': 'ERROR',
            'win_rate': 'ERROR',
            'total_txns': 'ERROR',
            'avg_pnl_per_asset': 'ERROR',
            'current_tokens': [],
            'token_count': 0,
            'status': f'error: {str(e)}'
        }

def extract_numeric_value(value_str):
    """
    Extract numeric value from strings like '$2,232,456.59' or '+$1.22K'
    """
    if pd.isna(value_str) or value_str in ['N/A', 'ERROR']:
        return 0

    # Remove $ and + signs, handle K/M suffixes
    clean_str = str(value_str).replace('$', '').replace('+', '').replace(',', '')

    if 'K' in clean_str:
        return float(clean_str.replace('K', '')) * 1000
    elif 'M' in clean_str:
        return float(clean_str.replace('M', '')) * 1000000
    else:
        try:
            return float(clean_str)
        except:
            return 0

def main():
    st.title("🚀 Solana Portfolio Dashboard")
    st.markdown("Track multiple Solana wallets with Jupiter portfolio data")

    # Sidebar for wallet input
    st.sidebar.header("📝 Add Wallets")

    # Initialize session state
    if 'wallets' not in st.session_state:
        st.session_state.wallets = []
    if 'results' not in st.session_state:
        st.session_state.results = pd.DataFrame()

    # Wallet input
    new_wallet = st.sidebar.text_input(
        "Enter wallet address:",
        placeholder="61rVn8zeoikzFuT2cuXAd3Qv9RxhMDvG52xL4LHLv7Nu"
    )

    if st.sidebar.button("➕ Add Wallet"):
        if new_wallet and new_wallet not in st.session_state.wallets:
            st.session_state.wallets.append(new_wallet)
            st.sidebar.success(f"Added: {new_wallet[:8]}...")
        elif new_wallet in st.session_state.wallets:
            st.sidebar.warning("Wallet already added!")

    # Show current wallets
    st.sidebar.subheader("📋 Current Wallets")
    for i, wallet in enumerate(st.session_state.wallets):
        col1, col2 = st.sidebar.columns([3, 1])
        col1.text(f"{wallet[:8]}...{wallet[-8:]}")
        if col2.button("🗑️", key=f"remove_{i}"):
            st.session_state.wallets.pop(i)
            st.rerun()

    # Quick add popular wallets
    st.sidebar.subheader("⚡ Quick Add")
    sample_wallets = {
        "High PnL Wallet": "61rVn8zeoikzFuT2cuXAd3Qv9RxhMDvG52xL4LHLv7Nu",
        "Another Wallet": "9QEHSyTqyRNDSvbYtFjqR2e5UXNfvjpAcEdTqAjSwVmH"
    }

    for name, address in sample_wallets.items():
        if st.sidebar.button(f"Add {name}"):
            if address not in st.session_state.wallets:
                st.session_state.wallets.append(address)
                st.sidebar.success(f"Added {name}!")

    # Main area
    if len(st.session_state.wallets) == 0:
        st.info("👆 Add some wallet addresses in the sidebar to get started!")
        st.markdown("""
        ### How to use:
        1. **Add wallet addresses** in the sidebar
        2. **Click 'Analyze Portfolios'** to fetch data
        3. **View results** in the dashboard below

        ### Features:
        - 📊 Portfolio PnL tracking
        - 💰 Net worth analysis
        - 🎯 Win rate statistics
        - 📈 Interactive charts
        - 💾 Data export
        """)
        return

    # Analyze button
    if st.button("🔍 Analyze Portfolios", type="primary"):
        if len(st.session_state.wallets) > 0:
            with st.spinner(f"Analyzing {len(st.session_state.wallets)} wallets..."):

                # Set up Chrome driver
                chrome_options = Options()
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--no-sandbox")
                chrome_options.add_argument("--disable-dev-shm-usage")

                results = []
                progress_bar = st.progress(0)

                try:
                    driver = webdriver.Chrome(options=chrome_options)

                    for i, wallet in enumerate(st.session_state.wallets):
                        st.write(f"Processing wallet {i+1}/{len(st.session_state.wallets)}: {wallet[:8]}...")

                        wallet_data = get_wallet_data(wallet, driver)
                        results.append(wallet_data)

                        progress_bar.progress((i + 1) / len(st.session_state.wallets))
                        time.sleep(2)

                    driver.quit()

                    # Store results
                    st.session_state.results = pd.DataFrame(results)
                    st.success(f"✅ Successfully analyzed {len(results)} wallets!")

                except Exception as e:
                    st.error(f"❌ Error during analysis: {e}")
                    try:
                        driver.quit()
                    except:
                        pass

    # Display results
    if not st.session_state.results.empty:
        st.header("📊 Portfolio Analysis Results")

        # Summary metrics
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            total_wallets = len(st.session_state.results)
            st.metric("Total Wallets", total_wallets)

        with col2:
            successful = len(st.session_state.results[st.session_state.results['status'] == 'success'])
            st.metric("Successful", successful)

        with col3:
            # Calculate total PnL
            total_pnl = 0
            for _, row in st.session_state.results.iterrows():
                pnl_value = extract_numeric_value(row['holdings_pnl'])
                total_pnl += pnl_value
            st.metric("Total PnL", f"${total_pnl:,.0f}")

        with col4:
            avg_pnl = total_pnl / max(successful, 1)
            st.metric("Avg PnL", f"${avg_pnl:,.0f}")

        # Detailed table
        st.subheader("📋 Detailed Results")

        # Format the dataframe for display
        display_df = st.session_state.results.copy()
        display_df['wallet_short'] = display_df['wallet'].apply(lambda x: f"{x[:8]}...{x[-8:]}")

        # Select columns to display
        cols_to_show = ['wallet_short', 'net_worth', 'holdings_pnl', 'jup_holdings', 'token_count', 'win_rate', 'total_txns', 'status']
        display_df = display_df[cols_to_show]

        st.dataframe(display_df, width='stretch')

        # Show token holdings details
        st.subheader("🪙 Current Token Holdings")

        for index, row in st.session_state.results.iterrows():
            if row['status'] == 'success' and row['current_tokens']:
                with st.expander(f"💰 {row['wallet'][:8]}... Token Holdings ({row['token_count']} tokens)"):
                    tokens_text = " | ".join(row['current_tokens'])
                    st.write(f"**Tokens:** {tokens_text}")
            elif row['status'] == 'success':
                with st.expander(f"💰 {row['wallet'][:8]}... Token Holdings"):
                    st.write("🔍 No current token holdings detected or wallet is empty")

        # Charts
        st.subheader("📈 Portfolio Visualizations")

        # PnL Chart
        pnl_data = []
        wallet_labels = []

        for _, row in st.session_state.results.iterrows():
            if row['status'] == 'success':
                pnl_value = extract_numeric_value(row['holdings_pnl'])
                pnl_data.append(pnl_value)
                wallet_labels.append(f"{row['wallet'][:8]}...")

        if pnl_data:
            fig = px.bar(
                x=wallet_labels,
                y=pnl_data,
                title="Holdings PnL by Wallet",
                labels={'x': 'Wallet', 'y': 'PnL ($)'}
            )
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig, use_container_width=True)

        # Download data
        st.subheader("💾 Export Data")
        csv = st.session_state.results.to_csv(index=False)
        st.download_button(
            label="📄 Download CSV",
            data=csv,
            file_name=f"portfolio_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main()