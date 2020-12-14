import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import os
from matplotlib.patches import Circle
from scipy.integrate import odeint
from Powitanie import *
from pozegnanie import *
import POU
import matplotlib.animation as animation
import scipy.integrate as integrate
from numpy import sin, cos







#######################################################
##              Liczenie pochodnych                  ##
#######################################################

def derywata(stan_p, t):
    # funkcja która liczy pochodne w punkcie t0

    dydx = np.zeros_like(stan_p)  # tablica o nazwie dydx wypełniona zerami wielkości stan
    dydx[0] = stan_p[1]

    delta = stan_p[2] - stan_p[0]
    den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
    dydx[1] = ((M2 * L1 * stan_p[1] * stan_p[1] * sin(delta) * cos(delta)
                + M2 * G * sin(stan_p[2]) * cos(delta)
                + M2 * L2 * stan_p[3] * stan_p[3] * sin(delta)
                - (M1+M2) * G * sin(stan_p[0]))
               / den1)

    dydx[2] = stan_p[3]

    den2 = (L2/L1) * den1
    dydx[3] = ((- M2 * L2 * stan_p[3] * stan_p[3] * sin(delta) * cos(delta)
                + (M1+M2) * G * sin(stan_p[0]) * cos(delta)
                - (M1+M2) * L1 * stan_p[1] * stan_p[1] * sin(delta)
                - (M1+M2) * G * sin(stan_p[2]))
               / den2)

    return dydx


#######################################################
##              Informacje o wahadła                 ##
#######################################################
G = 0.000000000066743  # stała grawitacji
M = 0.01
R = 0.01
G1 = 10  # przyspieszenie ziemskie
G2 = M*G/R**2  # przyspieszenie dowolne, które będzie policzone po podaniu
L1 = 0.01
L2 = 0.01
M1 = 0.01
M2 = 0.01

# czas
dt = 0.05  # Interwał czasowy / ilość fps gdy wyświetliny wahadło
t = np.arange(0, 30, dt)  # Przestrzeń czasu T |--> R, gdzie R to przestrzeń położeń


# warunki brzegowe ruchu
alfa_1 = 120.0  # początkowy kąt odchylenia pierwszej masy wahadła
omega_1 = 0.0  # początkowa wartość prędkości kątowej dla pierwszej części wahadła
alfa_2 = -10.0  # początkowy kąt odchylenia drugiej masy wahadła
omega_2 = 0.0  # początkowa wartość prędkości kątowej dla drugiej części wahadła


# stan początkowy
stan_p = np.radians([alfa_1, omega_1, alfa_2, omega_2])   # stan początkowy wahadła

# rozwiazania równań ruchu
y = integrate.odeint(derywata, stan_p, t)


#######################################################
##              Rdzeń programu                       ##
#######################################################

try:
    powitanie()
    # tu bedzie POU / pobieranie danych do wahadła oba typy 1 i 2
except IOError:                                             # Trzeba dopisywać na bierząco wyjątki
    print('Błąd odczytu danych lub plik nie istnieje')      # Tutaj również trzeba będzie zmieniać na bierząco







##############  Fragment do wyplucia danych o wahadłe  ###################





##############  Fragment do wyświetlenia animacji / portretu fazowego ####





##############  Fragment do siema / elo   ################################
pozegnanie()