# Solana Portfolio Tracker

Ein umfassendes Portfolio-Tracking-System für Solana Wallets mit Web-Dashboard, Multi-Wallet-Unterstützung und automatischer Datenextraktion.

## Überblick

Dieses Projekt ermöglicht es dir, mehrere Solana-Wallets gleichzeitig zu überwachen, Portfolio-Daten zu sammeln und in einem Dashboard zu visualisieren. Es nutzt Web Scraping um Daten von Jupiter Exchange zu extrahieren.

## Hauptkomponenten

### 1. Portfolio Dashboard (`portfolio_dashboard.py`)

**Was es macht:**
- Web-Interface mit Streamlit
- Zeigt Net Worth, PnL, Win Rate und mehr
- Visualisiert Portfolio-Performance mit interaktiven Charts
- Multi-Wallet-Unterstützung

**Features:**
- 💰 **Net Worth Tracking**: Gesamtwert aller Wallets
- 📊 **PnL Analyse**: Gewinn/Verlust-Übersicht
- 🎯 **Win Rate**: Erfolgsquote deiner Trades
- 📈 **Charts**: Interaktive Visualisierungen mit Plotly
- 👛 **Multi-Wallet**: Mehrere Wallets gleichzeitig tracken

**Verwendung:**
```bash
streamlit run solana-portfolio/portfolio_dashboard.py
```

**Technologien:**
- `streamlit` - Web-Dashboard Framework
- `plotly` - Interaktive Charts
- `selenium` - Web Scraping
- `pandas` - Datenverarbeitung

---

### 2. Multi-Wallet Tracker (`multi_wallet_tracker.py`)

**Was es macht:**
Automatisches Tracking von mehreren Wallets mit Datenexport.

**Features:**
- Mehrere Wallets parallel überwachen
- Automatischer Export zu CSV
- Zeitgestempelte Snapshots

**Verwendung:**
```python
# Wallet-Adressen in der Datei eintragen
wallets = [
    "deine_wallet_adresse_1",
    "deine_wallet_adresse_2"
]
```

---

### 3. Enhanced Wallet Tracker (`enhanced_wallet_tracker.py`)

**Was es macht:**
Erweiterter Tracker mit detaillierter Token-Extraktion.

**Konzepte:**
- Token-Holding Analyse
- Current Holdings vs. Historical Trades
- PnL per Token

---

### 4. Token Extractors

Verschiedene Versionen für die Extraktion von Token-Daten:

- `fixed_token_extractor.py` - Basis-Extraktor
- `precise_token_extractor.py` - Verbesserte Genauigkeit
- `current_holdings_only.py` - Nur aktuelle Holdings

---

### 5. Jupiter Integration (`jupiter_portfolio_selenium.py`)

**Was es macht:**
Direkte Integration mit Jupiter Exchange Portfolio-Seite.

**Jupiter Exchange:**
Jupiter ist der führende DEX Aggregator auf Solana. Die Portfolio-Seite zeigt:
- Wallet Balance
- Token Holdings
- Trading History
- PnL Statistiken

---

### 6. Test Scripts

Verschiedene Test-Dateien für Entwicklung und Debugging:

- `test_selenium_jupiter.py` - Selenium Setup testen
- `test_solana_rpc.py` - Solana RPC Verbindung testen
- `test_scraping.py` - Web Scraping testen
- `test_clean_extraction.py` - Datenextraktion testen
- `debug_tokens.py` - Token-Parsing debuggen

---

## Installation

### 1. Benötigte Pakete installieren:

```bash
# Virtual Environment aktivieren
source .venv/bin/activate

# Pakete installieren
pip install streamlit pandas plotly selenium webdriver-manager
```

### 2. Chrome WebDriver:

Das Projekt nutzt Selenium mit Chrome. Der WebDriver wird automatisch heruntergeladen.

Alternativ manuell installieren:
```bash
# macOS mit Homebrew
brew install chromedriver

# Oder mit webdriver-manager (empfohlen)
pip install webdriver-manager
```

