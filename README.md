# 🚀 Automated Sales Data Pipeline — Azure Data Factory + Python + SQL

![Azure](https://img.shields.io/badge/Azure-Data%20Factory-blue)
![Python](https://img.shields.io/badge/Python-ETL-yellow)
![SQL](https://img.shields.io/badge/SQL-Data%20Warehouse-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📖 Project Overview
This project demonstrates how to design a **real-world data pipeline** that automates the process of:
1. Ingesting raw sales CSV files from **Azure Blob Storage**
2. Cleaning and transforming data using **Python**
3. Loading the clean data into **Azure SQL Database**
4. Creating an aggregated **monthly sales summary** using **SQL**

It simulates the same workflow many companies use to automate daily reporting.

---

## 🧠 Objectives
✅ Build an **end-to-end ETL/ELT pipeline**  
✅ Apply **data cleaning and transformation** logic  
✅ Automate data loading and reporting  
✅ Showcase **Azure Data Factory orchestration** in a portfolio-ready example

---


---

## ⚙️ Tech Stack
- **Azure Data Factory** — Pipeline orchestration  
- **Azure Blob Storage** — Data lake for raw CSV files  
- **Python** — Data transformation scripts  
- **Azure SQL Database** — Data warehouse  
- **Power BI / SQL queries** — Reporting layer  

---

## 📂 Pipeline Steps
1. **Extract** — ADF pipeline reads CSV files from Azure Blob Storage  
2. **Transform** — Python cleans nulls, formats dates, and aggregates metrics  
3. **Load** — Data is inserted into SQL tables  
4. **Report** — SQL creates summarized monthly sales data for insights  

---

## 🧾 SQL Aggregation Example
```sql
SELECT 
    Region,
    MONTH(SaleDate) AS SaleMonth,
    SUM(SalesAmount) AS TotalSales
FROM Sales_Clean
GROUP BY Region, MONTH(SaleDate);
