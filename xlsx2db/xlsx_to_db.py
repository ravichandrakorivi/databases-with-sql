import pandas as pd
from sqlalchemy import create_engine
import re

excel_file = "booker_prize_dataset.xlsx"
db_file = "booker_prize_dataset.db"

engine = create_engine(f"sqlite:///{db_file}")

xls = pd.ExcelFile(excel_file)

"""
def clean_table_name(name):
    '''
    This function converts any Excel sheet name into a safe SQL table name. SQL table names cannot contain spaces or special characters. Excel sheet names often contain spaces, dashes, brackets, etc. SQLite (and most SQL engines) work best with: letters + numbers + underscore.
    
    :name: The original sheet name (string)
    '''
    # Keep only letters, numbers, underscore
    # replace using regular expression
    # r'\W+' → one or more non-word characters
    # '_' → replace them with underscore

    name = re.sub(r'\W+', '_', name)

    # Removes underscores from start and end of the string.
    # Does not remove underscores in the middle.
    return name.strip('_')
"""

# cleaner, uniform names
def clean_table_name(name):
    name = re.sub(r'\W+', '_', name)
    return f"tbl_{name.strip('_').lower()}"


for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name)

    # 🔴 Skip empty sheets
    if df.empty or len(df.columns) == 0:
        print(f"⚠ Skipping empty sheet: {sheet_name}")
        continue

    table_name = clean_table_name(sheet_name)

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"✅ Imported sheet: {sheet_name} → table: {table_name}")

print("🎯 Excel to SQLite conversion completed successfully")