---

## Verwendung

### Dashboard starten:

```bash
streamlit run solana-portfolio/portfolio_dashboard.py
```

### Multi-Wallet Tracking:

```bash
python solana-portfolio/multi_wallet_tracker.py
```

### Einzelnes Wallet analysieren:

```bash
python solana-portfolio/enhanced_wallet_tracker.py
```

---

## Für Arbeitgeber: Technische Skills

Dieses Projekt demonstriert:

### 1. **Web Scraping**
- Selenium WebDriver
- Dynamische Webseiten scrapen
- Error Handling bei Network Requests

### 2. **Data Engineering**
- Pandas DataFrames
- CSV Export/Import
- Datenbereinigung und -transformation

### 3. **Web Development**
- Streamlit Dashboards
- Interaktive UI-Komponenten
- Real-time Data Updates

### 4. **Blockchain/Crypto**
- Solana Blockchain Verständnis
- Wallet-Adressen
- DEX (Decentralized Exchange) Integration

### 5. **Software Architecture**
- Modulare Code-Struktur
- Separation of Concerns
- Test-Driven Development (Test Scripts)

### 6. **Data Visualization**
- Plotly Charts
- Interactive Graphs
- Financial Metrics Display

---

## Wichtige Konzepte

### Was ist eine Solana Wallet?

Eine Wallet-Adresse ist wie eine Kontonummer auf der Solana Blockchain:
```
Beispiel: 7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU
```

### Was ist Jupiter?

Jupiter (jup.ag) ist der größte DEX Aggregator auf Solana:
- Findet beste Preise über mehrere DEXs
- Portfolio-Tracking
- Trading History

### PnL (Profit and Loss)

Gewinn/Verlust Berechnung:
```
PnL = (Verkaufspreis - Kaufpreis) / Kaufpreis * 100
```

### Win Rate

Prozentsatz erfolgreicher Trades:
```
Win Rate = (Anzahl Gewinne / Anzahl Gesamt Trades) * 100
```

---

## Datenstruktur

### CSV Export Format:

```csv
wallet,timestamp,net_worth,holdings_pnl,win_rate,total_txns
wallet123,2025-10-13 18:00:00,$5420.50,+$1234.50,68.5%,142
```

---

## Nächste Schritte / Erweiterungen

- [ ] **Real-time Updates**: WebSocket Integration für Live-Daten
- [ ] **Price Alerts**: Benachrichtigungen bei Preisänderungen
- [ ] **Historical Charts**: Zeitverlauf des Portfolio-Werts
- [ ] **Tax Reports**: Steuerreport-Export
- [ ] **Mobile App**: React Native App
- [ ] **API Integration**: Direkte Solana RPC statt Scraping
- [ ] **Database**: PostgreSQL statt CSV
- [ ] **Authentication**: Multi-User Support

---

## Troubleshooting

### ChromeDriver Error:

```bash
# WebDriver Manager verwenden
pip install webdriver-manager
```

### Selenium Timeout:

```python
# Erhöhe Wartezeit in den Scripts
time.sleep(10)  # statt 5 Sekunden
```

### Jupiter Website Änderungen:

Wenn Jupiter ihre Website ändert, müssen die Selektoren angepasst werden:
```python
# In den Scraping-Scripts:
element = driver.find_element(By.CLASS_NAME, "neuer_class_name")
```

---

## Learning Resources

### Solana:
- [Solana Docs](https://docs.solana.com/)
- [Solana Explorer](https://explorer.solana.com/)

### Jupiter:
- [Jupiter Exchange](https://jup.ag/)
- [Jupiter Docs](https://station.jup.ag/docs)

### Selenium:
- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [Web Scraping Tutorial](https://realpython.com/modern-web-automation-with-python-and-selenium/)

### Streamlit:
- [Streamlit Docs](https://docs.streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery)
