import pandas as pd
import numpy as np

# --- STEP 1: SETUP (Load & Clean Data) ---
# Use the file path that works for you
df = pd.read_csv(r"C:\Youssef Miled\Python programming\Final Project\Data.csv", low_memory=False)

# Fix the number columns (Cleaning step from Part II)
cols_to_fix = ['BasePay', 'OvertimePay', 'OtherPay', 'Benefits', 'TotalPay']
for col in cols_to_fix:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

print("\n--- PART IV: New Columns & Summary Statistics ---")

# 6. Create computed columns
# Goal: Create a True/False column if the title contains "Manager" or "Chief"

def check_manager(title):
    # We must check if 'title' is a string (str) to avoid errors on empty data
    if not isinstance(title, str):
        return False
    
    # Convert to uppercase so we catch "Manager", "MANAGER", "manager"
    title_upper = title.upper()
    
    # Return True if either keyword is found
    return "MANAGER" in title_upper or "CHIEF" in title_upper

# Apply this function to every single row in 'JobTitle'
df['Is_Manager'] = df['JobTitle'].apply(check_manager)

print(f"Manager/Chief count: {df['Is_Manager'].sum()}")


# 7. Create summary statistics

# a) Average BasePay
avg_basepay = df['BasePay'].mean()
print(f"Average BasePay: ${avg_basepay:,.2f}")

# b) Top 5 most common titles
print("\nTop 5 Job Titles:")
# value_counts() counts how many times each title appears
# head(5) takes just the top 5
print(df['JobTitle'].value_counts().head(5).to_string())
# c) Total number of employees
print(f"\nTotal Number of Employees: {len(df)}")