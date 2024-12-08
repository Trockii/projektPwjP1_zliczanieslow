# Import polskich znaków w konsoli
import sys
import codecs
import re

sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

# Tworzenie zmiennych
try:
    tekst = open("tekst.txt", "r", encoding="utf-8")  # Połączenie tekstu zewnętrznego
    zawartosc = tekst.read().lower()  # Odczytanie i zamiana tekstu na małe litery
    zawartosc = re.sub(r'[^\w\s]', '', zawartosc)  # Usunięcie znaków specjalnych
    slowa = zawartosc.split()  # Rozdzielanie słów
except FileNotFoundError:
    print("Błąd: Plik 'tekst.txt' nie został znaleziony.")
    sys.exit()

# Dodawanie licznika do każdego słowa
licznik = {}
for slowo in slowa:
    if slowo in licznik:
        licznik[slowo] += 1
    else:
        licznik[slowo] = 1

# Funkcja wyświetlająca łączną liczbę słów w pliku
def laczna_liczba_slow():
    print(f"Łączna liczba słów w pliku: {len(slowa)}")

# Funkcja wyszukiwania słowa
def szukaj_slowo():
    while True:
        szukane_slowo = input("Wpisz słowo (lub wpisz 'exit', aby zakończyć): ").strip()
        if szukane_slowo.lower() == 'exit':
            print("Koniec programu. Dziękujemy!")
            break
        if szukane_slowo in licznik:
            print(f"Słowo '{szukane_slowo}' występuje {licznik[szukane_slowo]} razy.")
            eksport_do_pliku(szukane_slowo)
        else:
            print(f"Niestety słowo '{szukane_slowo}' nie występuje w tekście.")
            eksport_do_pliku(szukane_slowo)

# Funkcja wyświetlająca najczęściej występujące słowo
def najczestsze_slowo():
    if licznik:  # Sprawdzamy, czy licznik nie jest pusty
        najczestsze = max(licznik.items(), key=lambda x: x[1])
        print(f"Najczęściej występujące słowo to '{najczestsze[0]}', które występuje {najczestsze[1]} razy.")
    else:
        print("Nie znaleziono słów w pliku.")

# Funkcja eksportująca wyniki do pliku
def eksport_do_pliku(szukane_slowo):
    with open("wyniki.txt", "w", encoding="utf-8") as plik:
        plik.write(f"Łączna liczba słów: {len(slowa)}\n")
        if licznik:
            najczestsze = max(licznik.items(), key=lambda x: x[1])
            plik.write(f"Najczęściej występujące słowo: '{najczestsze[0]}' ({najczestsze[1]} razy)\n")
        if szukane_slowo in licznik:
            plik.write(f"Wpisane przez ciebie słowo '{szukane_slowo}' padło {licznik[szukane_slowo]} razy.\n")
        else:
            plik.write(f"Wpisane przez ciebie słowo '{szukane_slowo}' nie występuje w tekście.\n")
    print("Wyniki zapisano do pliku 'wyniki.txt'.")

# Wywołanie funkcji
laczna_liczba_slow()      # Wyświetlenie liczby wszystkich słów w pliku
najczestsze_slowo()      # Wyświetlenie najczęściej występującego słowa
szukaj_slowo()           # Rozpoczęcie wyszukiwania słów