opcje_platnosci = ['blik', 'karta', 'gotówka', 'drobne']
numery_blik  = ['228899', '990077']

def wyswietl_opcje():
    for opcje in enumerate(opcje_platnosci,1):
        print(f'{index}. {opcja}')


def platnosc_blik():
    wpisany_numer = input('wpisz kod blik: ')
    if wpisany_numer == numery_blik:
        print('tranzakcja zaakceptowana')
    else:
        print('wpisany numer jest nie poprawny proszę wpisań ponownie:')