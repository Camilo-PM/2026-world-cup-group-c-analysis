import pandas as pd
from config import FINAL_DATA_PATH


def generate_report():
    df = pd.read_csv(FINAL_DATA_PATH + "grupo_a_summary.csv")

    top_team = df.iloc[0]
    worst_team = df.iloc[-1]

    report = f"""
# World Cup 2026 - Group A Analysis

## Overview
This report analyzes the recent performance (last 10 matches) of Group A teams.

## Power Ranking
1. {df.iloc[0]['Team']}
2. {df.iloc[1]['Team']}
3. {df.iloc[2]['Team']}
4. {df.iloc[3]['Team']}

## Key Insights

### 🥇 Best Team (Recent Form)
{top_team['Team']} leads the group with:
- {top_team['Points_Form']} points out of 30
- Goal Difference: {top_team['Goal_Difference']}
- Win Rate: {round(top_team['Win_Rate'] * 100, 1)}%

### ⚠️ Team to Improve
{worst_team['Team']} shows weaker recent performance:
- Only {worst_team['Points_Form']} points
- Goal Difference: {worst_team['Goal_Difference']}

### ⚔️ Offensive vs Defensive Balance
- Best Attack: {df.loc[df['Goals_For'].idxmax()]['Team']}
- Best Defense: {df.loc[df['Goals_Against'].idxmin()]['Team']}

## Visual Analysis

### Power Ranking
![Power Ranking](reports/figures/power_ranking.png)

### Form Ranking
![Form Ranking](reports/figures/ranking_forma.png)

### Attack vs Defense
![Attack vs Defense](reports/figures/ataque_defensa.png)

### Goal Difference
![Goal Difference](reports/figures/goal_difference.png)
"""

    with open("reports/resumen_grupo_a.md", "w", encoding="utf-8") as f:
        f.write(report)

    print("✅ Reporte generado en reports/resumen_grupo_a.md")


if __name__ == "__main__":
    generate_report()