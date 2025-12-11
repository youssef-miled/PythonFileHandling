import pandas as pd
import sys

# --- SETUP: Load the Data ---
# We use the ORIGINAL Data.csv for the investigation

try:
    df = pd.read_csv(r"C:\Youssef Miled\Python programming\Final Project\Data.csv", low_memory=False)
    
    # Quick cleaning (essential for math)
    cols_to_fix = ['BasePay', 'TotalPay']
    for col in cols_to_fix:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
            
except FileNotFoundError:
    print("Error: Could not find Data.csv. Please check the path.")
    sys.exit()

# --- PART VII: Interactive Investigation Script ---
print("\n=== EMPLOYEE INVESTIGATION TOOL ===")

while True:
    # 10. Ask user for job title keyword
    keyword = input("Enter a job title to search for (e.g. 'Police'): ").strip()
    
    # Stop if user types 'exit'
    if keyword.lower() == 'exit':
        print("Goodbye!")
        break
        
    # Filter rows (Case insensitive search)
    # This finds everyone whose job title contains your keyword
    result = df[df['JobTitle'].str.contains(keyword, case=False, na=False)]
    
    if result.empty:
        print(f"-> No jobs found matching '{keyword}'. Try again.\n")
        continue
        
    # Calculate stats
    count = len(result)
    avg_base = result['BasePay'].mean()
    highest_total = result['TotalPay'].max()
    
    # Show Results
    print(f"\n--- REPORT FOR '{keyword.upper()}' ---")
    print(f"• Number of Employees found: {count}")
    print(f"• Average BasePay:           ${avg_base:,.2f}")
    print(f"• Highest TotalPay:          ${highest_total:,.2f}")
    
    # Save results to a file
    output_filename = "custom_search.csv"
    result.to_csv(output_filename, index=False)
    print(f"-> detailed results saved to '{output_filename}'\n")
    print(f"Type'exit' to stop")