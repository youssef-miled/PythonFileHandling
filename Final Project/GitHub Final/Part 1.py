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













