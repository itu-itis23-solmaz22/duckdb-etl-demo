# YZV 322E - Individual Tool Presentation: DuckDB

## 🦆 What is DuckDB?
**DuckDB** is an in-process SQL OLAP (Online Analytical Processing) database management system designed for fast analytical queries. Unlike traditional client-server databases like PostgreSQL, DuckDB operates as a **library within the host process**, which eliminates network overhead and makes it incredibly efficient for data engineering pipelines, especially when working with columnar formats like **Parquet**.

---

## 🛠 Prerequisites
To run this project, the following software and hardware specifications are required:
* **Operating System:** Windows 10/11, macOS, or Linux.
* **Docker Desktop:** Version 20.10 or higher (Required for the automated demo).
* **Python:** Version 3.10 or 3.11 (If running locally without Docker).
* **Memory:** Minimum 4GB RAM (To handle the NYC Taxi dataset in-memory).

---

## 📥 Installation
Follow these steps to set up the project on your local machine:

1. **Clone the repository**
git clone https://github.com/itu-itis23-solmaz22/duckdb-etl-demo.git

2. **Navigate into the project folder**
cd duckdb-etl-demo

<img width="1478" height="754" alt="installation" src="https://github.com/user-attachments/assets/a06480bf-bccc-4f29-80d0-26a0b68e73f0" />

---

## 🚀 Running the Example
You can execute the entire pipeline (automatic data download + SQL analysis) using Docker or local Python.
(Before proceeding, ensure that Docker Desktop is open and the engine is running.)
<img width="1590" height="747" alt="engine_running" src="https://github.com/user-attachments/assets/9d901ce0-569b-4c9e-93ac-e46e8f1884af" />


### Option A: Using Docker
This command builds the environment and runs the ETL pipeline automatically:

docker-compose up --build

### Option B: Using Local Python
If you prefer to run it manually:

pip install -r requirements.txt
python src/generate_data.py
python src/etl_process.py

---

## 📊 Expected Output
When the pipeline runs successfully, you should see an output similar to the following in your terminal:

<img width="1478" height="763" alt="part1" src="https://github.com/user-attachments/assets/fa680314-9ba6-4328-9181-81e5fa1c6ca3" />

<img width="1479" height="761" alt="part2" src="https://github.com/user-attachments/assets/fd6a6737-798f-48d5-b3aa-f929f9793bfe" />

<img width="1479" height="760" alt="part3" src="https://github.com/user-attachments/assets/d6bb0f7d-bf80-4309-943f-f53331c90b81" />


---

## 🧠 AI Usage Disclosure
* **AI Tool:** Gemini 3 Flash (Google AI).
* **Purpose:** This AI tool was used to assist in designing the project architecture, configuring the Docker environment, debugging pathing issues on Windows, and optimizing the DuckDB SQL queries for the presentation.

---

## 🎓 Course Connection
While **PostgreSQL** (covered in class) is the gold standard for OLTP (transactional) workloads, **DuckDB** is purpose-built for OLAP (analytical) tasks. It serves as an efficient analytical layer in modern data pipelines, allowing direct queries on external files (Parquet/CSV) or Pandas DataFrames without requiring a persistent database server.
