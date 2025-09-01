import pandas as pd
from scrapery import scraper
from urllib.parse import quote

def main(nazwa_leku: str):
    data = scraper(nazwa_leku)
    df = pd.DataFrame(data, columns=["Apteka", "Lek", "Cena"])

    if not df.empty:
        print("\n=== Porównanie cen ===")
        print(df.to_string(index=False))
        cheapest = df.loc[df["Cena"].idxmin()]
        print(f"\nNajtańsza opcja: {cheapest['Apteka']} ({cheapest['Cena']:.2f} zł)")
        avg = df["Cena"].mean()
        std = df["Cena"].std()
        print(f"\nŚrednia cena: {avg:.2f} zł")
        print(f"Odchylenie standardowe: {std:.2f} zł")
    else:
        print("Brak wyników dla podanego leku")

if __name__ == "__main__":
    lek = input("Podaj nazwę leku: ").strip()
    main(quote(lek))  # bezpieczne do URL
