import requests
from bs4 import BeautifulSoup

APTEKI = [
    {"name": "Ziko", "url": "https://www.e-zikoapteka.pl/{},n.html", "product_selector": 'meta[itemprop="name"]', "price_selector": "span.price-value"},
    {"name": "Lek24", "url": "https://www.lek24.pl/?name={}", "product_selector": "a.product-name-link", "price_selector": "span.price-value"},
    {"name": "Cefarm24", "url": "https://www.cefarm24.pl/{},n.html", "product_selector": 'header[itemprop="name"]', "price_selector": "span.promo"},
]

def scraper(nazwa_leku: str):
    results = []
    for apteka in APTEKI:
        url = apteka["url"].format(nazwa_leku)
        try:
            r = requests.get(url, timeout=5)
            r.raise_for_status()
            soup = BeautifulSoup(r.text, "html.parser")
            product = soup.select(apteka["product_selector"])
            if len(product) >= 2:
                Nazwa = product[1].get("content") or product[1].get("title") or product[1].get_text(strip=True)
                price_el = soup.select_one(apteka["price_selector"])
                if price_el:
                    price_text = price_el.get_text(strip=True).replace("zł", "").replace(",", ".")
                    results.append([apteka["name"], Nazwa, float(price_text)])
        except Exception as e:
            print(f"Błąd przy {apteka['name']}: {e}")
    return results
