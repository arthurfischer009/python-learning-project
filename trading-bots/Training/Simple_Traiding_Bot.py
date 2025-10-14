"""
Simple Trading Bot - Moving Average Strategy
============================================

Dieser Trading Bot implementiert eine einfache Moving Average (MA) Strategie.
Er vergleicht den aktuellen Aktienkurs mit dem Moving Average und
generiert Kauf-, Verkauf- oder Halte-Signale basierend auf Risikotoleranz.

Autor: Arthur Fischer
Datum: Oktober 2025
"""

# ============================================
# SCHRITT 1: Variablen definieren
# ============================================

# Aktienkurs: Der aktuelle Marktpreis der Aktie (in Euro/Dollar)
# Beispiel: 155 bedeutet die Aktie kostet aktuell 155€
Aktienkurs = 155

# MA (Moving Average): Der Durchschnittspreis über einen bestimmten Zeitraum
# Beispiel: 145 ist der Durchschnitt der letzten X Tage
# Ein steigender MA deutet auf einen Aufwärtstrend hin
MA = 145

# Risikotoleranz: Wie viel Risiko sind wir bereit einzugehen? (als Dezimalzahl)
# 0.05 = 5% - bedeutet wir kaufen nur wenn die Preisdifferenz unter 5% liegt
# Kleinere Werte = konservativer (weniger Risiko)
# Größere Werte = aggressiver (mehr Risiko)
Risikotoleranz = 0.05


# ============================================
# SCHRITT 2: Preisdifferenz berechnen
# ============================================

# Berechne die prozentuale Differenz zwischen Aktienkurs und MA
# Formel: (Aktueller Preis - Moving Average) / Moving Average
#
# Beispiel: (155 - 145) / 145 = 10 / 145 = 0.069 = 6.9%
#
# Warum ist das wichtig?
# - Positive Differenz: Preis ist über dem MA (möglicher Aufwärtstrend)
# - Negative Differenz: Preis ist unter dem MA (möglicher Abwärtstrend)
# - Große Differenz: Vorsicht! Preis könnte überkauft/überverkauft sein
preisdifferenz = (Aktienkurs - MA) / MA


# ============================================
# SCHRITT 3: Trading-Logik / Entscheidungen
# ============================================

# FALL 1: Preis ist ÜBER dem Moving Average
# Dies deutet auf einen Aufwärtstrend hin - potentielles Kauf-Signal
if Aktienkurs > MA:
    print("Price is above the moving average.-Buy signal")

    # Aber Vorsicht! Prüfe ob die Differenz nicht zu groß ist
    # Wenn der Preis zu stark gestiegen ist, könnte eine Korrektur kommen
    if preisdifferenz < Risikotoleranz:
        # Differenz ist klein genug - SICHERES Kauf-Signal
        # Beispiel: 3% Differenz bei 5% Risikotoleranz = OK
        print("Price difference is within risk tolerance.")
        # Hier würde man normalerweise: KAUFEN ausführen

    else:
        # Differenz ist zu groß - RISIKO zu hoch
        # Beispiel: 8% Differenz bei 5% Risikotoleranz = ZU RISKANT
        print("Price difference exceeds risk tolerance.")
        print("Action: HOLD")  # Besser abwarten statt bei Höchststand kaufen


# FALL 2: Preis ist UNTER dem Moving Average
# Dies deutet auf einen Abwärtstrend hin - Verkauf-Signal
elif Aktienkurs < MA:
    print("Sell signal")
    # Hier würde man normalerweise: VERKAUFEN ausführen
    # Begründung: Trend zeigt nach unten, besser Position schließen


# FALL 3: Preis ist GENAU GLEICH dem Moving Average
# Kein klarer Trend erkennbar - abwarten
else:
    print("Price is equal to the moving average.")
    print("Action: HOLD")
    # Kein eindeutiges Signal - lieber nichts tun


# ============================================
# WIE DU DIESEN BOT TESTEN KANNST:
# ============================================
#
# 1. Ändere die Werte oben (Aktienkurs, MA, Risikotoleranz)
# 2. Führe das Skript aus: python Simple_Traiding_Bot.py
# 3. Beobachte welches Signal ausgegeben wird
#
# BEISPIEL-SZENARIEN ZUM TESTEN:
#
# Szenario 1 - Klarer Aufwärtstrend (sollte kaufen):
#   Aktienkurs = 148
#   MA = 145
#   Risikotoleranz = 0.05
#   Ergebnis: Buy signal + within risk tolerance
#
# Szenario 2 - Zu starker Anstieg (sollte halten):
#   Aktienkurs = 160
#   MA = 145
#   Risikotoleranz = 0.05
#   Ergebnis: Buy signal + exceeds risk tolerance → HOLD
#
# Szenario 3 - Abwärtstrend (sollte verkaufen):
#   Aktienkurs = 140
#   MA = 145
#   Risikotoleranz = 0.05
#   Ergebnis: Sell signal
#
# Szenario 4 - Neutral (sollte halten):
#   Aktienkurs = 145
#   MA = 145
#   Risikotoleranz = 0.05
#   Ergebnis: Equal to MA → HOLD


# ============================================
# NÄCHSTE SCHRITTE / VERBESSERUNGEN:
# ============================================
#
# [ ] Input vom Benutzer: input() verwenden statt feste Werte
# [ ] Echte Daten: yfinance API nutzen für Live-Preise
# [ ] MA berechnen: Automatisch aus Preisverlauf berechnen
# [ ] Weitere Indikatoren: RSI, MACD, Bollinger Bands hinzufügen
# [ ] Logging: Entscheidungen in Datei speichern
# [ ] Backtesting: Mit historischen Daten testen
# [ ] Paper Trading: Simulation mit virtuellem Geld
