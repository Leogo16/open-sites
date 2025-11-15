import json
import webbrowser
import time

FILENAME = "Sites.txt"   # fișierul JSON cu categorii
DELAY_BETWEEN = 0.5      # secunde între deschideri

def load_sites(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)  # citește JSON-ul ca dict
    return data

def main():
    data = load_sites(FILENAME)

    # Afișăm categoriile
    print("Categorii disponibile:")
    for category in data.keys():
        print(f" - {category}")

    # Alegem categoria
    chosen = input("Alege categoria: ").strip()

    if chosen not in data:
        print("Categoria nu există!")
        return

    urls = data[chosen]

    print(f"Deschid {len(urls)} site-uri din categoria '{chosen}'...")

    for u in urls:
        webbrowser.open_new_tab(u)
        time.sleep(DELAY_BETWEEN)

if __name__ == "__main__":
    main()


