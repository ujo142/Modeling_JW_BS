import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import os
from matplotlib.patches import Circle
from scipy.integrate import odeint
from Powitanie import *
from pozegnanie import *
from pochodne import *
import matplotlib.animation as animation
import scipy.integrate as integratefrom
from numpy import sin, cos










#######################################################
##              Informacje o wahadła                 ##
#######################################################

G = 0.000000000066743  # stała grawitacji
M = 0.0
R = 0.0
G1 = 10  # przyspieszenie ziemskie
G2 = M*G/R**2  # przyspieszenie dowolne, które będzie policzone po podaniu
L1 = 0.0
L2 = 0.0
M1 = 0.0
M2 = 0.0

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