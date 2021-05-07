opcje_menu = ['Produkty','Ceny']
lista_produktow = ['czipsy','krakersy','cisteczka','paluszki']
cena_produktu = [1.20,1.80,2.50]


def wyswietl_menu():
    for index,opcja in enumerate(opcje_menu,1):
        print(f'{index}. {opcja}')


def wyswielt_produkty():
    for index,napoj in enumerate(lista_produktow,1):
        print(f'{index}. {napoj}')


def wyswietl_ceny():
    for index,cena in enumerate(cena_produktu,1):
        print(f'{index}. {cena}')

