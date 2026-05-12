import pandas as pd
import matplotlib.pyplot as plt
from config import FINAL_DATA_PATH

# Leer datos
df = pd.read_csv(FINAL_DATA_PATH / "grupo_c_summary.csv")

# =========================
# Power Ranking
# =========================

df_power = df.sort_values("Power_Score", ascending=True)

plt.figure(figsize=(10, 6))
plt.barh(df_power["Team"], df_power["Power_Score"])

plt.title("Grupo C - Power Ranking")
plt.xlabel("Power Score")
plt.ylabel("Selección")

plt.tight_layout()

plt.savefig("reports/figures/power_ranking.png")

# =========================
# Forma reciente
# =========================

df_form = df.sort_values("Points_Form", ascending=True)

plt.figure(figsize=(10, 6))
plt.barh(df_form["Team"], df_form["Points_Form"])

plt.title("Grupo C - Puntos de forma")
plt.xlabel("Puntos")
plt.ylabel("Selección")

plt.tight_layout()

plt.savefig("reports/figures/ranking_forma.png")

# =========================
# Ataque vs Defensa
# =========================

plt.figure(figsize=(9, 6))

plt.scatter(
    df["Goals_For_per_Game"],
    df["Goals_Against_per_Game"]
)

for _, row in df.iterrows():
    plt.text(
        row["Goals_For_per_Game"],
        row["Goals_Against_per_Game"],
        row["Team"]
    )

plt.title("Grupo C - Ataque vs Defensa")

plt.xlabel("Goles a favor por partido")
plt.ylabel("Goles en contra por partido")

plt.tight_layout()

plt.savefig("reports/figures/ataque_defensa.png")

# =========================
# Diferencia de gol
# =========================

df_gd = df.sort_values("Goal_Difference", ascending=True)

plt.figure(figsize=(10, 6))

plt.barh(
    df_gd["Team"],
    df_gd["Goal_Difference"]
)

plt.title("Grupo C - Diferencia de gol")

plt.xlabel("Diferencia de gol")
plt.ylabel("Selección")

plt.tight_layout()

plt.savefig("reports/figures/goal_difference.png")

print("Gráficos generados correctamente")