import webbrowser
import time
from urllib.parse import urlparse

FILENAME = "Sites.txt"   # numele fișierului cu URL-uri
DELAY_BETWEEN = 0.5     # secunde între deschideri

def normalize(url: str) -> str | None:
    url = url.strip()
    if not url or url.startswith("#"):
        return None
    parsed = urlparse(url)
    if not parsed.scheme:
        # dacă lipsește schema (http/https) adaugă http://
        url = "http://" + url
    return url

def read_urls(filename: str):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            n = normalize(line)
            if n:
                yield n

def main():
    urls = list(read_urls(FILENAME))
    if not urls:
        print(f"Nu am găsit URL-uri în {FILENAME}.")
        return

    print(f"Deschid {len(urls)} site-uri în browserul implicit...")
    for u in urls:
        webbrowser.open_new_tab(u)
        time.sleep(DELAY_BETWEEN)

if __name__ == "__main__":
    main()

