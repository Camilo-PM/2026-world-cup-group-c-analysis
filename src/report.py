import pandas as pd
from config import FINAL_DATA_PATH


def generate_report():

    df = pd.read_csv(FINAL_DATA_PATH + "grupo_b_summary.csv")

    report = f"""
# Group B - FIFA World Cup 2026 Analysis

## Team Rankings

{df[['Team', 'Power_Score']].to_string(index=False)}

## Key Insights

- Switzerland appears as the strongest team in the group.
- Bosnia and Herzegovina shows strong offensive consistency.
- Canada remains competitive but draws too many matches.
- Qatar presents the weakest overall metrics.

## Predicted Standings

1. Switzerland
2. Bosnia and Herzegovina
3. Canada
4. Qatar
"""

    with open("reports/resumen_grupo_b.md", "w", encoding="utf-8") as f:
        f.write(report)

    print("✅ Reporte generado en reports/resumen_grupo_b.md")


if __name__ == "__main__":
    generate_report()