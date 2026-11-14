
import pandas as pd
from pathlib import Path

input_file = Path(
    r"C:\Users\Administrator\Downloads\GrocerySales10MDataset\GrocerySales10MDataset\GrocerySales10MDataset\GrocerySales10MDataset\transactions_10M.csv"
)

output_file = Path(
    r"C:\Users\Administrator\Downloads\GrocerySales10MDataset\transactions_2M.csv"
)

if not input_file.exists():
    print("ERROR: CSV file not found!")
    print("Check the input file path.")
else:
    print("Reading the first 2 million records...")

    df = pd.read_csv(input_file, nrows=2_000_000)

    print("Records selected:", len(df))

    df.to_csv(output_file, index=False)

    print("File saved successfully!")
    print("Output file:", output_file)
