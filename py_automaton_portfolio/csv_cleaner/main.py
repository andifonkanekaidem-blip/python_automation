import pandas as pd


# CONFIG

input_file = "input.csv"        # CSV file to clean
output_file = "cleaned.csv"     # Output CSV file
sort_column = "Name"            # Column to sort by
fill_missing = ""               # Value to fill missing cells, leave "" if no filling


# Load the CSV file

try:
    df = pd.read_csv(input_file)
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
    exit()


# Clean the dataframe

# Remove rows where all values are empty
df.dropna(how="all", inplace=True)

# Strip spaces from column names
df.columns = df.columns.str.strip()

# Fill missing values
if fill_missing != "":
    df.fillna(fill_missing, inplace=True)

# Strip spaces from string columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()


# Sort data based on column

if sort_column in df.columns:
    df.sort_values(by=sort_column, inplace=True)
else:
    print(f"Warning: Column '{sort_column}' not found. Skipping sort.")

#Save
df.to_csv(output_file, index=False)
print(f"CSV cleaned and saved as '{output_file}'")
"""This script can be adjusted to clean excel files by changing 'df.read_csv()' to 'df.read_excel()'"""