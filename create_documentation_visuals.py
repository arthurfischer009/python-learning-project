"""
Script to create visualizations and screenshots for documentation
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Set style
plt.style.use('seaborn-v0_8-darkgrid')

# Create output directory
import os
os.makedirs('docs/images', exist_ok=True)

# ============================================
# 1. Trading Bot - Moving Average Visualization
# ============================================

fig, ax = plt.subplots(figsize=(12, 6))

# Simulate price data
days = np.arange(0, 50)
price = 140 + np.sin(days / 5) * 10 + days * 0.3
ma = np.convolve(price, np.ones(20)/20, mode='same')

# Plot
ax.plot(days, price, label='Aktienkurs', linewidth=2, color='#2E86AB')
ax.plot(days, ma, label='Moving Average (MA)', linewidth=2, color='#A23B72', linestyle='--')

# Highlight buy/sell zones
buy_zone = (price > ma) & (((price - ma) / ma) < 0.05)
sell_zone = price < ma

ax.fill_between(days, 120, 180, where=buy_zone, alpha=0.2, color='green', label='BUY Zone')
ax.fill_between(days, 120, 180, where=sell_zone, alpha=0.2, color='red', label='SELL Zone')

# Add annotations
ax.annotate('BUY Signal', xy=(25, 150), xytext=(25, 165),
            arrowprops=dict(arrowstyle='->', color='green', lw=2),
            fontsize=12, fontweight='bold', color='green')

ax.annotate('SELL Signal', xy=(15, 143), xytext=(15, 130),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=12, fontweight='bold', color='red')

ax.set_xlabel('Tage', fontsize=12)
ax.set_ylabel('Preis ($)', fontsize=12)
ax.set_title('Trading Bot - Moving Average Strategie', fontsize=16, fontweight='bold')
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_ylim(120, 180)

plt.tight_layout()
plt.savefig('docs/images/trading_bot_strategy.png', dpi=300, bbox_inches='tight')
print("✓ Created: trading_bot_strategy.png")
plt.close()

# ============================================
# 2. Portfolio Allocation - Pie Chart
# ============================================

fig, ax = plt.subplots(figsize=(10, 8))

# Example allocation
stocks = ['Stock A\n(Tech)', 'Stock B\n(Finance)', 'Stock C\n(Healthcare)']
allocation = [50, 30, 20]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
explode = (0.1, 0, 0)  # Explode Stock A

wedges, texts, autotexts = ax.pie(allocation,
                                    labels=stocks,
                                    autopct='%1.1f%%',
                                    startangle=90,
                                    colors=colors,
                                    explode=explode,
                                    shadow=True)

# Style the text
for text in texts:
    text.set_fontsize(14)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(14)
    autotext.set_fontweight('bold')

ax.set_title('Portfolio Allocation Beispiel\nTotal: $10,000',
             fontsize=16, fontweight='bold', pad=20)

# Add legend with values
legend_labels = [f'{stock}: ${allocation[i]*100:,.0f}'
                 for i, stock in enumerate(['Stock A', 'Stock B', 'Stock C'])]
ax.legend(legend_labels, loc='upper left', bbox_to_anchor=(1, 0, 0.5, 1), fontsize=11)

plt.tight_layout()
plt.savefig('docs/images/portfolio_allocation.png', dpi=300, bbox_inches='tight')
print("✓ Created: portfolio_allocation.png")
plt.close()

# ============================================
# 3. Risk Tolerance Visualization
# ============================================

fig, ax = plt.subplots(figsize=(12, 6))

# Risk levels
risk_tolerance = [0.02, 0.05, 0.10, 0.20]
risk_labels = ['Sehr\nKonservativ\n(2%)', 'Konservativ\n(5%)', 'Moderat\n(10%)', 'Aggressiv\n(20%)']
colors_risk = ['#2ECC71', '#F39C12', '#E67E22', '#E74C3C']

bars = ax.barh(risk_labels, risk_tolerance, color=colors_risk, alpha=0.7, edgecolor='black', linewidth=2)

# Add value labels
for i, (bar, val) in enumerate(zip(bars, risk_tolerance)):
    ax.text(val + 0.005, i, f'{val*100:.0f}%',
            va='center', fontsize=12, fontweight='bold')

ax.set_xlabel('Risikotoleranz (%)', fontsize=12, fontweight='bold')
ax.set_title('Risikotoleranz-Profile für Trading', fontsize=16, fontweight='bold')
ax.set_xlim(0, 0.25)
ax.grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.savefig('docs/images/risk_tolerance.png', dpi=300, bbox_inches='tight')
print("✓ Created: risk_tolerance.png")
plt.close()

# ============================================
# 4. Project Architecture Diagram
# ============================================

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9.5, 'Python Learning & Finance Projects',
        ha='center', fontsize=20, fontweight='bold')
ax.text(5, 9, 'Projekt-Architektur',
        ha='center', fontsize=14, style='italic')

# Projects
projects = [
    {'name': 'Trading Bots', 'x': 1.5, 'y': 7, 'color': '#FF6B6B', 'tech': 'Python\npandas\nnumpy'},
    {'name': 'Solana Portfolio', 'x': 5, 'y': 7, 'color': '#4ECDC4', 'tech': 'Streamlit\nSelenium\nPlotly'},
    {'name': 'AFAR Indicators', 'x': 8.5, 'y': 7, 'color': '#45B7D1', 'tech': 'Pine Script\nTradingView'},
    {'name': 'Portfolio Tools', 'x': 3.25, 'y': 4, 'color': '#95E1D3', 'tech': 'Python\nMath'}
]

for proj in projects:
    # Box
    rect = patches.FancyBboxPatch(
        (proj['x']-0.8, proj['y']-0.6), 1.6, 1.8,
        boxstyle="round,pad=0.1",
        linewidth=3,
        edgecolor=proj['color'],
        facecolor=proj['color'],
        alpha=0.3
    )
    ax.add_patch(rect)

    # Title
    ax.text(proj['x'], proj['y']+0.8, proj['name'],
            ha='center', va='center', fontsize=12, fontweight='bold')

    # Tech stack
    ax.text(proj['x'], proj['y'], proj['tech'],
            ha='center', va='center', fontsize=9, style='italic')

# Skills bar at bottom
skills_box = patches.FancyBboxPatch(
    (1, 1), 8, 1.5,
    boxstyle="round,pad=0.1",
    linewidth=2,
    edgecolor='#333',
    facecolor='#F8F9FA',
    alpha=0.8
)
ax.add_patch(skills_box)

skills_text = '''Skills: Python • Data Science • Web Development • Automation
Trading • Blockchain • Portfolio Management • Clean Code'''

ax.text(5, 1.75, skills_text,
        ha='center', va='center', fontsize=11, fontweight='bold')

# Arrows connecting to skills
for proj in projects:
    ax.annotate('', xy=(5, 2.5), xytext=(proj['x'], proj['y']-0.6),
                arrowprops=dict(arrowstyle='->', lw=1.5, alpha=0.4, color='gray'))

plt.tight_layout()
plt.savefig('docs/images/project_architecture.png', dpi=300, bbox_inches='tight')
print("✓ Created: project_architecture.png")
plt.close()

# ============================================
# 5. Learning Path Visualization
# ============================================

fig, ax = plt.subplots(figsize=(12, 8))

# Learning stages
stages = ['Beginner', 'Intermediate', 'Advanced', 'Expert']
y_positions = [7, 5, 3, 1]
colors_stage = ['#95E1D3', '#4ECDC4', '#45B7D1', '#2E86AB']

projects_learning = [
    ('Portfolio Allocation', 0),
    ('Trading Bot\n(Simple MA)', 1),
    ('Solana Tracker\n(Web Scraping)', 2),
    ('AFAR Indicators\n(Pine Script)', 2),
]

# Draw stages
for i, (stage, y) in enumerate(zip(stages, y_positions)):
    circle = patches.Circle((2, y), 0.5, color=colors_stage[i], alpha=0.7, linewidth=3, edgecolor='black')
    ax.add_patch(circle)
    ax.text(2, y, stage, ha='center', va='center', fontsize=12, fontweight='bold')

    # Connecting line
    if i < len(stages) - 1:
        ax.plot([2, 2], [y-0.5, y_positions[i+1]+0.5], 'k--', linewidth=2, alpha=0.5)

# Add projects
for proj_name, stage_idx in projects_learning:
    y = y_positions[stage_idx]
    x_offset = 5 + (projects_learning.index((proj_name, stage_idx)) % 2) * 2

    # Arrow from stage to project
    ax.annotate('', xy=(x_offset, y), xytext=(2.5, y),
                arrowprops=dict(arrowstyle='->', lw=2, color=colors_stage[stage_idx]))

    # Project box
    rect = patches.FancyBboxPatch(
        (x_offset-0.7, y-0.3), 1.4, 0.6,
        boxstyle="round,pad=0.05",
        linewidth=2,
        edgecolor=colors_stage[stage_idx],
        facecolor='white',
        alpha=0.9
    )
    ax.add_patch(rect)
    ax.text(x_offset, y, proj_name, ha='center', va='center', fontsize=9, fontweight='bold')

ax.set_xlim(0, 10)
ax.set_ylim(0, 9)
ax.set_title('Learning Path: Python für Finance', fontsize=16, fontweight='bold', pad=20)
ax.axis('off')

plt.tight_layout()
plt.savefig('docs/images/learning_path.png', dpi=300, bbox_inches='tight')
print("✓ Created: learning_path.png")
plt.close()

print("\n✅ All documentation visuals created successfully!")
print("📁 Location: docs/images/")
