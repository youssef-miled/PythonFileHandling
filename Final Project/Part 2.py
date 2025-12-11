import pandas as pd
import numpy as np

print("\n--- PART II: Data Cleaning (Pandas) ---")

# 1. Load the dataset
df = pd.read_csv(r"C:\Youssef Miled\Python programming\Final Project\Data.csv", low_memory=False)

# --- FIX: Convert salary columns to numbers ---
# We do this immediately after loading to fix the "DtypeWarning"
cols_to_fix = ['BasePay', 'OvertimePay', 'OtherPay', 'Benefits', 'TotalPay']
for col in cols_to_fix:
    if col in df.columns:
        # errors='coerce' turns text into NaN, then we fill with 0
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

# 2. Remove duplicates
before_dedup = len(df)
df.drop_duplicates(inplace=True)
print(f"Rows removed (Duplicates): {before_dedup - len(df)}")

print("-> Data cleaned and salary columns fixed.")