
A Python script that cleans and organizes CSV files quickly and efficiently.  
Built using **pandas** for data processing.

## Features
- Remove empty rows
- Strip spaces from column names
- Trim spaces from string values
- Fill missing values (optional)
- Sort rows by a column of your choice
- Save the cleaned CSV

## Requirements
- Python 3.x
- pandas (`pip install pandas`)

## How It Works
1. Load your CSV file into a pandas DataFrame.
2. Remove rows where all values are empty.
3. Clean column names and string values.
4. Fill missing values if configured.
5. Sort the DataFrame by a specified column.
6. Save the cleaned CSV file.

## Usage
1. Place your CSV file in the same folder as `csv_cleaner.py`.
2. Update the script with your configuration:
```python
input_file = "input.csv"
output_file = "cleaned.csv"
sort_column = "Name"
fill_missing = ""

3. Run the script:



python csv_cleaner.py

4. The cleaned CSV will be saved as cleaned.csv.


