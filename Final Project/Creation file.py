import pandas as pd

# Create a dictionary with the data
# We map the exact name found in your data ("San Francisco") to a code ("SF")
data = {
    'Agency': ['San Francisco', 'London', 'New York'], 
    'AgencyCode': ['SF', 'LON', 'NY']
}

# Create the DataFrame
agency_df = pd.DataFrame(data)

# Save it as a CSV file
agency_df.to_csv('agency_codes.csv', index=False)

print("SUCCESS: 'agency_codes.csv' has been created!")
print(agency_df)