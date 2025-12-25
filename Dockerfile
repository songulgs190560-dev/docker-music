# Hafif bir Python imajı kullan
FROM python:3.9-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Gerekli dosyaları kopyala
COPY requirements.txt .
COPY app.py .

# Kütüphaneleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamayı çalıştır (varsayılan arama terimiyle)
ENTRYPOINT ["python", "app.py"]
