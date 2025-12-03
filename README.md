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

```mermaid
graph LR
    A[Spotify API] -->|Extract (Python/Spotipy)| B(GitHub Actions Runner)
    B -->|Transform & Clean| B
    B -->|Load CSV| C[AWS S3 Bucket]
    C -->|Auto-Ingest / Copy Into| D[Snowflake Data Warehouse]
    D -->|Direct Query| E[Power BI Dashboard]

---
## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| **Cloud** | ![AWS](https://img.shields.io/badge/AWS_S3-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white) |
| **Warehouse** | ![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white) |
| **Orchestration** | ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white) |
| **Visualization** | ![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=power-bi&logoColor=black) |
| **Libraries** | `pandas`, `spotipy`, `boto3` |

---


