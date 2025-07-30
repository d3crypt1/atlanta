# Use the official lightweight Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (for geopandas and streamlit)
RUN apt-get update && apt-get install -y \
    build-essential \
    gdal-bin \
    python3-dev \
    libgdal-dev \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Copy Data
COPY data/ ./data/

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy app code
COPY atlanta_sales_streamlit.py .

# Expose Streamlit port
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "atlanta_sales_streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]
