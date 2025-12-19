# Excel (.xlsx) file to a database (.db) file conversion

You can convert an Excel (.xlsx) file into a database (.db) file (SQLite) so it can be used directly with SQL.

Below are practical, reliable methods. The Python method is the most flexible and recommended.

## ✅ Method 1: Python (Recommended – clean & automated)

This converts each Excel sheet into a SQL table inside a .db file.

### 🔹 Prerequisites
Install required libraries:

`pip install pandas openpyxl sqlalchemy`

### 🔹 Python Script: .xlsx → .db

```
import pandas as pd
from sqlalchemy import create_engine
import re

excel_file = "booker_prize_dataset.xlsx"
db_file = "booker_prize_dataset.db"

engine = create_engine(f"sqlite:///{db_file}")

xls = pd.ExcelFile(excel_file)

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
```

### 🔹Script Explanation

In Python regex:

| Pattern | Matches |
| :-----: | :------ |
|`\w`     | letters (a-z, A-Z), digits (0-9), underscore `_`|
|`\W`       |everything else (space, dash, brackets, dots, etc.)|

Role of `name.strip('_')`:

Removes underscores from start and end of the string.
Does not remove underscores in the middle.

## ✅ Method 2: Excel → CSV → SQLite (Manual but Simple)
### Step 1: Save Excel as CSV
In Excel:

```
mathematica

File → Save As → CSV (Comma delimited)
```

### Step 2: Import into SQLite

```
bash

sqlite3 output.db
```

```
sql

.mode csv
.import data.csv table_name
```