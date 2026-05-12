from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "data" / "raw"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed"
FINAL_DATA_PATH = BASE_DIR / "data" / "final"

TEAMS = {
    "Brazil": [
        "data/raw/html/brazil.html",
        "data/raw/html/brazil_2025.html"
    ],
    "Morocco": [
        "data/raw/html/morocco.html",
        "data/raw/html/morocco_2025.html"
    ],
    "Haiti": [
        "data/raw/html/haiti.html",
        "data/raw/html/haiti_2025.html"
    ],
    "Scotland": [
        "data/raw/html/scotland.html",
        "data/raw/html/scotland_2025.html"
    ]
}