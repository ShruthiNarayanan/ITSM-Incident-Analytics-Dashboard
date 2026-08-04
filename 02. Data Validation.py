"""
Project: ITSM Incident Analytics Dashboard

Author: Shruthi Lakshminarayanan

Description:
This script performs data validation on the ITSM Incident Dataset before visualization.

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
CLEANED_DIR = (
    BASE_DIR
    / "Data"
    / "Cleaned"
)
CLEANED_DIR.mkdir(
    parents=True,
    exist_ok=True
)
is_distinct = df['Incident_ID'].is_unique
print("Are Incident IDs distinct?", is_distinct) # To check if Incident_IDs are unique
missing_dates = df[['Created_Date']].isnull().sum()
print("Missing Created Dates:", missing_dates) # To check for missing Created Dates per INC.
invalid_dates = df[df['Created_Date']> df['Closed_Date']]
print("Invalid date : \n", invalid_dates) # To check for invalid dates where Created_Date is after Closed_Date
missing_closed_dates = df[(df['Status'] == 'Closed') & (df['Closed_Date'].isna())]
print("Missing Closed Dates:", missing_closed_dates) # To check for missing Closed Dates in Closed INCs
missing_category = df[['Category']].isnull().sum()
print("Missing Category:", missing_category) # To check for missing Category
missing_sub_category = df[['Sub_Category']].isnull().sum()
print("Missing Sub Category:", missing_sub_category) # To check for missing Sub Category
missing_service = df[['Service']].isnull().sum()
print("Missing Service:", missing_service) # To check for missing Service
missing_assignment_group = df[['Assignment_Group']].isnull().sum()
print("Missing Assignment Group:", missing_assignment_group) # To check for missing Assignment Group
incorrect_closed_dates = df[(df['Status'].isin(['Open', 'Pending'])) & (df['Closed_Date'].notna())]
print("Incorrect Closed Dates:", incorrect_closed_dates.shape[0]) # To check for consistency between Status and Closed_Date
incorrect_SLA_Status = df[(df['SLA_Status'] == 'Met') & (df['Resolution_Time_Hours'] > df['SLA_Target_Hours'])]
print("Incorrect SLA Status:", incorrect_SLA_Status.shape[0]) # To check for incorrect SLA Status
print(incorrect_SLA_Status[['Incident_ID', 'SLA_Status', 'Resolution_Time_Hours', 'SLA_Target_Hours']]) # To print the rows that are incorrect
sla_matrix = {
    'P1': 4.0,
    'P2': 8.0,
    'P3': 24.0,
    'P4': 72.0
}
df['Expected_SLA_Hours'] = df['Priority'].map(sla_matrix)
wrong_sla_target = df[
    (df['Priority'].isin(sla_matrix.keys())) & (df['SLA_Target_Hours'] != df['Expected_SLA_Hours'])
]
print("Incorrect SLA Target Hours:", wrong_sla_target.shape[0]) # To check for incorrect SLA Target Hours
print(wrong_sla_target[['Incident_ID', 'SLA_Status', 'Resolution_Time_Hours', 'SLA_Target_Hours']]) # To print the rows that are incorrect
incorrect_affected_users = df[(df['Affected_Users'] < 0)]
print("Incorrect Affected Users:", incorrect_affected_users.shape[0]) # To check for incorrect Affected User
incorrect_priority = df[
    (df['Priority'].isin(['P3', 'P4'])) & 
    (df['Business_Criticality'] == 'High') & 
    (df['Impact'] == 'High') & 
    (df['Urgency'] == 'High')
    ]
print("Incorrect Priority:", incorrect_priority.shape[0]) # To check for incorrect Priority
print(incorrect_priority[['Incident_ID', 'Priority', 'Business_Criticality', 'Impact', 'Urgency']]) # To print the rows that are incorrect
# Update the priority to P1 for High-severity incidents
df.loc[
    (df["Business_Criticality"] == "High")
    & (df["Impact"] == "High")
    & (df["Urgency"] == "High"),
    "Priority",
] = "P1"
# Save to a specific folder on Windows
df.to_excel(
    CLEANED_DIR / "Corrected_Incidents_Report.xlsx",
    index=False
)
print(
    f"Corrected dataset saved to:\n{CLEANED_DIR / 'Corrected_Incidents_Report.xlsx'}"
)
df.drop(columns=["Expected_SLA_Hours"], inplace=True)