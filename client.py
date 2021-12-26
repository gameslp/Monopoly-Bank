import requests
import time

def cls():
    print("\033[H\033[J", end="")
    print(""" __  __                               _       
|  \/  | ___  _ __   ___  _ __   ___ | |_   _ 
| |\/| |/ _ \| '_ \ / _ \| '_ \ / _ \| | | | |
| |  | | (_) | | | | (_) | |_) | (_) | | |_| |
|_|  |_|\___/|_| |_|\___/| .__/ \___/|_|\__, |
                         |_|            |___/ 
 _             __  __            _      _    
| |__  _   _  |  \/  | __ _  ___(_) ___| | __
| '_ \| | | | | |\/| |/ _` |/ __| |/ _ \ |/ /
| |_) | |_| | | |  | | (_| | (__| |  __/   < 
|_.__/ \__, | |_|  |_|\__,_|\___|_|\___|_|\_\\
       |___/     


""")


cls()

try:
    status = requests.get("http://interesti.com:2005//?czynnosc=ping")
    if (status.status_code==200): print("Połączono z serwerem ")
except:
    print("Serwer nieosiągalny...")
    time.sleep(3)
    quit()
print("1) Stwórz grę")
print("2) Dołącz do gry")
print("3) Dołącz do gry jako bank")

def bank(kod_gry):
    print(f"Kod gry: {kod_gry}")
    opcje = ["Zaplac", "Zapłać wszystkim", "Zabierz", "Zabierz wszystkim", "Wyswietl graczy"]
    for i, opcja in enumerate(opcje):
        print(f"{i + 1}) {opcja}")
    wybor = input(">")
    if (wybor == '1'):
        dla = input("Komu chcesz zapłacić: ")
        ile = input("Ile chcesz zapłacić: ")
        while (ile.isnumeric() != True):
            ile = input("Podaj liczbe: ")
        response = requests.get(f"http://interesti.com:2005//?czynnosc=zaplac&nazwa=bank&id_gry={kod_gry}&kto={dla}&ile={ile}")
        if (response.status_code == 200):
            print("Udało się!")
        else:
            print("Nie udało się")
    elif (wybor == '2'):
        ile = input("Ile chcesz zapłacić: ")
        response = requests.get(f"http://interesti.com:2005//?czynnosc=lista_graczy&id_gry={kod_gry}")
        lista_graczy = response.content.decode("utf-8").split('\n')
        for gracz in lista_graczy:
            if (gracz == ''): continue
            response = requests.get(f"http://interesti.com:2005//?czynnosc=zaplac&nazwa=bank&id_gry={kod_gry}&kto={gracz}&ile={ile}")
            if (response.status_code == 400):
                print("Coś nie działa...")
                input("Wcisnij Enter aby kontynuowac...")
                break
            else: print("Udało się ")
    elif (wybor == '3'):
        ile = input("Ile chcesz zabrac: ")
        kto = input("Komu chcesz zabrac: ")
        response = requests.get(f"http://interesti.com:2005//?czynnosc=zabierz&id_gry={kod_gry}&kto={kto}&ile={ile}")
        if (response.status_code == 200): print("Udało się")
        else: print("Gracz nie ma wystarczająco pieniędzy")
    elif (wybor == '4'):
        ile = input("Ile chcesz zabrac: ")
        response = requests.get(f"http://interesti.com:2005//?czynnosc=lista_graczy&id_gry={kod_gry}")
        lista_graczy = response.content.decode("utf-8").split('\n')
        for gracz in lista_graczy:
            if (gracz == ''): continue
            response = requests.get(f"http://interesti.com:2005//?czynnosc=zabierz&id_gry={kod_gry}&kto={gracz}&ile={ile}")
            if (response.status_code == 400):
                print("Coś nie działa...")
                input("Wcisnij Enter aby kontynuowac...")
                break
            else: print("Udało się ")
    elif (wybor == '5'):
        response = requests.get(f"http://interesti.com:2005//?czynnosc=lista_graczy&id_gry={kod_gry}")
        print(response.content.decode("utf-8"))
    input("Wcisnij Enter aby kontynuowac...")


