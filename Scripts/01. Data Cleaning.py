"""
Project: ITSM Incident Analytics Dashboard

Author: Shruthi Lakshminarayanan

Description:
This script performs data cleaning on the ITSM Incident Dataset before validation and visualization.

Tools:
- Python
- Pandas
"""
import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA = (
    BASE_DIR
    / "Data"
    / "Raw"
    / "ITSM_Incident_Dataset_500_Records.xlsx"
)
def load_data():
    """
    Load ITSM incident dataset from Excel file.
    """
    df = pd.read_excel(RAW_DATA)
    return df
df = load_data()
print("Dataset shape:",df.shape)
print("\nFirst 5 Records")
print(df.head())
print("\nData Information")
df.info()
# Changing the data types of the columns to appropriate types
df[['Created_Date', 'Closed_Date']] = df[['Created_Date', 'Closed_Date']].apply(pd.to_datetime, errors='coerce')
df.info()
print(df.isnull().sum())
print(df.duplicated().sum())
print("Duplicate Incidents:", df['Incident_ID'].duplicated().sum()) # To check for duplicate incidents
# Checking for missing values in the dataset
print("Missing values in each column:\n", df.isnull().sum())
print("\nPriority")
print(df["Priority"].unique())
print("\nStatus")
print(df["Status"].unique())
print("\nCategory")
print(df["Category"].unique())
print("\nAssignment Group")
print(df["Assignment_Group"].unique())
print("\nLocation")
print(df["Location"].unique())
print("\nResolution Time (Hours)")
print(df['Resolution_Time_Hours'].describe())
