# Solana Multi-Wallet Trading Journal

An automated trading journal dashboard that aggregates portfolio data from multiple Solana wallets using Jupiter's portfolio analysis. Perfect for traders who want to track multiple wallets in one unified view.

## ✨ Features

- **🔥 Multi-Wallet View** - Track multiple Solana wallets simultaneously (Jupiter doesn't have this!)
- **💰 Real-Time Portfolio Data** - Current USD balances for all token holdings
- **📊 Trading Analytics** - Win rates, PnL, transaction counts, and performance metrics
- **🎯 Automated Data Extraction** - Scrapes Jupiter's detailed portfolio analysis
- **📈 Visual Dashboard** - Clean Streamlit interface with charts and tables
- **💾 Data Export** - Download portfolio data as CSV for further analysis
- **🪙 Token Holdings** - Current USD values for each token position

## 🚀 Quick Start

### Prerequisites
- Python 3.13+
- Chrome browser (for Selenium automation)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/solana-trading-journal.git
   cd solana-trading-journal
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit selenium pandas plotly beautifulsoup4 requests
   ```

### Usage

**Run the dashboard:**
```bash
streamlit run portfolio_dashboard.py
```

**Open your browser** to `http://localhost:8501`

**Add wallet addresses** in the sidebar and click "Analyze Portfolios"

## 📊 What You Get

### Portfolio Analytics
- **Net Worth** - Current total value
- **Holdings PnL** - Total profit/loss from trading
- **Win Rate** - Success percentage of trades
- **Token Holdings** - Current USD value of each position

### Multi-Wallet Comparison
- **Side-by-side analysis** of multiple wallets
- **Aggregated performance** metrics
- **Individual token breakdowns**
- **Export capabilities** for further analysis

## 🛠️ Project Structure

```
├── portfolio_dashboard.py          # Main Streamlit dashboard
├── jupiter_portfolio_selenium.py   # Core extraction logic
├── multi_wallet_tracker.py         # Batch wallet analysis
├── enhanced_wallet_tracker.py      # Advanced popup extraction
└── test_*.py                       # Testing and debugging scripts
```

## 🎯 Why This Project?

Jupiter provides excellent portfolio analysis for individual wallets, but lacks:
- **Multi-wallet comparison** views
- **Batch analysis** capabilities
- **Data export** functionality
- **Custom dashboard** options

This trading journal fills that gap by automating Jupiter's data extraction and presenting it in a unified multi-wallet interface.

## 🔧 Technical Details

- **Selenium WebDriver** - Automates Jupiter website interaction
- **Beautiful Soup** - Parses portfolio data from popup modals
- **Streamlit** - Creates interactive web dashboard
- **Pandas** - Data processing and export
- **Plotly** - Interactive charts and visualizations

## 📝 Usage Examples

### Single Wallet Analysis
```python
python jupiter_portfolio_selenium.py
```

### Multi-Wallet Tracking
```python
python multi_wallet_tracker.py
```

### Custom Dashboard
```python
streamlit run portfolio_dashboard.py
```

## 🤝 Contributing

Contributions welcome! This project was built for rapid prototyping and can be extended with:
- **Additional DEX integrations** (Raydium, Orca, etc.)
- **Historical tracking** and trend analysis
- **Alert systems** for portfolio changes
- **Mobile-responsive** interface improvements

## 📄 License

MIT License - feel free to use and modify for your trading needs.

---

**⚡ Built with [Claude Code](https://claude.com/claude-code) for faster prototyping**

*This project demonstrates the power of AI-assisted development for quickly building functional trading tools and portfolio analytics.*