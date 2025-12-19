import pandas as pd
from sqlalchemy import create_engine
import re
import os

# -----------------------------
# Configuration
# -----------------------------
CSV_FOLDER = "csv"              # Folder containing CSV files
DB_FILE = "database.db"         # Output SQLite DB

engine = create_engine(f"sqlite:///{DB_FILE}")

# -----------------------------
# Clean table name function
# -----------------------------
def clean_table_name(name):
    name = re.sub(r'\W+', '_', name)
    #return f"tbl_{name.strip('_').lower()}"
    return f"{name.strip('_').lower()}"

# -----------------------------
# Process CSV files
# -----------------------------
for file in os.listdir(CSV_FOLDER):
    if not file.lower().endswith(".csv"):
        continue

    csv_path = os.path.join(CSV_FOLDER, file)
    table_name = clean_table_name(os.path.splitext(file)[0])

    df = pd.read_csv(csv_path)

    # 🔴 Skip empty CSVs
    if df.empty or len(df.columns) == 0:
        print(f"⚠ Skipping empty CSV: {file}")
        continue

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"✅ Imported CSV: {file} → table: {table_name}")

print("🎯 CSV to SQLite conversion completed successfully")
