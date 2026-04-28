# 1. Hafif bir Python imajı kullan
FROM python:3.11-slim

# 2. Çalışma dizinini ayarla
WORKDIR /app

# 3. Kütüphaneleri kur
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Tüm proje dosyalarını içeri kopyala
COPY . .

# 5. OTOMASYON: Önce veriyi üret, sonra ETL'i çalıştır
# Bu komut "docker run" dendiği an her şeyi sırayla yapar
CMD ["sh", "-c", "python src/generate_data.py && python src/etl_process.py"]