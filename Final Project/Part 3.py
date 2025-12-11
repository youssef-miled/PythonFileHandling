import pandas as pd
import numpy as np

# --- STEP 1: SETUP (Copy this to every new file!) ---
# 1. Load the data (Use the path that worked for you!)
# Note: If your file is in the same folder, just use "Data.csv". 
# If not, paste your full path like: r"C:\Users\...\Data.csv"
df = pd.read_csv(r"C:\Youssef Miled\Python programming\Final Project\Data.csv", low_memory=False)


print("--- PART III: Subsetting & Filtering ---")

# --- STEP 2: YOUR PART III TASKS ---

# a) High earners (> $200,000)
high_earners = df[df['TotalPay'] > 200000]
print(f"a) High Earners: {len(high_earners)}")

# b) Employees from year 2013
employees_2013 = df[df['Year'] == 2013]
print(f"b) Employees in 2013: {len(employees_2013)}")

# c) JobTitle contains "POLICE"
# This finds "Police", "POLICE", "police" etc.
police_df = df[df['JobTitle'].str.contains("POLICE", case=False, na=False)]
print(f"c) Police related jobs: {len(police_df)}")