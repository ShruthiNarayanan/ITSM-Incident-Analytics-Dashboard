"""
Project: ITSM Incident Analytics Dashboard

Author: Shruthi Lakshminarayanan

Description:
This script performs data visualization on the ITSM Incident Dataset.

Tools:
- Python
- Pandas
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
CLEANED_DATA = (
    BASE_DIR
    / "Data"
    / "Cleaned"
    / "Corrected_Incidents_Report.xlsx"
)
OUTPUT_DIR = (
    BASE_DIR
    / "Outputs"
    / "Charts"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)
def load_data():
    """
    Load ITSM incident dataset from Excel file.
    """
    df = pd.read_excel(CLEANED_DATA)
    return df
df = load_data()
def create_bar_chart(data, title, xlabel, ylabel, filename):
    """ 
    Creates a bar chart and saves it as a PNG file.
    """
    plt.figure(figsize=(10,6))

    bars = plt.bar(
        data.index,
        data.values
    )

    for bar in bars:
        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 1,
            str(int(height)),
            ha='center'
        )

    plt.title(
        title,
        fontsize=16,
        fontweight='bold'
    )

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.xticks(rotation=45)

    plt.grid(
        axis='y',
        linestyle='--',
        alpha=0.7
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / filename,
        dpi=300,
        bbox_inches="tight"
    )
    plt.show()
def create_grouped_bar_chart(
    data,
    title,
    xlabel,
    ylabel,
    legend_title,
    filename
):
    """
    Create a grouped bar chart from a DataFrame.
    Each column in the DataFrame becomes one bar group.
    """

    x_indexes = np.arange(len(data.index))
    num_series = len(data.columns)
    bar_width = 0.8 / num_series

    plt.figure(figsize=(12, 6))

    for i, column in enumerate(data.columns):

        offset = (i - (num_series - 1) / 2) * bar_width

        bars = plt.bar(
            x_indexes + offset,
            data[column],
            width=bar_width,
            label=column
        )

        # Optional: add labels on top
        for bar in bars:
            height = bar.get_height()

            plt.text(
                bar.get_x() + bar.get_width() / 2,
                height + 0.2,
                str(int(height)),
                ha="center",
                va="bottom",
                fontsize=8
            )

    plt.xticks(x_indexes, data.index)

    plt.title(title, fontsize=16, fontweight="bold")
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)

    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.legend(title=legend_title)

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / filename,
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
 # 1. Which month has the most incidents?
df['Created_Date'] = pd.to_datetime(df['Created_Date'], errors='coerce')
df['Month_Name'] = df['Created_Date'].dt.month_name()
month_order = [
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
]
df['Month_Name'] = pd.Categorical(df['Month_Name'], categories=month_order, ordered=True)
monthly_summary = (
    df.groupby(
        'Month_Name',
        observed=False
    )['Incident_ID']
    .nunique()
)
create_bar_chart(
    monthly_summary,
    "Monthly Incident Volume Trend",
    "Month",
    "Incident Count",
    "Monthly_Incident_Volume.png"
)
# 2. What is the average resolution time?
overall_avg_resolution_time = df['Resolution_Time_Hours'].mean()
print(f"The average resolution time is: {overall_avg_resolution_time:.2f} hours")
# 3. Which categories take the longest to resolve?
average_resolution_time = df.groupby('Category', observed=False)['Resolution_Time_Hours'].mean().sort_values(ascending=False)
print(average_resolution_time)
create_bar_chart(
    average_resolution_time,
    "Average Resolution Time by Category",
    "Category",
    "Average Resolution Time (Hours)",
    "Average_Resolution_Time_by_Category.png"
)
#4. Which category has more incidents?
category_incidents = df.groupby('Category', observed=False)['Incident_ID'].nunique().sort_values(ascending=False)
create_bar_chart(
    category_incidents,
    "Incident Count by Category",
    "Category",
    "Incident Count",
    "Incident_Count_by_Category.png"
)
# 5. What is the distribution of incidents by priority?
incident_per_priority = df.groupby('Priority', observed=False)['Incident_ID'].nunique().sort_values(ascending=False)
create_bar_chart(
    incident_per_priority,
    "Incident Count by Priority",
    "Priority",
    "Incident Count",
    "Incident_Count_by_Priority.png"
)
# 6. Which team has more incidents?
team_incidents = df.groupby('Assignment_Group', observed=False)['Incident_ID'].nunique().sort_values(ascending=False)
create_bar_chart(
    team_incidents,
    "Incident Count by Assignment Group",
    "Assignment Group",
    "Incident Count",
    "Incident_Count_by_Assignment_Group.png"
)
grouped = df.groupby(['Category', 'Status'], observed=False)['Incident_ID'].nunique()
incident_per_category = grouped.unstack(fill_value=0)
incident_per_category["Total"] = incident_per_category.sum(axis=1)

incident_per_category = (
    incident_per_category
    .sort_values("Total", ascending=False)
    .drop(columns="Total")
)

create_grouped_bar_chart(
    incident_per_category,
    "Incident Status Distribution by Category",
    "Category",
    "Incident Count",
    "Incident Status",
    "incident_status_by_category.png"
)
# 8. SLA status - monthly  
SLA_status_monthly = df.groupby(['Month_Name', 'SLA_Status'], observed=False)['Incident_ID'].nunique().unstack(fill_value=0)
create_grouped_bar_chart(
    SLA_status_monthly,
    "SLA Status Distribution by Month",
    "Month",
    "Incident Count",
    "SLA Status",
    "sla_status_by_month.png"
)
# 9. Which services affected the most users?
affected_users_services = df.groupby('Service')['Affected_Users'].sum()
create_bar_chart(
    affected_users_services,
    "Affected Users by Service",
    "Service",
    "Affected Users Count",
    "affected_users_by_service.png"
)
# 10. Regions affected by month 
regions_affected_monthly = df.groupby(['Month_Name', 'Location'], observed=False)['Incident_ID'].nunique().unstack(fill_value=0)
create_grouped_bar_chart(
    regions_affected_monthly,
    "Regions Affected by Month",
    "Month",
    "Incident Count",
    "Location",
    "regions_affected_by_month.png"
)
# 11. Which services have the highest number of High Business Criticality incidents?
high_bc = df[df['Business_Criticality'] == 'High']
service_summary = (
    high_bc
    .groupby('Service')['Incident_ID']
    .count()
    .sort_values(ascending=False)
)
create_bar_chart(
    service_summary,
    "High Business Criticality Incidents by Service",
    "Service",
    "Incident Count",
    "high_bc_incidents_by_service.png"
)
# 12. Do Known Errors reduce average resolution time?
# known_error_incidents = df[df['Known_Error'] == 'Yes'].groupby('Known_Error', observed=False)['Incident_ID'].nunique()
known_error = df[df['Known_Error'] == 'Yes']
incident_known_error = (
    known_error
    .groupby('Known_Error')['Incident_ID']
    .count()
    .sort_values(ascending=False)
)
print('Incident Count for Known Errors:' + str(incident_known_error.iloc[0]))
# Calculate the actual average time
avg_time = df.groupby('Known_Error')['Resolution_Time_Hours'].mean()
# Corrected function call to plot Resolution Time instead of Incident Counts
create_bar_chart(
    avg_time,
    "Average Resolution Time: Known Errors vs Others",
    "Known Error Status",
    "Average Resolution Time (Hours)",
    "average_resolution_time.png"
)