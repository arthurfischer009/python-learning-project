# Portfolio Tools

Nützliche Tools für Portfolio-Management und Analyse.

## Überblick

Diese Tools helfen dir bei der Verwaltung und Analyse deines Investment-Portfolios, insbesondere bei der Berechnung von Portfolio-Allokationen.

---

## Portfolio Allocation Calculator (`portfolio_allocation.py`)

### Was macht dieses Tool?

Der **Portfolio Allocation Calculator** berechnet die prozentuale Verteilung deiner Investments über verschiedene Aktien/Assets hinweg.

### Warum ist das wichtig?

**Diversifikation** ist ein Kernprinzip des Investierens:
- Verteile dein Risiko über mehrere Assets
- Vermeide Übergewichtung einzelner Positionen
- Balanciere dein Portfolio nach deiner Risikotoleranz

### Beispiel

Du hast investiert:
- Stock A: $5,000
- Stock B: $3,000
- Stock C: $2,000

**Output:**
```
Total amount is: 10000
Stock A: 50.00%
Stock B: 30.00%
Stock C: 20.00%
```

**Interpretation:**
- 50% deines Portfolios ist in Stock A (höchstes Risiko bei A)
- 30% in Stock B
- 20% in Stock C

---

## Verwendung

### Direkt ausführen:

```bash
python portfolio-tools/portfolio_allocation.py
```

### Interaktive Eingabe:

```
Enter the stock A: 5000
Enter the stock B: 3000
Enter the stock C: 2000
```

### Als Funktion verwenden:

```python
from portfolio_allocation import portfolio_allocation

# Berechne Allocation
portfolio_allocation(5000, 3000, 2000)
```

---

## Code-Erklärung

### Die Funktion im Detail:

```python
def portfolio_allocation(stock_a, stock_b, stock_c):
    # 1. Berechne Gesamtwert
    total = stock_a + stock_b + stock_c

    # 2. Berechne prozentuale Anteile
    allocation_a = stock_a / total * 100  # z.B. 5000/10000 * 100 = 50%

    # 3. Zeige Ergebnisse
    print(f"Stock A: {allocation_a:.2f}%")  # .2f = 2 Dezimalstellen
```

### Python Konzepte die du lernst:

1. **Funktionen**: Wiederverwendbarer Code mit Parametern
2. **User Input**: `input()` für Benutzereingaben
3. **Type Conversion**: `int()` konvertiert String zu Integer
4. **String Formatting**: f-strings für formatierte Ausgabe
5. **Mathematische Operationen**: Division und Multiplikation
6. **Docstrings**: Funktionsdokumentation

---

## Portfolio-Management Konzepte

### 1. Diversifikation

**"Don't put all your eggs in one basket"**

Ideale Portfolio-Verteilung (Beispiel):
```
60% Aktien (Stocks)
30% Anleihen (Bonds)
10% Alternative (Crypto, Gold, etc.)
```

### 2. Asset Allocation

Verteilung nach Anlageklassen:
```python
# Beispiel: Aggressive Portfolio
stocks = 0.80      # 80% Aktien
bonds = 0.15       # 15% Anleihen
cash = 0.05        # 5% Cash
```

### 3. Rebalancing

Portfolio regelmäßig anpassen:

```
Start:    60% Stock A, 40% Stock B
Nach Jahr: 75% Stock A, 25% Stock B (A ist gestiegen)

Rebalancing: Verkaufe A, kaufe B → zurück zu 60/40
```

### 4. Risk Management

**Maximum Position Size:**
```python
# Regel: Keine Einzelposition > 10% vom Portfolio
if allocation > 10:
    print("WARNING: Position zu groß!")
```

---

## Erweiterte Features (für die Zukunft)

### Multi-Asset Support

Aktuell: 3 Stocks
Zukünftig: Beliebig viele Assets

```python
def portfolio_allocation_advanced(*assets):
    total = sum(assets)
    for i, asset in enumerate(assets):
        print(f"Asset {i+1}: {asset/total*100:.2f}%")
```

### Ziel-Allocation Vergleich

Vergleiche aktuelle mit gewünschter Allocation:

```python
def check_allocation(current, target):
    """
    current = [50, 30, 20]  # Aktuelle %
    target = [40, 40, 20]   # Ziel %
    """
    difference = [c - t for c, t in zip(current, target)]
    return difference  # [-10, +10, 0]
```

### Risk Metrics

