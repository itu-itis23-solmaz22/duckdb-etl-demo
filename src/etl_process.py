import duckdb
import os
import time

# Dosya yolu
current_dir = os.path.dirname(os.path.abspath(__file__))
parquet_path = os.path.abspath(os.path.join(current_dir, "..", "data", "yellow_tripdata_2024-01.parquet"))


def run_real_analysis():
    # Windows yolu düzeltme
    duck_path = parquet_path.replace('\\', '/')

    print(f"--- Gerçek Veri Analizi Başlıyor ---")
    print(f"Dosya: {duck_path}")

    if not os.path.exists(parquet_path):
        print("HATA: Veri dosyası bulunamadı! Önce generate_data.py çalıştırılmalı.")
        return

    con = duckdb.connect(database=':memory:')

    start_time = time.time()

    # Gerçek veri analizi: Günlük ortalama bahşiş ve yolculuk sayısı
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

    print(f"\nAnaliz Süresi: {end_time - start_time:.4f} saniye")
    print("\n--- Ocak 2024 İlk 10 Gün Analizi ---")
    print(result)


if __name__ == "__main__":
    run_real_analysis()