import pandas as pd
import time
from config import TEAMS, RAW_DATA_PATH


def get_fixtures_table(local_html_path):
    tables = pd.read_html(local_html_path)

    for table in tables:
        columns = [str(col).lower() for col in table.columns]

        if (
            "date" in columns
            and "gf" in columns
            and "ga" in columns
            and "opponent" in columns
        ):
            return table

    raise ValueError(f"No se encontró tabla de partidos en {local_html_path}")


def collect_last_10_matches():
    for team, html_paths in TEAMS.items():
        print(f"Leyendo datos de {team}...")

        team_data = []

        for html_path in html_paths:
            print(f"  Leyendo archivo: {html_path}")

            df = get_fixtures_table(html_path)
            df["Team"] = team

            df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
            df["GF"] = pd.to_numeric(df["GF"], errors="coerce")
            df["GA"] = pd.to_numeric(df["GA"], errors="coerce")

            df = df.dropna(subset=["Date", "GF", "GA"])

            team_data.append(df)

        combined_df = pd.concat(team_data, ignore_index=True)

        combined_df = combined_df.sort_values("Date", ascending=False)

        last_10 = combined_df.head(10)

        filename = team.lower().replace(" ", "_") + "_last_10.csv"
        last_10.to_csv(RAW_DATA_PATH + filename, index=False)

        print(f"Guardado: {filename} | Partidos guardados: {len(last_10)}")

        time.sleep(1)

    print("Datos guardados correctamente.")


if __name__ == "__main__":
    collect_last_10_matches()