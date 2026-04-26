import requests
import hashlib
from datetime import datetime

def generate_id(source, identifier):
    return hashlib.sha1(f"{source}|{identifier}".encode()).hexdigest()

def get_iso_utc():
    return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

# API 1: NEWS API (Teknologi)
def fetch_news_api(api_key):
    url = f"https://newsapi.org/v2/everything?q=teknologi&language=id&pageSize=4&apiKey={api_key}"
    try:
        resp = requests.get(url).json()
        articles = resp.get('articles', [])
        return [{
            "_id": generate_id("news_api", a['url']),
            "src": "news_api", "fmt": "json", "ts": a['publishedAt'] or get_iso_utc(),
            "title": a['title'], "text": a['description'] or "No Content", "entities": ["Berita", "Tech"],
            "kv": {"url": a['url'], "source": a['source']['name']}
        } for a in articles]
    except: return []

# API 2: CRYPTO API (CoinGecko)
def fetch_crypto_api():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=id&per_page=4"
    try:
        resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).json()
        return [{
            "_id": generate_id("crypto_api", c.get('id')),
            "src": "crypto_api", "fmt": "json", "ts": get_iso_utc(),
            "title": f"Harga {c.get('name')}", "text": f"Symbol: {c.get('symbol').upper()}",
            "entities": ["Crypto", c.get('name')],
            "kv": {"price": c.get('current_price'), "rank": c.get('market_cap_rank')}
        } for c in resp]
    except: return []

# API 3: EXCHANGE RATE (Kurs IDR)
def fetch_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/IDR"
    try:
        resp = requests.get(url).json()
        rates = list(resp.get('rates', {}).items())[:4]
        return [{
            "_id": generate_id("exchange_api", curr),
            "src": "exchange_api", "fmt": "json", "ts": get_iso_utc(),
            "title": f"Kurs IDR ke {curr}", "text": f"Nilai: {val}",
            "entities": ["Finance", curr],
            "kv": {"rate": val, "base": "IDR"}
        } for curr, val in rates]
    except: return []

# API 4: WEATHER API (Cuaca Surabaya)
def fetch_weather_api():
    url = "https://api.open-meteo.com/v1/forecast?latitude=-7.24&longitude=112.75&current_weather=true"
    try:
        resp = requests.get(url).json()
        curr = resp['current_weather']
        return [{
            "_id": generate_id("weather_api", "sub_current"),
            "src": "weather_api", "fmt": "json", "ts": get_iso_utc(),
            "title": "Cuaca Surabaya Hari Ini", "text": f"Suhu: {curr['temperature']}C",
            "entities": ["Weather", "Surabaya"],
            "kv": {"temp": curr['temperature'], "wind": curr['windspeed']}
        }]
    except: return []