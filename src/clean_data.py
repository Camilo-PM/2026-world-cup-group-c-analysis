import pandas as pd
import os
from config import RAW_DATA_PATH, PROCESSED_DATA_PATH


def clean_all_files():
    all_data = []

    print("Buscando archivos en:", RAW_DATA_PATH)

    for file in os.listdir(RAW_DATA_PATH):
        if file.endswith(".csv"):
            print("Procesando:", file)

            df = pd.read_csv(RAW_DATA_PATH + file)

            # 🔥 FILTRO CLAVE: eliminar partidos sin resultado real
            df = df[df["GF"].notna() & df["GA"].notna()]

            # Asegurar tipo numérico
            df["GF"] = pd.to_numeric(df["GF"], errors="coerce")
            df["GA"] = pd.to_numeric(df["GA"], errors="coerce")

            # Volver a filtrar por si hubo errores
            df = df.dropna(subset=["GF", "GA"])

            # Calcular métricas
            df["Goal_Difference"] = df["GF"] - df["GA"]

            df["Result_Clean"] = df["Goal_Difference"].apply(
                lambda x: "Win" if x > 0 else "Draw" if x == 0 else "Loss"
            )

            all_data.append(df)

    if not all_data:
        print("⚠️ No se encontraron archivos CSV")
        return

    final_df = pd.concat(all_data, ignore_index=True)

    output_path = PROCESSED_DATA_PATH + "grupo_b_last_10_clean.csv"
    final_df.to_csv(output_path, index=False)

    print("✅ Archivo creado en:", output_path)


if __name__ == "__main__":
    clean_all_files()