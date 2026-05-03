# 🔄 Power BI & Fabric: Native Writeback & Closed-Loop Analytics

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Microsoft Fabric](https://img.shields.io/badge/Microsoft_Fabric-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)
![Python](https://img.shields.io/badge/Python_UDF-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL_Serverless-CC2927?style=for-the-badge&logo=microsoft-sql-server&logoColor=white)

## 📌 Executive Summary
Standard BI dashboards are historically passive—they only report on what has happened. This repository demonstrates an enterprise architecture pattern that transcends traditional reporting by acting as an active **Data App**. 
Demo:

https://github.com/user-attachments/assets/7f302426-1fc5-4746-89fa-6df6e605b434


By leveraging **Microsoft Fabric Native Writeback**, users can take immediate operational action on insights without leaving the Power BI environment, creating a true "Closed-Loop" analytical pipeline.

## ⚙️ The Architecture Flow

The data flow seamlessly connects the Power BI front-end with the Fabric compute and storage layer, utilizing DirectQuery to instantly refresh the visual state.
```mermaid
graph TD
    A[Power BI Input Slicer<br/>& Action Button] -->|Executes| B(Fabric Python UDF)
    B -->|Data Validation & INSERT| C[(Fabric SQL Database)]
    C -->|Real-Time DirectQuery| D[Power BI Visual Table]
    
    style B fill:#3776ab,stroke:#FFE873,stroke-width:2px,color:#fff
    style C fill:#004578,stroke:#0078D4,stroke-width:2px,color:#fff
```

## 🛠️ Technical Implementation

### 1. Fabric SQL Database (The Storage)
A dedicated, serverless Fabric SQL Database (`FPA_Writeback_DB`) is deployed to capture user-generated inputs. The schema is designed with strict data governance and automated audit trails (`CreatedAt`, `CreatedBy`).
* 📁 **Source Code:** [`/src/setup_database.sql`](./src/setup_database.sql)

### 2. Python User-Defined Functions (The Compute)
Custom Fabric UDFs are utilized to bridge Power BI and SQL. The Python script securely processes the inputs passed from DAX (via explicit string casting), validates character limits, and executes the parameterized SQL `INSERT` commands.
* 📁 **Source Code:** [`/src/writeback_udf.py`](./src/writeback_udf.py)

### 3. Power BI Integration (The Interface)
* **Explicit DAX Type Casting:** To pass dynamic filter context into the Python function, `SELECTEDVALUE()` is wrapped in `CONVERT(..., STRING)` to strictly match the UDF parameter types.
* **DirectQuery Injection:** The writeback table is integrated back into the semantic model via DirectQuery. This creates a real-time feedback loop where the user's action plan instantly renders in the report's visual table, bypassing the need for a scheduled dataset refresh.

## 🎯 Business Use Case (Example)
**Strategic Action Planning:** When an FP&A controller identifies an "Empty Calorie" client (high volume, negative margin) on the scatter plot, they can instantly select the client, log a strategic mitigation plan (e.g., *"Renegotiate contract by +5% in Q3"*), and save it. The data is instantly broadcasted to the centralized SQL instance for organizational alignment.
