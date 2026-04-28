import os
import urllib.request

# Yollar: src -> .. -> data
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.abspath(os.path.join(current_dir, "..", "data"))
file_name = "yellow_tripdata_2024-01.parquet"
file_path = os.path.join(data_dir, file_name)

# NYC Taxi Data URL (Parquet format)
URL = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{file_name}"


def download_real_data():
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    if os.path.exists(file_path):
        print(f"--- Veri zaten mevcut: {file_path} ---")
        return

    print(f"--- Gerçek NYC Taksi Verisi İndiriliyor (~50MB) ---")
    print(f"URL: {URL}")

    try:
        # Veriyi indir
        urllib.request.urlretrieve(URL, file_path)
        print(f"--- İndirme Tamamlandı: {file_path} ---")
    except Exception as e:
        print(f"HATA: Veri indirilemedi: {e}")


if __name__ == "__main__":
    download_real_data()