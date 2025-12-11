import os
import csv

filename=r"C:\Youssef Miled\Python programming\Final Project\Data.csv"
if not os.path.exists(filename):
    print("Could not find file")
    exit()

def count(fname,tosearch):
    with open(fname,mode='r')as f:
        reader=csv.reader(f)
        count=0
        for i,row in enumerate(reader):
            if not row:
                continue
            row_text=",".join(row).lower()
            if tosearch in row_text:
                count=count+1
    return count
def extract(fname,toextract):
    with open(fname,mode="r")as f:
        reader=csv.reader(f)
        header=next(reader)
        extracted_data=[]
        for i, row in enumerate(reader):
            if not row:
                continue
            if len(extracted_data)<toextract:
                if len(row)>=2:
                    extracted_data.append((row[0], row[1]))
        for item in extracted_data:
            print(item)
print("--- PART I: Manual File Handling ---")

try:
    with open(filename,mode="r")as f:
        reader=csv.reader(f)
        try:
            header=next(reader)
            print(f"\nSUCCESS: File opened. Header: {header}")
        except StopIteration:
            print("Error: The file is empty!")
            exit()
        print("Chief found in "+str(count(filename,"chief"))+" rows")
        extract(filename,5)
except Exception as e:
    print(f"\nCRITICAL ERROR: {e}")

#---------------------------------------------------------------
#Part 2:
import pandas as pd
print("--- PART II: Data Cleaning ---")

df=pd.read_csv(filename, low_memory=False)
cols_to_fix = ['BasePay', 'OvertimePay', 'OtherPay', 'Benefits', 'TotalPay']
for col in cols_to_fix:
    if col in df.columns:
        df[col]=pd.to_numeric(df[col],errors="coerce").fillna(0)

initial_len=len(df)
df.drop_duplicates(inplace=True)
print("Rows removed= "+str(initial_len-len(df)))
print("-> Data cleaned and salary columns fixed.")

#---------------------------------------------------------------
#Part 3:
print("--- PART III: Subsetting & Filtering ---")

def highEarners(data,high):
    highEarners=df[data['TotalPay']>=high]
    return highEarners
def employeeFrom(data,year):
    employeeFrom=df[data['Year']==year]
    return employeeFrom
def jobTitle(data,job):
    relatedJobs=df[data['JobTitle'].str.contains(job,case=False,na=False)]
    return relatedJobs

print("High earners: "+str(len(highEarners(df,200000))))
print("Employees in 2013: "+str(len(employeeFrom(df,2013))))
print("High earners: "+str(len(jobTitle(df,"POLICE"))))

#---------------------------------------------------------------
#Part 4:
print("--- PART IV: New Columns & Summary Statistics ---")

def checkJobTitle(title,keyword):
    if not isinstance(title,str):
        return False
    return keyword.lower() in title.lower()
df['Is_Job'] = df['JobTitle'].apply(checkJobTitle, keyword="Manager")
num_managers=df['Is_Job'].sum()

avg_basepay = df['BasePay'].mean()
print("Average BasePay: "+str(avg_basepay))

print(df['JobTitle'].value_counts().head(5).to_string())

print("Total Number of Employees: "+str(len(df)))

#---------------------------------------------------------------
#Part 5:
print("--- PART V: Grouping & Aggregation ---")

avg_totalpay_by_year = df.groupby('Year')['TotalPay'].mean()
print("Average TotalPay by Year:")
print(avg_totalpay_by_year.to_string())

#---------------------------------------------------------------
#Part 6:
print("--- PART VI: Joining ---")

data = {
    'Agency': ['San Francisco', 'London', 'New York'], 
    'AgencyCode': ['SF', 'LON', 'NY']
}

agency_df = pd.DataFrame(data)
agency_df.to_csv('agency_codes.csv', index=False)

print("SUCCESS: 'agency_codes.csv' has been created!")
print(agency_df)

agency_file=r"C:\Youssef Miled\Python programming\agency_codes.csv"
if not os.path.exists(agency_file):
    print("Could not find agency codes file")
    exit()
agency_df=pd.read_csv(agency_file)
merged_df = pd.merge(df, agency_df, on='Agency', how='left')
csv_filename = "merged_data.csv"
merged_df.to_csv(csv_filename, index=False)
print("Saved file as "+csv_filename)
#---------------------------------------------------------------
#Part 7:
print("--- PART VII: Interactive Investigation Script ---") 
def checkJobTitle(title,keyword):
    if not isinstance(title,str):
        return False
    return keyword.lower() in title.lower()
while True:
    print("PS: Type 'exit' to quit.")
    user_keyword=input("Enter a keyword to search in job titles: ")
    if user_keyword.lower()=='exit':
        break
    res = df['JobTitle'].apply(checkJobTitle, keyword=user_keyword)
    result=df[res]
    if result.empty:
        print("No matching job titles found.")
    else:
        count=len(result)
        avg_basepay=result['BasePay'].mean()
        highest_totalpay=result['TotalPay'].max()
        print("Number of employees with '"+user_keyword+"' in job title: "+str(count))
        print("Average BasePay: "+str(avg_basepay))
        print(f"Highest TotalPay: "+str(highest_totalpay))
        output_filename="custom_search.csv"
        result.to_csv(output_filename,index=False)
        print("Results saved to "+output_filename)













