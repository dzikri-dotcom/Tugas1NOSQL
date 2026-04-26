from bs4 import BeautifulSoup
import requests
import hashlib
from datetime import datetime

def scrape_base(url, src, selector, title_tag, limit=2):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.select(selector)[:limit]
        docs = []
        for item in items:
            link_tag = item.find('a')
            if not link_tag or not link_tag.get('href'): continue
            link = link_tag['href']
            title = item.find(title_tag).get_text(strip=True)
            docs.append({
                "_id": hashlib.sha1(f"{src}|{link}".encode()).hexdigest(),
                "src": src, "fmt": "html", "ts": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
                "title": title, "text": f"Berita terkini dari {src}",
                "entities": ["Web", src.replace('_site','').capitalize()],
                "kv": {"url": link}
            })
        return docs
    except: return []

def scrape_detik(): return scrape_base("https://www.detik.com/terpopuler", "detik_site", "article", "h3")
def scrape_cnbc(): return scrape_base("https://www.cnbcindonesia.com/news", "cnbc_site", "article", "h2")
def scrape_kompas(): return scrape_base("https://www.kompas.com/", "kompas_site", ".article__list", "h3")
def scrape_tempo(): return scrape_base("https://www.tempo.co/", "tempo_site", ".card-box", "h2")