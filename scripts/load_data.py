
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

csv_file = Path(
    r"C:\Users\Administrator\Downloads\GrocerySales10MDataset\transactions_2M.csv"
)

# Replace YOUR_PASSWORD with your PostgreSQL password
engine = create_engine(
    "postgresql+psycopg://postgres:121221@localhost:5432/retail_etl_v2"
)
try:
    print("Reading CSV file...")
    df = pd.read_csv(csv_file)
    print("Records read:", len(df))

    # Transform and clean the data
    df.columns = df.columns.str.strip()

    df["timestamp"] = pd.to_datetime(
        df["timestamp"], errors="coerce"
    )

    for col in [
        "transaction_id", "user_id", "product_id",
        "quantity", "price"
    ]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=[
        "transaction_id", "user_id", "product_id",
        "category", "quantity", "price", "timestamp", "region"
    ])

    df = df.drop_duplicates(subset=["transaction_id"])

    df = df[
        (df["quantity"] > 0) &
        (df["price"] >= 0)
    ].copy()

    for col in [
        "transaction_id", "user_id", "product_id", "quantity"
    ]:
        df[col] = df[col].astype("int64")

    print("Records after cleaning:", len(df))
    print("Loading data into PostgreSQL...")

    df.to_sql(
        "transactions",
        engine,
        schema="public",
        if_exists="append",
        index=False,
        chunksize=1000
    )

    print("Loading completed successfully!")
    print("Records loaded:", len(df))

finally:
    engine.dispose()
