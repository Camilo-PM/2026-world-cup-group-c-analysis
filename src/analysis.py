import pandas as pd
from config import PROCESSED_DATA_PATH, FINAL_DATA_PATH


def analyze_group():

    df = pd.read_csv(PROCESSED_DATA_PATH + "grupo_b_last_10_clean.csv")

    summary = df.groupby("Team").agg(
        Matches=("Team", "count"),
        Wins=("Result_Clean", lambda x: (x == "Win").sum()),
        Draws=("Result_Clean", lambda x: (x == "Draw").sum()),
        Losses=("Result_Clean", lambda x: (x == "Loss").sum()),
        Goals_For=("GF", "sum"),
        Goals_Against=("GA", "sum"),
        Goal_Difference=("Goal_Difference", "sum"),
        Avg_Goals_For=("GF", "mean"),
        Avg_Goals_Against=("GA", "mean"),
    ).reset_index()

    summary["Points_Form"] = summary["Wins"] * 3 + summary["Draws"]

    summary["Win_Rate"] = summary["Wins"] / summary["Matches"]

    summary["Goals_For_per_Game"] = (
        summary["Goals_For"] / summary["Matches"]
    )

    summary["Goals_Against_per_Game"] = (
        summary["Goals_Against"] / summary["Matches"]
    )

    # Índices tipo scouting
    summary["Attack_Index"] = summary["Goals_For_per_Game"]

    summary["Defense_Index"] = (
        1 / summary["Goals_Against_per_Game"]
    )

    summary["Form_Index"] = summary["Points_Form"] / 30

    # Score final
    summary["Power_Score"] = (
        summary["Form_Index"] * 0.45
        + summary["Win_Rate"] * 0.30
        + summary["Goals_For_per_Game"] * 0.15
        + summary["Defense_Index"] * 0.10
    )

    summary = summary.sort_values(
        by=["Power_Score", "Points_Form", "Goal_Difference"],
        ascending=False
    )

    # CSV principal
    output_path = FINAL_DATA_PATH + "grupo_b_summary.csv"

    summary.to_csv(output_path, index=False)

    # CSV Tableau
    tableau_path = FINAL_DATA_PATH + "grupo_b_summary_tableau.csv"

    summary.to_csv(
        tableau_path,
        index=False,
        sep=";",
        encoding="utf-8-sig"
    )

    print(summary)

    print("✅ Archivo creado en:", output_path)

    print("✅ Archivo para Tableau creado en:", tableau_path)


if __name__ == "__main__":
    analyze_group()