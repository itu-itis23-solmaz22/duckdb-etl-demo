# 1. a lightweight Python image.
FROM python:3.11-slim

# 2. Set the working directory
WORKDIR /app

# 3. Set up libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy all project files inside.
COPY . .

# 5. AUTOMATION: First generate the data, then run the ETL
CMD ["sh", "-c", "python src/generate_data.py && python src/etl_process.py"]