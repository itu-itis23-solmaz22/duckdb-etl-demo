import os
import urllib.request

# paths
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
        print(f"--- The data is already available: {file_path} ---")
        return

    print(f"--- Downloading real NYC Taxi data (~50MB) ---")
    print(f"URL: {URL}")

    try:
        # download the data
        urllib.request.urlretrieve(URL, file_path)
        print(f"--- Download complete: {file_path} ---")
    except Exception as e:
        print(f"ERROR: Data could not be downloaded: {e}")


if __name__ == "__main__":
    download_real_data()
