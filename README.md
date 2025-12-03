# 🎵 Spotify End-to-End Data Engineering Pipeline

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python&logoColor=white)
![AWS S3](https://img.shields.io/badge/AWS-S3-orange?logo=amazon-aws&logoColor=white)
![Snowflake](https://img.shields.io/badge/Snowflake-Data_Warehouse-blue?logo=snowflake&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-yellow?logo=power-bi&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automated-green?logo=github-actions&logoColor=white)

## 📌 Project Overview
This project is a robust **ETL (Extract, Transform, Load) pipeline** designed to analyze global music trends. It automates the extraction of data from the **Spotify API**, stores raw data in a **AWS S3 Data Lake**, warehouses structured data in **Snowflake**, and visualizes insights using **Power BI**.

The pipeline is fully automated using **GitHub Actions**, running on a daily schedule to ensure the dashboard reflects the latest music trends without manual intervention.

---

## 🏗️ System Architecture

The pipeline follows a modern data stack architecture:

```graph LR
    A[Spotify API] -->|Extract (Python/Spotipy)| B(GitHub Actions Runner)
    B -->|Transform & Clean| B
    B -->|Load CSV| C[AWS S3 Bucket]
    C -->|Auto-Ingest / Copy Into| D[Snowflake Data Warehouse]
    D -->|Direct Query| E[Power BI Dashboard]
```

## 🛠️ Tech Stack & Tools

| Component | Tool | Description & Usage |
| :--- | :--- | :--- |
| **Scripting** | **Python 3.9** | Used for API extraction (Spotipy) and data transformation (Pandas). |
| **Data Lake** | **AWS S3** | Stores raw `.csv` files extracted from Spotify before processing. |
| **Warehouse** | **Snowflake** | Serves as the central repository; auto-ingests data from S3 using Snowpipe. |
| **Automation** | **GitHub Actions** | Orchestrates the ETL pipeline to run daily at 6:00 AM via CRON jobs. |
| **Viz** | **Power BI** | Connects to Snowflake via Direct Query to visualize artist popularity trends. |


## 🚀 Setup & Installation

Follow these steps to set up the project locally.

### 1. Prerequisites
Ensure you have the following installed:
* **Python 3.9+**
* **Git**
* An **AWS Account** (S3 Bucket created)
* A **Snowflake Account** (Standard or Trial)
* A **Spotify Developer Account** (to get API keys)

### 2. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/spotify-etl-pipeline.git](https://github.com/YOUR_USERNAME/spotify-etl-pipeline.git)
cd spotify-etl-pipeline
```




