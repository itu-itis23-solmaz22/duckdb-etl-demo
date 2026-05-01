# YZV 322E - Individual Tool Presentation: DuckDB

## 1. Purpose and Scope
This project demonstrates the capabilities of **DuckDB** as an in-process analytical (OLAP) database engine. We showcase a real-world data engineering pipeline that fetches live NYC Taxi data in Parquet format and performs high-speed SQL analysis.

## 2. Key Features
- **Zero-Setup ETL:** Automatically downloads real NYC Taxi data (~50MB) upon first run.
- **Parquet Integration:** Leverages columnar storage for optimized query performance.
- **Dockerized Environment:** Ensures "works on my machine" reliability for the presentation.

## 3. Course Connection
- **Core Tool Relation:** While **PostgreSQL** (covered in class) is the gold standard for OLTP (transactional) workloads, **DuckDB** is purpose-built for OLAP (analytical) tasks. 
- **Pipeline Role:** It acts as the analytical layer that consumes data from raw files (CSV/Parquet) or Pandas DataFrames without requiring a persistent database server.

## 4. Setup and Demo (How to Run)

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

### Automatic Run (Recommended)
Simply run the following command in the project root:
```bash
docker-compose up --build
