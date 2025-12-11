import pandas as pd
import numpy as np

# --- STEP 1: SETUP (Load & Clean) ---
# Use the file path that works for you
df = pd.read_csv(r"C:\Youssef Miled\Python programming\Final Project\Data.csv", low_memory=False)


print("\n--- PART V: Grouping & Aggregation ---")

# 8. Perform an analysis using group-based aggregation
# Goal: Calculate the Average TotalPay for each Year

print("Average TotalPay by Year:")

# 1. Group by 'Year'
# 2. Select 'TotalPay'
# 3. Calculate the Mean (Average)
avg_pay_by_year = df.groupby('Year')['TotalPay'].mean()

# Print the result nicely (formatted as currency)
# We loop through the items to print them cleanly without the "dtype" message
for year, pay in avg_pay_by_year.items():
    print(f"Year {year}: ${pay:,.2f}")

# (Optional) Find the year with the highest average
highest_year = avg_pay_by_year.idxmax()
print(f"\n-> The year with the highest average pay was: {highest_year}")