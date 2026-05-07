import pandas as pd

path = "data/raw/html/mexico.html"

tables = pd.read_html(path)

print(f"Tablas encontradas: {len(tables)}")

for i, table in enumerate(tables):
    print("\n========================")
    print(f"TABLA {i}")
    print("========================")
    print(table.head())
    print("Columnas:")
    print(table.columns)