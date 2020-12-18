# początowa inicjalizacja wartosci wahadła
G = 0.000000000066743  # stała grawitacji
n_p = 0 # numer planety (2)
n_w = 0 # numer wyboru

try:

    print("1. WYybór planety")
    print("2. Kreator tworzenia własnej planety")
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
        print("1. Merkury")
        print("2. Wenus")
        print("3. Ziemia")
        print("4. Mars")
        print("5. Jowisz")
        print("6. Saturn")
        print("7. Uran")
        print("8. Neptun")
        n_p = float(input("Twój wybór: "))
    elif n_w==2:
        print("Kreator własnej planety: ")
        M = float(input(
        "Wpisz masę planety na której ma działać wahadło(jako wielokrotność masy ziemi): "))  # masa planety do wyboru
        M = M * 5 * 10 ** 24
        R = float(input("Wpisz promień planety na której ma działać wahadło(w km): "))  # promień planety do wyboru
        R = R * 1000
        G1 = 10  # przyspieszenie , które będzie można wybrać z kilku dostępnych
        G2 = M * G1 / R ** 2  # przyspieszenie z, które będzie policzone po podaniu
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



