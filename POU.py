
print("Pora zdecydować w jakich warunkach wahadło zostanie zasymulowane")
print(" ")
print("1. Ziemia")
print("2. Genetycznie zmodyfikowana ziemia, ten wybór przeniesie Cie do kreatora planty")
print("")
n_w = int(input("Twój wybór: "))

if n_w==1:
    print("Wybrałeś naszą rodzimą ziemie!")
    M = 5*(10**24)
    M1 = float(input("Wpisz masę pierwszej części wahadła: "))  # masa pierwszej części wahadła
    M2 = float(input("Wpisz masę drugiej części wahadła: "))  # masa drugiej części wahadła
    R = 6371000
    G2 = 9.81
    G1 =9.81
    L1 = float(input("Wpisz długość pierwszej części wahadła: "))  # długość pierwszej części wahadła
    L2 = float(input("Wpisz długość drugiej części wahadła: "))  # długość drugiej części wahadła
    z=1
elif n_w==2:
    print("Kreator zmodyfikowanej ziemi: ")
    M = (float(input("Wpisz masę zmodyfikowanej ziemi (jako wielokrotność masy rzeczywistej ziemi): ")))*5*(10**24)  # masa planety do wyboru
    R = (float(input("Wpisz promień zmodyfikowanej ziemi (w km): ")))*1000 # promień planety do wyboru
    G= 6.67*(1/(10**11))
    G1 = 9.8  # przyspieszenie , które będzie można wybrać z kilku dostępnych
    G2 = (M * G) / (R**2)  # przyspieszenie z, które będzie policzone po podaniu
    L1 = float(input("Wpisz długość pierwszej części wahadła: "))  # długość pierwszej części wahadła
    L2 = float(input("Wpisz długość drugiej części wahadła: "))  # długość drugiej części wahadła
    M1 = float(input("Wpisz masę pierwszej części wahadła: "))  # masa pierwszej części wahadła
    M2 = float(input("Wpisz masę drugiej części wahadła: "))  # masa drugiej części wahadła
    z=1

