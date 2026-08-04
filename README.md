# East Coast Job Market Analysis

## Project Overview

This project analyzes entry-level data and analytics job opportunities across the U.S. East Coast, focusing on New Jersey, New York, Washington, D.C., Virginia, and Maryland.

The project aims to identify regional hiring trends, commonly requested technical skills, frequently advertised job titles, and differences across locations and industries. The findings will help students and recent graduates better understand the East Coast job market and prioritize the skills most relevant to entry-level analytics roles.

## Target Roles

The analysis will focus primarily on positions such as:

* Data Analyst
* Business Intelligence Analyst
* Reporting Analyst
* Operations Analyst
* Marketing Analyst
* Digital Analytics Analyst
* Research Data Analyst
* Junior Data Scientist

## Research Questions

1. Which East Coast locations offer the most entry-level data and analytics job opportunities?
2. What technical skills are most frequently requested in job postings?
3. Which job titles appear most often?
4. How do job opportunities differ across locations and industries?
5. Which skills are commonly requested together?
6. How often do entry-level positions require previous work experience?
7. Are there meaningful differences between Data Analyst and related analytics roles?

## Tools and Technologies

* Python
* pandas
* NumPy
* Matplotlib
* Jupyter Notebook
* SQL
* Microsoft Excel
* Git and GitHub

## Data Collection

The dataset will contain job postings collected from publicly available job-posting sources.

Planned variables include:

* Job title
* Company
* Location
* State
* Industry
* Salary, when available
* Required technical skills
* Required years of experience
* Education requirements
* Posting date
* Remote, hybrid, or on-site status

The final dataset will be documented with its source, collection date, and any relevant limitations.

## Planned Analysis

### 1. Data Collection

Collect job-posting data for selected data and analytics positions in New Jersey, New York, Washington, D.C., Virginia, and Maryland.

### 2. Data Cleaning

* Standardize job titles and location names
* Remove duplicate postings
* Handle missing values
* Categorize job titles and industries
* Extract technical skills from job descriptions
* Convert experience requirements into structured categories

### 3. Exploratory Data Analysis

* Compare the number of postings by state and metropolitan area
* Identify the most frequent job titles
* Calculate the frequency of requested skills
* Compare industries hiring analytics professionals
* Examine remote, hybrid, and on-site work patterns
* Analyze experience and education requirements

### 4. Visualization

Planned visualizations include:

* Job-posting counts by location
* Most common job titles
* Most frequently requested technical skills
* Skills by job category
* Job opportunities by industry
* Experience requirements by role
* Remote, hybrid, and on-site job distribution

### 5. Key Findings

Summarize the most important findings and explain their implications for students and recent graduates pursuing data-related careers on the East Coast.

## Expected Deliverables

* A cleaned and documented job-posting dataset
* Jupyter Notebooks containing the analysis
* SQL queries used to explore the dataset
* Charts and visualizations
* A summary of key findings
* A final dashboard or interactive report
* A reproducible GitHub repository with clear instructions

## Project Status

🚧 **In Progress**

Current progress:

* [x] Defined the project topic and geographic scope
* [x] Developed initial research questions
* [ ] Select and document the data source
* [ ] Collect job-posting data
* [ ] Clean and standardize the dataset
* [ ] Conduct exploratory data analysis
* [ ] Create visualizations
* [ ] Build the final dashboard or report
* [ ] Summarize findings

## Repository Structure

```text
east-coast-job-market-analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_exploratory_analysis.ipynb
│
├── sql/
│   └── analysis_queries.sql
│
├── visualizations/
│
├── src/
│
├── README.md
└── requirements.txt
```

## Limitations

Potential limitations include incomplete salary information, duplicated job postings, inconsistent job titles, and differences in how employers describe entry-level experience requirements. The results will represent the postings collected during the selected data-collection period rather than the entire job market.

