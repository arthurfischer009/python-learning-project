"""
Portfolio Allocation Calculator
================================

Dieses Script berechnet die prozentuale Verteilung (Allocation) von
drei verschiedenen Aktien/Assets in einem Investment-Portfolio.

Autor: Arthur Fischer
Datum: Oktober 2025

Konzept:
--------
Portfolio Allocation = Wie viel Prozent deines Gesamtkapitals ist in welchem Asset investiert?

Beispiel:
- Du hast $10,000 total
- $5,000 in Apple (AAPL) = 50%
- $3,000 in Google (GOOGL) = 30%
- $2,000 in Bitcoin (BTC) = 20%

Warum wichtig?
- Risikomanagement: Nicht alles in eine Aktie
- Diversifikation: Verluste in einem Asset durch Gewinne in anderen ausgleichen
- Portfolio-Rebalancing: Regelmäßig Allocation anpassen
"""


def portfolio_allocation(stock_a, stock_b, stock_c):
    """
    Berechne und zeige die prozentuale Allocation von drei Stocks/Assets.

    Diese Funktion nimmt drei Geldbeträge (Dollar/Euro) und berechnet
    wie viel Prozent jeder Betrag vom Gesamtportfolio ausmacht.

    Parameter:
    ----------
    stock_a : int oder float
        Der investierte Betrag in Stock A (z.B. $5000)
    stock_b : int oder float
        Der investierte Betrag in Stock B (z.B. $3000)
    stock_c : int oder float
        Der investierte Betrag in Stock C (z.B. $2000)

    Returns:
    --------
    None (gibt nichts zurück, printet nur die Ergebnisse)

    Beispiel:
    ---------
    >>> portfolio_allocation(5000, 3000, 2000)
    total amount is: 10000
    Stock A: 50.00%
    Stock B: 30.00%
    Stock C: 20.00%
    """

    # ============================================
    # SCHRITT 1: Berechne den Gesamtwert
    # ============================================

    # Addiere alle drei Investments um den Total Portfolio Value zu bekommen
    # Beispiel: 5000 + 3000 + 2000 = 10000
    total = stock_a + stock_b + stock_c

    # ============================================
    # SCHRITT 2: Berechne prozentuale Anteile
    # ============================================

    # Formel: (Einzelwert / Gesamtwert) * 100 = Prozent
    #
    # Beispiel für Stock A:
    # allocation_a = 5000 / 10000 * 100 = 0.5 * 100 = 50%
    #
    # Warum teilen wir durch total?
    # - Um den Anteil am Ganzen zu bekommen (0.0 bis 1.0)
    #
    # Warum * 100?
    # - Um aus dem Dezimalbruch (0.5) einen Prozentsatz (50%) zu machen

    allocation_a = stock_a / total * 100
    allocation_b = stock_b / total * 100
    allocation_c = stock_c / total * 100

    # ============================================
    # SCHRITT 3: Zeige die Ergebnisse
    # ============================================

    # Zeige den Gesamtwert des Portfolios
    print(f"total amount is: {total}")

    # Zeige die Allocation für jede Position
    # {allocation_a:.2f} bedeutet:
    # - {allocation_a} = Variable einsetzen
    # - :.2f = Format: 2 Dezimalstellen (fixed point)
    # - Beispiel: 50.0 wird zu "50.00"
    print(f"Stock A: {allocation_a:.2f}%")
    print(f"Stock B: {allocation_b:.2f}%")
    print(f"Stock C: {allocation_c:.2f}%")

    # Optional: Prüfe ob die Summe 100% ergibt (Sanity Check)
    # total_percent = allocation_a + allocation_b + allocation_c
    # assert round(total_percent) == 100, "Allocation muss 100% ergeben!"


# ============================================
# HAUPTPROGRAMM - User Input
# ============================================

# input() zeigt einen Text und wartet auf Benutzereingabe
# int() konvertiert den Text (String) zu einer Ganzzahl (Integer)
#
# Beispiel:
# User tippt: 5000
# input() gibt zurück: "5000" (String)
# int("5000") konvertiert zu: 5000 (Integer)

stock_a = int(input("Enter the stock A: "))
stock_b = int(input("Enter the stock B: "))
stock_c = int(input("Enter the stock C: "))

# ============================================
# Funktion aufrufen mit den eingegebenen Werten
# ============================================

portfolio_allocation(stock_a, stock_b, stock_c)


# ============================================
# LERNNOTIZEN:
# ============================================
#
# 1. FUNKTIONEN:
#    def funktionsname(parameter1, parameter2):
#        # Code hier
#        return ergebnis
#
# 2. F-STRINGS:
#    name = "Arthur"
#    print(f"Hallo {name}")  # Output: Hallo Arthur
#
# 3. STRING FORMATTING:
#    zahl = 3.14159
#    print(f"{zahl:.2f}")  # Output: 3.14 (2 Dezimalstellen)
#
# 4. INPUT & TYPE CONVERSION:
#    alter = int(input("Wie alt? "))  # String → Integer
#    preis = float(input("Preis? "))  # String → Float
#
# 5. DOCSTRINGS:
#    """
#    Beschreibung der Funktion
#    """
#    Wird mit help(funktionsname) angezeigt


# ============================================
# ERWEITERUNGSIDEEN:
# ============================================
#
# [ ] Error Handling: Was wenn User Text statt Zahl eingibt?
#     try:
#         stock_a = int(input("Stock A: "))
#     except ValueError:
#         print("Bitte eine Zahl eingeben!")
#
# [ ] Mehr als 3 Stocks: Liste verwenden
#     stocks = []
#     for i in range(5):
#         stocks.append(int(input(f"Stock {i+1}: ")))
#
# [ ] Visualization: Pie Chart mit matplotlib
#     import matplotlib.pyplot as plt
#     plt.pie([stock_a, stock_b, stock_c], labels=['A', 'B', 'C'])
#
# [ ] Save to File: Ergebnisse in CSV speichern
#     import csv
#     with open('portfolio.csv', 'w') as f:
#         writer = csv.writer(f)
#         writer.writerow(['Stock', 'Amount', 'Allocation'])
#
# [ ] Target Allocation: Soll/Ist-Vergleich
#     target = [40, 40, 20]  # Ziel: 40%, 40%, 20%
#     actual = [allocation_a, allocation_b, allocation_c]
#     difference = [t - a for t, a in zip(target, actual)]


# ============================================
# PORTFOLIO MANAGEMENT TIPPS:
# ============================================
#
# 1. DIVERSIFIKATION:
#    - Nicht mehr als 10-20% in einem einzelnen Stock
#    - Verschiedene Sektoren (Tech, Finance, Healthcare, etc.)
#    - Verschiedene Asset-Klassen (Stocks, Bonds, Crypto, Gold)
#
# 2. REBALANCING:
#    - Mindestens 1x pro Jahr Portfolio prüfen
#    - Wenn Allocation > 5% vom Ziel abweicht → Rebalancieren
#    - Beispiel: 60/40 Portfolio wird 70/30 → Verkaufe Stocks, kaufe Bonds
#
# 3. RISK MANAGEMENT:
#    - Risikotoleranz definieren (konservativ/moderat/aggressiv)
#    - Stop-Loss setzen (z.B. -10% dann verkaufen)
#    - Position Sizing (größere Positionen in sichereren Assets)
#
# 4. STEUER-OPTIMIERUNG:
#    - Tax-Loss Harvesting (Verluste realisieren für Steuervorteile)
#    - Haltefrist beachten (Long-term vs Short-term Capital Gains)
