## Check via Command Prompt or PowerShell if SQLite is installed on your Windows system 

This is the most direct way to verify if the SQLite command-line tool is installed and configured in your system's PATH. 

1. Press `Win + R`, type `cmd` (or `powershell`), and press Enter.
2. Type the following command and press Enter:  
   ```
   cmd
   

   sqlite3 --version
   ```

3. Results:
   1. Installed: You will see a version number and date (e.g., 3.51.1 2025-xx-xx ...).
   2. Not Installed: You will see an error message stating that 'sqlite3' is not recognized as an internal or external command. 

## Enter the SQLite Shell 
Alternatively, you can try to launch the interactive shell directly. 

1. In the Command Prompt, type:
   ```
   cmd

   sqlite3
   ```
2. Results:
   1. If installed, you will see a message beginning with SQLite version 3.x.x followed by a sqlite> prompt.
   2. To exit this shell, type .quit and press Enter. 

## Check for Python's Built-in Library 

If you are a developer, note that Python comes with a built-in SQLite library, even if the command-line tool itself is not installed. To check this: 

1. Open Command Prompt and type python to enter the Python shell.
2. Run the following code:
   ```
   python
   import sqlite3
   print(sqlite3.sqlite_version)
   ```
3. This will display the version of the SQLite library used by your Python installation. 

## Using Python’s SQLite shell (always shows prompt)
If prompt visibility is critical:
```
python -m sqlite3
```
You will get:
```
sqlite>
```

Best practice recommendation (for your workflow):
```
python -m sqlite3 mydata.db
```

## How to list tables in a database

```
SELECT name FROM sqlite_master WHERE type='table';
```

```
sqlite> SELECT name FROM sqlite_master WHERE type='table';
('_S_h_e_e_t_1_',)
('Sheet1',)
('tbl_sheet1',)
```

Quering the entire table:
```
sqlite> SELECT * FROM "tbl_sheet1";
```

Querying the "WINNER" column from the "tbl_sheet1" table:
```
sqlite> SELECT "WINNER" FROM "tbl_sheet1";
```

Querying multiple columns from a table:
```
sqlite> SELECT "WINNER", "NOVEL" FROM "tbl_sheet1";
```