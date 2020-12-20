# początowa inicjalizacja wartosci wahadła

G = 0.000000000066743  # stała grawitacji
n_p = 0 # numer planety (2)
n_w = 0 # numer wyboru  (1)

try:
    print("Pora zdecydować w jakich warunkach wahadło zostanie zasymulowane")
    print(" ")
    print("1. Ziemia")
    print("2. Dowolna planeta, ten wybór przeniesie Cie do kreatora planty")
    print("")
    n_w = int(input("Twój wybór: "))

    M=1
    M2=1
    R=1
    G1=1
    G2=1
    L1=1
    L2=1
    M1=1
    if n_w==1:
        print("Wybierz jedną z planet podając numer planety.")

        n_p = float(input("Twój wybór: "))
    elif n_w==2:
        print("Kreator własnej planety: ")
        M = (float(input("Wpisz masę planety na której ma działać wahadło(jako wielokrotność masy ziemi): ")))*5*(10**24)  # masa planety do wyboru

        R = (float(input("Wpisz promień planety na której ma działać wahadło(w km): ")))*1000 # promień planety do wyboru

        G1 = 10  # przyspieszenie , które będzie można wybrać z kilku dostępnych
        G2 = (M * G) / (R**2)  # przyspieszenie z, które będzie policzone po podaniu
        L1 = float(input("Wpisz długość pierwszej części wahadła: "))  # długość pierwszej części wahadła
        L2 = float(input("Wpisz długość drugiej części wahadła: "))  # długość drugiej części wahadła
        M1 = float(input("Wpisz masę pierwszej części wahadła: "))  # masa pierwszej części wahadła
        M2 = float(input("Wpisz masę drugiej części wahadła: "))  # masa drugiej części wahadła

except IOError:                                             # Trzeba dopisywać na bierząco wyjątki
    print('Błąd odczytu danych lub plik nie istnieje')      # Tutaj również trzeba będzie zmieniać na bierząco
except NameError:
    print("Wykryto błąd!")
except ZeroDivisionError:
    print("divide by zero")



