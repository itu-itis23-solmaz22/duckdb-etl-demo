import duckdb
import os
import time

# file path
current_dir = os.path.dirname(os.path.abspath(__file__))
parquet_path = os.path.abspath(os.path.join(current_dir, "..", "data", "yellow_tripdata_2024-01.parquet"))


def run_real_analysis():
    # Windows path
    duck_path = parquet_path.replace('\\', '/')

    print(f"--- Real Data Analysis is Starting ---")
    print(f"File: {duck_path}")

    if not os.path.exists(parquet_path):
        print("ERROR: Data file not found! generate_data.py must be run first.")
        return

    con = duckdb.connect(database=':memory:')

    start_time = time.time()

    # Real data analysis: Average daily tips and number of trips.
    query = f"""
        SELECT 
            tpep_pickup_datetime::DATE as trip_date,
            COUNT(*) as trip_count,
            ROUND(AVG(tip_amount), 2) as avg_tip,
            ROUND(AVG(fare_amount), 2) as avg_fare
        FROM read_parquet('{duck_path}')
        GROUP BY 1
        ORDER BY 1
        LIMIT 10
    """

    result = con.execute(query).df()
    end_time = time.time()

    print(f"\nAnalysis Time: {end_time - start_time:.4f} seconds")
    print("\n--- January 2024 First 10 Days Analysis ---")
    print(result)


if __name__ == "__main__":
    run_real_analysis()