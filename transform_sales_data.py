import pandas as pd
from pathlib import Path

# Define file paths
raw_path = Path("data/raw/sales_data_2025_01.csv")
clean_path = Path("data/clean/sales_data_cleaned.csv")

# Read raw CSV
df = pd.read_csv(raw_path)

# Basic cleaning
df['order_date'] = pd.to_datetime(df['order_date'])
df['total_amount'] = df['quantity'] * df['unit_price']

# Remove invalid or missing values
df = df.dropna(subset=['customer', 'region', 'product'])

# Add derived columns
df['month'] = df['order_date'].dt.to_period('M')

# Save cleaned file
Path("data/clean").mkdir(parents=True, exist_ok=True)
df.to_csv(clean_path, index=False)

print("✅ Cleaned data saved:", clean_path)
