# ITSM Incident Analytics Dashboard | Python, Pandas & Data Visualization

## Project Overview

The **ITSM Incident Analytics Dashboard** is an end-to-end data analytics project developed using Python and Pandas to analyse IT Service Management (ITSM) incident data.

The project demonstrates a complete analytics workflow, starting from raw data, performing data cleaning and validation, answering business-driven questions, and visualising key operational metrics. The objective is to showcase how data can support IT Operations and Service Management teams in making informed decisions.

---

## Features

- End-to-end data analytics workflow
- Data cleaning and validation
- Business rule validation
- Exploratory Data Analysis (EDA)
- Automated chart generation
- Reusable visualization functions
- Modular Python scripts

## Business Problem

IT Operations teams receive hundreds of incidents every month. Without proper analysis, it becomes difficult to identify recurring issues, understand operational performance, monitor SLA compliance, and prioritise improvement efforts.

This project aims to transform raw incident data into meaningful insights that help answer real business questions such as:

* Which months experience the highest number of incidents?
* Which categories generate the most incidents?
* Which categories take the longest to resolve?
* How are incidents distributed across priorities?
* Which assignment groups handle the highest workload?
* How is SLA performance changing over time?
* Which services experience the highest number of High Business Criticality incidents?
* How do Known Errors contribute to incident management?

---

## Objectives

* Clean and validate raw ITSM incident data.
* Perform exploratory data analysis (EDA).
* Answer business-focused operational questions.
* Generate meaningful visualisations.
* Demonstrate practical use of Python and Pandas in data analytics.

---
## Project Workflow

The project follows a structured data analytics workflow:

Raw Dataset
↓
Data Cleaning
↓
Data Validation
↓
Exploratory Data Analysis (EDA)
↓
Business Analysis
↓
Data Visualization
↓
Business Insights

## Technologies Used

* Python
* Pandas
* Matplotlib
* OpenPyXL
* Microsoft Excel
* Visual Studio Code
* Git & GitHub

---

## Project Structure

ITSM-Incident-Analytics
│
├── Data
│   ├── Raw
│   └── Cleaned
│
├── Outputs
│   └── Charts
│
├── Scripts
│   ├── 01_Data_Cleaning.py
│   ├── 02_Data_Validation.py
│   └── 03_Data_Visualization.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Data Cleaning

The dataset was cleaned before analysis by:

* Checking for duplicate Incident IDs
* Validating missing values
* Converting date columns to datetime format
* Verifying data consistency
* Creating derived columns required for analysis

---

## Data Validation

The following validation checks were performed:

* Unique Incident IDs
* Missing Created Dates
* Closed Date validation
* Closed incidents must contain Closed Date
* Mandatory fields validation
* Assignment Group validation
* Status and Closed Date consistency
* SLA Status validation
* SLA Target validation
* Negative affected users validation
* Priority validation based on Business Criticality, Impact and Urgency

---

## Business Questions Answered

1. Which month has the most incidents?
2. What is the overall average resolution time?
3. Which categories take the longest to resolve?
4. Which category has the highest number of incidents?
5. What is the distribution of incidents by priority?
6. Which assignment groups receive the most incidents?
7. What is the distribution of incident status by category?
8. What is the monthly SLA status?
9. Which incidents and services affect the highest number of users?
10. Which regions experience the highest number of incidents by month?
11. Which services have the highest number of High Business Criticality incidents?
12. Do Known Errors reduce average resolution time?

---
## Project Outputs

The project generates:

- Cleaned ITSM dataset
- Validation report
- Business insights
- High-quality charts (.png)
- Summary statistics

---

## Sample Visualizations

### Monthly Incident Volume

![Monthly Incident Volume](Outputs/Charts/Monthly_Incident_Volume.png)

### Incident Count by Category

![Incident Count by Category](Outputs/Charts/Incident_Count_by_Category.png)

### SLA Status by Month

![SLA Status](Outputs/Charts/sla_status_by_month.png)
---

## Key Skills Demonstrated

* Data Cleaning
* Data Validation
* Exploratory Data Analysis (EDA)
* Business Problem Solving
* Data Visualisation
* Python Programming
* Pandas
* ITSM Domain Knowledge
* Root Cause Analysis
* KPI Development

---
## How to Run

1. Clone the repository

```bash
git clone https://github.com/<your-github-username>/ITSM-Incident-Analytics.git
```

2. Install the required libraries

```bash
pip install -r requirements.txt
```

3. Run the scripts in the following order:

```text
01_Data_Cleaning.py
        ↓
02_Data_Validation.py
        ↓
03_Data_Visualization.py
```

The project will generate:

- A cleaned dataset in `Data/Cleaned`
- Charts in `Outputs/Charts`
---


## Future Enhancements

* Develop an interactive Power BI dashboard.
* Automate data ingestion using Python.
* Build KPI dashboards for IT Operations.
* Add trend analysis and predictive analytics.
* Integrate SQL for querying larger datasets.

---

## About This Project

This project was created as part of my transition into Data Analytics while leveraging over eight years of experience in IT Service Management (ITSM), Release Management, and IT Operations. It demonstrates how operational knowledge combined with data analytics can help organisations improve service quality, identify trends, and support data-driven decision-making.
