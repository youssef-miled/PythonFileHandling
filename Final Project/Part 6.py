import pandas as pd
import os

# --- STEP 1: SETUP ---
# Load the main data
df = pd.read_csv(r"C:\Youssef Miled\Python programming\Final Project\Data.csv", low_memory=False)

print("\n--- PART VI: Joining ---")

# 9. Merge with agency_codes.csv
# usage of 'r' before the quote is crucial for Windows paths!
agency_file = r"C:\Youssef Miled\Python programming\Final Project\agency_codes.csv"
# Check if the file exists now
if not os.path.exists(agency_file):
    print(f"ERROR: '{agency_file}' is missing! Did you run the creation script?")
else:
    # A. Load the agency codes
    agency_df = pd.read_csv(agency_file)
    print("Loaded agency_codes.csv...")

    # ... (Keep your merge code the same) ...

    # B. Merge
    merged_df = pd.merge(df, agency_df, on='Agency', how='left')

    # --- SAVE OPTION 1: The Requirement (CSV) ---
    # We save this for the assignment. 
    # If this looks messy in Excel, ignore it—it is technically correct for the code.
    csv_filename = "merged_data.csv"
    merged_df.to_csv(csv_filename, index=False)
    print(f"SUCCESS: Saved assignment file: {csv_filename}")

    # --- SAVE OPTION 2: The Viewable File (Excel) ---
    # Open THIS file to see the columns perfectly separated.
    excel_filename = "merged_data_VIEW_ME.xlsx"
    try:
        merged_df.to_excel(excel_filename, index=False)
        print(f"SUCCESS: Saved clear Excel file: {excel_filename}")
        print("-> Open 'merged_data_VIEW_ME.xlsx' to see the separated columns!")
    except ImportError:
        print("NOTE: Could not save .xlsx. Run 'pip install openpyxl' to fix.")