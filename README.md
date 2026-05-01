YZV 322E - Individual Tool Presentation: DuckDB
1. What is DuckDB?
DuckDB is an in-process SQL OLAP (Online Analytical Processing) database management system designed for fast analytical queries. Unlike traditional client-server databases like PostgreSQL, DuckDB operates as a library within the host process, which eliminates network overhead and makes it incredibly efficient for data engineering pipelines, especially when working with columnar formats like Parquet.

2. Prerequisites
To run this project, the following software and versions are required:

Operating System: Windows 10/11, macOS, or Linux.

Docker Desktop: Version 20.10 or higher (Required for the automated demo).

Python: Version 3.10 or 3.11 (If running locally without Docker).

Memory: Minimum 4GB RAM (To handle the NYC Taxi dataset in-memory).

3. Installation
Follow these steps to set up the project on your local machine:

Bash
# 1. Clone the repository
git clone https://github.com/KULLANICI_ADIN/duckdb-etl-demo.git

# 2. Navigate into the project folder
cd duckdb-etl-demo
4. Running the Example
You can execute the entire pipeline (automatic data download + SQL analysis) using Docker or local Python.

Option A: Using Docker (Recommended for Presentation)
This command builds the environment and runs the ETL pipeline automatically:

Bash
docker-compose up --build
Option B: Using Local Python
If you prefer to run it manually:

Bash
pip install -r requirements.txt
python src/generate_data.py
python src/etl_process.py
5. Expected Output
When the pipeline runs successfully, you should see an output similar to the following in your terminal:

Plaintext
duckdb-presentation-1  | --- Gerçek NYC Taksi Verisi İndiriliyor (~50MB) ---
duckdb-presentation-1  | URL: https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet
duckdb-presentation-1  | --- İndirme Tamamlandı ---
duckdb-presentation-1  |
duckdb-presentation-1  | --- Gerçek Veri Analizi Başlıyor ---
duckdb-presentation-1  | Analiz Süresi: 1.3281 saniye
duckdb-presentation-1  |
duckdb-presentation-1  | --- Ocak 2024 İlk 10 Gün Analizi ---
duckdb-presentation-1  |     trip_date  trip_count  avg_tip  avg_fare
duckdb-presentation-1  | 0  2024-01-01      81013     3.26     21.79
duckdb-presentation-1  | 1  2024-01-02      75519     3.52     20.97
duckdb-presentation-1  | 2  2024-01-03      82427     3.37     19.66
6. AI Usage Disclosure
AI Tool: Gemini 3 Flash (Google AI).

Purpose: This AI tool was used to assist in designing the project architecture, configuring the Docker environment, debugging pathing issues on Windows, and optimizing the DuckDB SQL queries for the presentation.

7. Course Connection
While PostgreSQL (covered in class) is the gold standard for OLTP (transactional) workloads, DuckDB is purpose-built for OLAP (analytical) tasks. It serves as an efficient analytical layer in modern data pipelines, allowing direct queries on external files (Parquet/CSV) or Pandas DataFrames without requiring a persistent database server.
