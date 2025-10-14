# AFAR Trading Indicators

Custom Trading Indicators entwickelt für TradingView mit Pine Script.

## Überblick

Dieses Projekt enthält selbst entwickelte Trading-Indikatoren basierend auf verschiedenen technischen Analyse-Methoden. Die Indikatoren sind in Pine Script geschrieben und können direkt in TradingView verwendet werden.

## Dateien

### 1. AFAR Indicator (Original) - `AFAR indicator.ipynb`

**Jupyter Notebook** für die Entwicklung und Prototyping des AFAR Indikators.

**Verwendung:**
```bash
jupyter notebook indicators/AFAR\ indicator.ipynb
```

---

### 2. AFAR Indicator (Modified) - `AFAR_indicator_modified.pine`

**Pine Script Indikator** - Verbesserte Version mit zusätzlichen Features.

**Features:**
- Technische Indikatoren kombiniert
- Custom Signale für Ein- und Ausstiege
- Visuelle Alerts auf dem Chart

**Installation in TradingView:**

1. Gehe zu [TradingView](https://www.tradingview.com/)
2. Öffne einen Chart
3. Klicke auf "Pine Editor" (unten)
4. Kopiere den Code aus `AFAR_indicator_modified.pine`
5. Klicke "Add to Chart"

**Was der Indikator zeigt:**
```
🟢 BUY Signal  - Potentieller Einstiegspunkt
🔴 SELL Signal - Potentieller Ausstiegspunkt
📊 Trend Lines - Unterstützung und Widerstand
```

---

### 3. AFAR 3 Strategies - `AFAR_3_strategies.pine`

**Pine Script** mit **drei verschiedenen Trading-Strategien** kombiniert.

**Die 3 Strategien:**

#### Strategie 1: Trend Following
- Folgt dem übergeordneten Trend
- Nutzt Moving Averages
- Beste für starke Trends

#### Strategie 2: Mean Reversion
- Kauft bei Überverkauft
- Verkauft bei Überkauft
- Beste für Seitwärtsmärkte

#### Strategie 3: Breakout
- Erkennt Ausbrüche aus Konsolidierungen
- Volume-bestätigt
- Beste für volatile Märkte

**Verwendung:**
```pine
// In TradingView Pine Editor:
// 1. Wähle Strategy 1, 2 oder 3 in den Settings
// 2. Backteste auf historischen Daten
// 3. Optimiere Parameter
```

---

## Was ist Pine Script?

**Pine Script** ist die Programmiersprache von TradingView für:
- Custom Indicators (Indikatoren)
- Trading Strategies (Handelsstrategien)
- Alerts (Benachrichtigungen)

**Beispiel eines einfachen Indikators:**
```pine
//@version=5
indicator("Simple MA", overlay=true)

// Berechne 20-Tage Moving Average
ma = ta.sma(close, 20)

// Zeichne auf Chart
plot(ma, color=color.blue, linewidth=2)
```

---

## Trading Konzepte

### Moving Averages (MA)
Gleitende Durchschnitte glätten Preisbewegungen:
```
SMA(20) = (Preis1 + Preis2 + ... + Preis20) / 20
```

### RSI (Relative Strength Index)
Misst Momentum (0-100):
- RSI > 70: Überkauft (möglicherweise verkaufen)
- RSI < 30: Überverkauft (möglicherweise kaufen)

### Support & Resistance
- **Support**: Preislevel wo Käufer einsteigen
- **Resistance**: Preislevel wo Verkäufer verkaufen

### Breakout
Ausbruch aus einer Preisspanne:
```
Preis durchbricht Widerstand → Kaufsignal
Preis durchbricht Unterstützung → Verkaufsignal
```

---

## Installation & Verwendung

### Schritt 1: TradingView Account

Erstelle einen kostenlosen Account auf [TradingView.com](https://www.tradingview.com/)

### Schritt 2: Pine Editor öffnen

1. Öffne einen Chart (z.B. BTC/USD)
2. Klicke unten auf "Pine Editor"
3. Klicke "Open" → "New Blank Indicator"

### Schritt 3: Code einfügen

1. Lösche den Template-Code
2. Kopiere Code aus einer der `.pine` Dateien
3. Klicke "Save"
4. Klicke "Add to Chart"

### Schritt 4: Anpassen

Ändere Parameter in den Indicator Settings:
- Timeframe
- MA Periode
- RSI Levels
- etc.

---

## Für Arbeitgeber: Skills

Dieses Projekt zeigt:

### 1. **Technische Analyse**
- Verständnis von Trading-Indikatoren
- Strategieentwicklung
- Backtesting

### 2. **Pine Script Programming**
- Custom Indicator Development
- Algorithmic Trading
- Financial Mathematics

### 3. **Quantitative Analysis**
- Datenanalyse mit Jupyter
- Statistische Auswertungen
- Performance Metrics

### 4. **Trading Psychology**
- Risikomanagement
- Strategie-Kombinationen
- Multi-Timeframe-Analyse

### 5. **Problem Solving**
- Iterative Entwicklung (3 Versionen)
- Optimization
- Real-world Testing

---

## Backtesting

**Was ist Backtesting?**
Teste deine Strategie mit historischen Daten:

```
1. Wähle Zeitraum (z.B. 2023-2024)
2. Wende Strategie an
3. Messe Performance:
   - Win Rate
   - Profit Factor
   - Max Drawdown
```

**In TradingView:**
1. Öffne Strategy Tester Tab
2. Siehe Ergebnisse
3. Optimiere Parameter

---

## Performance Metriken

### Win Rate
```
Win Rate = (Gewinn-Trades / Gesamt-Trades) * 100
Beispiel: 60/100 = 60% Win Rate
```

### Profit Factor
```
Profit Factor = Gesamt-Gewinne / Gesamt-Verluste
> 1.0 = Profitabel
< 1.0 = Verluste
```

### Max Drawdown
Größter Verlust von Peak zu Trough:
```
Portfolio: $10,000 → $8,000 → $12,000
Max Drawdown: -20% ($10k → $8k)
```

### Sharpe Ratio
Risk-adjusted Returns:
```
Sharpe > 1.0 = Gut
Sharpe > 2.0 = Sehr gut
Sharpe > 3.0 = Exzellent
```

---

## Nächste Schritte

- [ ] **Machine Learning**: Integrate ML predictions
- [ ] **Multi-Asset**: Test auf verschiedenen Märkten (Forex, Crypto, Stocks)
- [ ] **Automated Trading**: Bot-Integration
- [ ] **Risk Management**: Position Sizing, Stop Loss Optimization
- [ ] **Live Trading**: Paper Trading → Real Money
- [ ] **Performance Dashboard**: Web-Interface für Tracking
- [ ] **Alert System**: Telegram/Email Notifications

---

## Trading Disclaimer

⚠️ **WICHTIG**: Dies ist ein Lernprojekt!

- Keine Anlageberatung
- Past Performance ≠ Future Results
- Teste immer mit Paper Trading zuerst
- Investiere nur was du bereit bist zu verlieren
- Lerne Risk Management bevor du real tradest

---

## Learning Resources

### TradingView & Pine Script:
- [Pine Script Documentation](https://www.tradingview.com/pine-script-docs/)
- [Pine Script Tutorial](https://www.tradingview.com/pine-script-docs/tutorials/)
- [TradingView Ideas](https://www.tradingview.com/ideas/) - Lerne von anderen

### Technische Analyse:
- [Investopedia - Technical Analysis](https://www.investopedia.com/terms/t/technicalanalysis.asp)
- [BabyPips - School of Pipsology](https://www.babypips.com/learn/forex) - Gratis Trading Kurs

### Bücher:
- "Technical Analysis of the Financial Markets" - John Murphy
- "A Beginner's Guide to the Stock Market" - Matthew Kratter
- "Trading for a Living" - Alexander Elder

### YouTube Channels:
- The Chart Guys
- Rayner Teo
- UKspreadbetting

---

## Code Beispiel

Einfacher AFAR-Style Indikator:

```pine
//@version=5
indicator("AFAR Simple", overlay=true)

// Inputs
ma_length = input.int(20, "MA Length")
rsi_length = input.int(14, "RSI Length")

// Berechnungen
ma = ta.sma(close, ma_length)
rsi = ta.rsi(close, rsi_length)

// Signale
buySignal = ta.crossover(close, ma) and rsi < 50
sellSignal = ta.crossunder(close, ma) and rsi > 50

// Plot
plot(ma, "Moving Average", color=color.blue, linewidth=2)
plotshape(buySignal, "Buy", shape.triangleup, location.belowbar, color.green, size=size.small)
plotshape(sellSignal, "Sell", shape.triangledown, location.abovebar, color.red, size=size.small)

// Alert
alertcondition(buySignal, "Buy Alert", "Potential Buy Signal!")
alertcondition(sellSignal, "Sell Alert", "Potential Sell Signal!")
```

---

## Kontakt & Fragen

Für Fragen zur Strategie oder zum Code, siehe die Jupyter Notebooks für detaillierte Erklärungen und Experimente.
