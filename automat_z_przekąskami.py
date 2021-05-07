from menu_automatu import wyswietl_menu,wyswielt_produkty,wyswietl_ceny
from formy_platnosci import platnosc_blik

def menu():
    wyswietl_menu()
    opcja = input('Wybierz opcje: ')
    if opcja == '1':
        wyswielt_produkty()
        platnosci()
    elif opcja == '2':
        wyswietl_ceny()


def platnosci():
    if wybrana_platnosc == '1':
        platnosc_blik()
    elif wybrana_platnosc == '2':
        platnosc_karta()