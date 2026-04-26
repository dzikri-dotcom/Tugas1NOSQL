# 📊 Big Data Management System: Integrated Crawler & Dashboard

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/Database-MongoDB-green.svg)](https://www.mongodb.com/)
[![Docker](https://img.shields.io/badge/Container-Docker-blue.svg)](https://www.docker.com/)

Sistem pengelolaan Big Data otomatis yang melakukan *scraping* berita (Detik News) dan konsumsi API (DummyJSON) secara berkala, menyimpannya ke database NoSQL MongoDB, dan menyajikannya melalui dashboard web interaktif berbasis Flask.

---

## 👥 Anggota Kelompok (IS-06-02)
- **Farrel Mario Prasetyo** (1204230049) 
- **Dzikri Lathiful Qodim** (1204230102) 
- **Ahmad Zaki** 

---

## 🚀 Fitur Utama
- **Automated Ingestion:** Penarikan data otomatis setiap 5 menit menggunakan Python Threading.
- **NoSQL Persistence:** Penyimpanan data fleksibel menggunakan MongoDB.
- **Search Engine:** Optimasi pencarian kata kunci menggunakan *Text Indexing* pada database.
- **Modern UI:** Dashboard responsif dengan tipografi Plus Jakarta Sans.
- **Dockerized:** Lingkungan database yang terisolasi menggunakan Docker Compose.

---
## 📂 Struktur Folder
```text
Tugas1NOSQL/
└── tugas1_nosql/
    ├── main.py              # Logic Flask & Background Crawler
    ├── docker-compose.yml   # Konfigurasi MongoDB
    ├── requirements.txt     # Dependensi Library
    ├── templates/           # Frontend (HTML)
    └── static/              # Aset Visual (CSS/JS)

1. **Clone Repository**
   ```bash
   git clone [https://github.com/dzikri-dotcom/Tugas1NOSQL.git](https://github.com/dzikri-dotcom/Tugas1NOSQL.git)
