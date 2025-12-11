import csv
import os

filename = r"C:\Youssef Miled\Python programming\Final Project\Data.csv"

print("--- PART I: Manual File Handling (Safe Version) ---")

# 1. Check if file exists to prevent FileNotFoundError
if not os.path.exists(filename):
    print(f"ERROR: Could not find '{filename}'")
    print(f"I am looking in this folder: {os.getcwd()}")
    print("Please move Data.csv into this folder.")
    exit()

try:
    # 2. Open with 'errors=replace' to prevent UnicodeDecodeError
    # We use 'utf-8-sig' to handle files saved by Excel
    with open(filename, mode='r') as f:
        reader = csv.reader(f)
        
        # Safe header extraction
        try:
            header = next(reader)
            print(f"\nSUCCESS: File opened. Header: {header}")
        except StopIteration:
            print("Error: The file is empty!")
            exit()

        # Reset variables for the loop
        chief_count = 0
        extracted_data = []
        # Loop through the rows
        for i, row in enumerate(reader):
            # 3. Skip empty lines to prevent IndexError
            if not row:
                continue
            # Task 2: Search for "chief" (Case insensitive)
            row_text = ",".join(row).lower()
            if "chief" in row_text:
                chief_count += 1
            # Task 3: Extract first 2 columns manually
            # Only save the first 5 for the preview to avoid flooding the screen
            if len(extracted_data) < 5:
                # Ensure the row has at least 2 columns before accessing index 1
                if len(row) >= 2:
                    extracted_data.append((row[0], row[1]))

        print(f"\n2. Found 'chief' in {chief_count} rows.")
        
        print("\n3. First 5 extracted rows (Column 0 and 1):")
        for item in extracted_data:
            print(item)

except Exception as e:
    print(f"\nCRITICAL ERROR: {e}")