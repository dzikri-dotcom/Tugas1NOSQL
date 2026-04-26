import os
import threading
import time
from flask import Flask, render_template, request
from pymongo import MongoClient
from scripts.api_collector import *
from scripts.web_scraper import *

app = Flask(__name__)

# --- KONFIGURASI DATABASE (MONGODB ATLAS) ---
# Gunakan link koneksi dari akun Dzikri Lathiful Qodim
MONGO_URI = "mongodb+srv://dzikrilathifulqodim_db_user:Dzikri987321@tugas1nosql.xp3k9pj.mongodb.net/?retryWrites=true&w=majority&appName=Tugas1Nosql"

try:
    client = MongoClient(MONGO_URI)
    db = client["pbd_tugas1"]
    col = db["crawl_results"]
    # Membuat Text Index untuk fitur Search Engine cepat sesuai kriteria tugas
    col.create_index([("title", "text"), ("text", "text")])
    print("✔ Terhubung ke MongoDB Atlas")
except Exception as e:
    print(f"✘ Gagal terhubung ke MongoDB: {e}")

API_KEY = "465a1185759846f7bc02a799d1929162"

def background_crawler():
    """Menjalankan otomasi crawling setiap 5 menit secara real-time"""
    while True:
        try:
            print(f"\n[{time.strftime('%H:%M:%S')}] Memulai penarikan data otomatis...")
            
            # Gabungkan data dari minimal 2 sumber (API & Website)
            data = (
                fetch_news_api(API_KEY) + fetch_crypto_api() + 
                fetch_exchange_rate() + fetch_weather_api() +
                scrape_detik() + scrape_cnbc() + 
                scrape_kompas() + scrape_tempo()
            )
            
            if data:
                for d in data:
                    # Update atau insert (upsert) berdasarkan ID agar tidak duplikat
                    col.update_one({"_id": d["_id"]}, {"$set": d}, upsert=True)
                print(f"✔ Berhasil memperbarui {len(data)} dokumen di Cloud Atlas.")
        except Exception as e:
            print(f"⚠ Error saat crawling: {e}")
            
        # Tunggu 5 menit (300 detik) untuk iterasi berikutnya
        time.sleep(300)

@app.route('/')
def index():
    # Fitur Search Engine: Mengambil input dari bar pencarian di index.html
    search_query = request.args.get('search')
    
    try:
        if search_query:
            # Mencari data menggunakan Text Index MongoDB
            docs = list(col.find({"$text": {"$search": search_query}}).sort("ts", -1))
        else:
            # Default: Menampilkan 30 data terbaru
            docs = list(col.find().sort("ts", -1).limit(30))
        
        stats = {
            "total": col.count_documents({}),
            "api": col.count_documents({"fmt": "json"}),
            "web": col.count_documents({"fmt": "html"})
        }
    except:
        docs = []
        stats = {"total": 0, "api": 0, "web": 0}

    return render_template('index.html', docs=docs, stats=stats)

if __name__ == "__main__":
    # 1. Jalankan crawler di thread terpisah agar sistem berjalan real-time
    threading.Thread(target=background_crawler, daemon=True).start()
    
    # 2. Jalankan Flask dengan host 0.0.0.0 dan port dinamis untuk hosting (Render)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)