# 📊 Big Data Management System: Integrated Crawler & Dashboard

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/Database-MongoDB-green.svg)](https://www.mongodb.com/)
[![Docker](https://img.shields.io/badge/Container-Docker-blue.svg)](https://www.docker.com/)

Sistem pengelolaan Big Data otomatis yang dirancang untuk melakukan ingesti data dari berbagai sumber (Multi-source Ingestion), mencakup teknik Web Scraping pada portal berita nasional dan konsumsi REST API secara berkala. Seluruh data diintegrasikan ke dalam database NoSQL MongoDB dan disajikan melalui dashboard web interaktif berbasis Flask yang dilengkapi dengan fitur pencarian cepat.

---

## 👥 Anggota Kelompok (IS-06-02)
- **Farrel Mario Prasetyo** (1204230049) 
- **Dzikri Lathiful Qodim** (1204230102) 
- **Achmad Zaki** (1204230042)

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
├── scripts/
│   ├── api_collector.py     # Modul pengumpulan data via API
│   ├── web_scraper.py       # Modul scraping data dari portal berita
│   └── __init__.py          # Inisialisasi package Python
├── templates/
│   └── index.html           # Dashboard UI (Jinja2 Template)
├── Dockerfile               # Konfigurasi Docker Image
├── docker-compose.yml       # Konfigurasi MongoDB Container
├── main.py                  # Aplikasi Utama & Flask Server
├── README.md                # Dokumentasi Proyek
└── requirements.txt         # Daftar Library (Flask, Pymongo, dll)

1. **Clone Repository**
   ```bash
   git clone [https://github.com/dzikri-dotcom/Tugas1NOSQL.git](https://github.com/dzikri-dotcom/Tugas1NOSQL.git)