```python
def portfolio_risk(weights, volatilities):
    """
    weights = [0.5, 0.3, 0.2]  # Allocation
    volatilities = [0.2, 0.15, 0.25]  # Risiko pro Asset
    """
    portfolio_vol = sum(w * v for w, v in zip(weights, volatilities))
    return portfolio_vol
```

---

## Für Arbeitgeber: Skills

Dieses Projekt zeigt:

### 1. **Financial Literacy**
- Portfolio Management
- Risk Management
- Diversifikation-Strategien

### 2. **Python Fundamentals**
- Funktionen und Parameter
- User Input Handling
- String Formatting
- Type Conversion

### 3. **Mathematical Modeling**
- Prozentuale Berechnungen
- Gewichtete Durchschnitte
- Financial Formulas

### 4. **Clean Code**
- Docstrings
- Beschreibende Variablennamen
- Modulare Funktionen

### 5. **User Experience**
- Klare Input-Prompts
- Formatierte Ausgabe
- Benutzerfreundlichkeit

---

## Nächste Schritte

- [ ] **Multi-Asset**: Unterstützung für mehr als 3 Positionen
- [ ] **Datenvisualisierung**: Pie Chart mit matplotlib
- [ ] **CSV Import**: Portfolio aus Datei laden
- [ ] **Target Allocation**: Soll/Ist-Vergleich
- [ ] **Rebalancing Calculator**: Wie viel kaufen/verkaufen?
- [ ] **Risk Metrics**: Volatilität, Sharpe Ratio berechnen
- [ ] **Historical Performance**: Integration mit yfinance
- [ ] **Web Interface**: Streamlit Dashboard

---

## Beispiel-Szenarien

### Szenario 1: Balanced Portfolio

```
Stock A (Tech): $4,000    → 40%
Stock B (Finance): $3,000 → 30%
Stock C (Healthcare): $3,000 → 30%

Total: $10,000
Risk: Medium (gut diversifiziert)
```

### Szenario 2: Aggressive Portfolio

```
Stock A (Crypto): $7,000  → 70%
Stock B (Growth): $2,000  → 20%
Stock C (Blue Chip): $1,000 → 10%

Total: $10,000
Risk: High (übergewichtet in Crypto)
⚠️ WARNING: Zu viel Risiko in einer Position!
```

### Szenario 3: Conservative Portfolio

```
Stock A (S&P 500 ETF): $5,000  → 50%
Stock B (Bond ETF): $3,000     → 30%
Stock C (Gold): $2,000         → 20%

Total: $10,000
Risk: Low (stabile, defensive Assets)
```

---

## Learning Resources

### Portfolio Management:
- [Investopedia - Portfolio Management](https://www.investopedia.com/terms/p/portfoliomanagement.asp)
- [Bogleheads - Asset Allocation](https://www.bogleheads.org/wiki/Asset_allocation)

### Python for Finance:
- [Python for Finance by Yves Hilpisch](https://www.oreilly.com/library/view/python-for-finance/9781492024323/)
- [Quantitative Finance](https://www.quantopian.com/)

### Financial Concepts:
- **Modern Portfolio Theory** - Harry Markowitz
- **Efficient Frontier** - Optimale Risk/Return
- **Sharpe Ratio** - Risk-adjusted Performance

---

## Code Improvements (Advanced)

### Mit Error Handling:

```python
def portfolio_allocation_safe(stock_a, stock_b, stock_c):
    try:
        # Prüfe auf negative Werte
        if any(s < 0 for s in [stock_a, stock_b, stock_c]):
            raise ValueError("Negative investments not allowed!")

        total = stock_a + stock_b + stock_c

        # Prüfe auf 0
        if total == 0:
            raise ValueError("Total portfolio value cannot be zero!")

        # Berechnung...

    except ValueError as e:
        print(f"Error: {e}")
```

### Mit Klassen (OOP):

```python
class Portfolio:
    def __init__(self):
        self.positions = {}

    def add_position(self, name, amount):
        self.positions[name] = amount

    def calculate_allocation(self):
        total = sum(self.positions.values())
        return {name: (amount/total)*100
                for name, amount in self.positions.items()}

    def display(self):
        allocations = self.calculate_allocation()
        for name, percent in allocations.items():
            print(f"{name}: {percent:.2f}%")

# Verwendung:
p = Portfolio()
p.add_position("AAPL", 5000)
p.add_position("GOOGL", 3000)
p.add_position("BTC", 2000)
p.display()
```

---

## Kontakt

Für Fragen oder Verbesserungsvorschläge, siehe die anderen Projekte in diesem Repository für weitere Finance-Tools!
