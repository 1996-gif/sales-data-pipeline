# Automated Sales Data Pipeline — From Raw CSV to Clean SQL Table using Azure Data Factory

## Overview
This project demonstrates how to build a data ingestion and transformation pipeline that ingests raw sales CSVs from Azure Blob Storage, cleans them using Python, and loads them into Azure SQL for reporting.

## Tech Stack
- Azure Data Factory
- Azure Blob Storage
- Azure SQL Database
- Python
- SQL

## Project Structure
```
sales-data-pipeline/
├── data/
│   ├── raw/
│   └── clean/
├── scripts/
├── adf_pipeline/
└── reports/
```

## How It Works
1. Upload sales CSVs to Azure Blob Storage.
2. ADF triggers a Python script to clean and transform data.
3. ADF copies the clean data into Azure SQL.
4. A stored procedure aggregates sales per region/month.

## Example
Raw → Clean → SQL → Report summary.

## Author
**Sandeep Sawan**
_Data Engineer | Azure | SQL | Python_
📧 sandeep.sawan.careers@gmail.com