def gra(nazwa, kod_gry, stan_konta):
    print(f"""Kod gry: {kod_gry}
Nazwa: {nazwa}
Stan konta: {stan_konta}""")
    opcje = ["Zaplac", "Zaplac do banku", "Stan Konta", "Wyswietl graczy"]
    for i, opcja in enumerate(opcje):
        print(f"{i + 1}) {opcja}")
    wybor = input(">")
    if (wybor == '1'):
        dla = input("Komu chcesz zapłacić: ")
        ile = input("Ile chcesz zapłacić: ")
        while (ile.isnumeric() != True):
            ile = input("Podaj liczbe: ")
        response = requests.get(f"http://interesti.com:2005//?czynnosc=zaplac&nazwa={nazwa}&id_gry={kod_gry}&kto={dla}&ile={ile}")
        if (response.status_code == 200):
            print("Udało się!")
        else:
            print("Nie udało się")
    elif (wybor == '2'):
        ile = input("Ile chcesz zapłacić: ")
        while (ile.isnumeric() != True):
            ile = input("Podaj liczbe: ")
        response = requests.get(f"http://interesti.com:2005//?czynnosc=zaplac&id_gry={kod_gry}&nazwa={nazwa}&ile={ile}&kto=bank")
        if (response.status_code == 200):
            print("Udało się!")
        else:
            print("Nie udało się")
    elif (wybor == '3'):
        response = requests.get(f"http://interesti.com:2005//?czynnosc=stan&id_gry={kod_gry}&nazwa={nazwa}")
        if (response.status_code == 200):
            print(f"Stan konta: {response.content.decode('utf-8')}")
        else: print("Nie udało się")
    elif (wybor == '4'):
        response = requests.get(f"http://interesti.com:2005//?czynnosc=lista_graczy&id_gry={kod_gry}")
        print(response.content.decode("utf-8"))
    input("Wcisnij Enter aby kontynuowac...")
wybor = input(">")

if (wybor == "1"):
    nazwa = input("Nick: ")
    while (nazwa.find(" ") > 0):
        print("Nazwa nie może zawierać spacji")
        nazwa = input("Nick: ")
    start = input("Ile pieniędzy gracz dostanie na start: ")
    while (start.isnumeric() == False):
        start = input("Podaj liczbę: ")
    kod_gry = requests.get(f"http://interesti.com:2005//?czynnosc=nowa_gra&nazwa={nazwa}&start={start}")
    kod_gry = kod_gry.content.decode("utf-8")
    print(f"Kod Gry: {kod_gry}")
    while True:
        cls()
        stan_konta = requests.get(f"http://interesti.com:2005//?czynnosc=stan&id_gry={kod_gry}&nazwa={nazwa}").content.decode("utf-8")
        gra(nazwa,kod_gry, stan_konta)
elif (wybor == "2"):
    nazwa = input("Nick: ")
    while (nazwa.find(" ") > 0):
        print("Nazwa nie może zawierać spacji")
        nazwa = input("Nick: ")
    kod_gry = input("Podaj kod gry: ")
    response = requests.get(f"http://interesti.com:2005//?czynnosc=dolacz&nazwa={nazwa}&id_gry={kod_gry}")
    if (response.status_code == 200):
        print("Udało się dołączyć")
    else: 
        print("Nie udało się dołączyć")
        quit()
    while True:
        cls()
        stan_konta = requests.get(f"http://interesti.com:2005//?czynnosc=stan&id_gry={kod_gry}&nazwa={nazwa}").content.decode("utf-8")
        gra(nazwa, kod_gry, stan_konta)
elif (wybor == "3"):
    nazwa = "bank"
    kod_gry = input("Podaj kod gry: ")
    response = requests.get(f"http://interesti.com:2005//?czynnosc=gra_istnieje&id_gry={kod_gry}")
    if response.status_code == 200: print("Połączono...")
    else: 
        print("Nie znaleziono gry...")
        quit()
    while True:
        cls()
        bank(kod_gry)