import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import os
from matplotlib.patches import Circle
from scipy.integrate import odeint
from Powitanie import *
from pozegnanie import *
import matplotlib.animation as animation
import scipy.integrate as integrate
from numpy import sin, cos
from control.phaseplot import phase_plot

powitanie()

from POU import *

# czas
dt = 0.05  # Interwał czasowy / ilość fps gdy wyświetliny wahadło
t = np.arange(0, 30, dt)  # Przestrzeń czasu T |--> R, gdzie R to przestrzeń położeń


#######################################################
##              Liczenie pochodnych                  ##
#######################################################



# czas
dt = 0.005  # Interwał czasowy / ilość fps gdy wyświetliny wahadło
t = np.arange(0, 30, dt)  # Przestrzeń czasu T |--> R, gdzie R to przestrzeń położeń


# warunki brzegowe ruchu
alfa_1 = 120.0  # początkowy kąt odchylenia pierwszej masy wahadła
omega_1 = 0.0  # początkowa wartość prędkości kątowej dla pierwszej części wahadła
alfa_2 = -10.0  # początkowy kąt odchylenia drugiej masy wahadła
omega_2 = 0.0  # początkowa wartość prędkości kątowej dla drugiej części wahadła


# stan początkowy
stan_p = np.radians([alfa_1, omega_1, alfa_2, omega_2])   # stan początkowy wahadła

def derywata(stan_p, t):
    # funkcja która liczy pochodne w punkcie t0

    dydx = np.zeros_like(stan_p)  # tablica o nazwie dydx wypełniona zerami wielkości stan
    dydx[0] = stan_p[1]

    delta = stan_p[2] - stan_p[0]
    den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
    dydx[1] = ((M2 * L1 * stan_p[1] * stan_p[1] * sin(delta) * cos(delta)
                + M2 * G2 * sin(stan_p[2]) * cos(delta)
                + M2 * L2 * stan_p[3] * stan_p[3] * sin(delta)
                - (M1+M2) * G2 * sin(stan_p[0]))
               / den1)

    dydx[2] = stan_p[3]

    den2 = (L2/L1) * den1
    dydx[3] = ((- M2 * L2 * stan_p[3] * stan_p[3] * sin(delta) * cos(delta)
                + (M1+M2) * G2 * sin(stan_p[0]) * cos(delta)
                - (M1+M2) * L1 * stan_p[1] * stan_p[1] * sin(delta)
                - (M1+M2) * G2 * sin(stan_p[2]))
               / den2)

    return dydx
# rozwiazania równań ruchu
y = integrate.odeint(derywata, stan_p, t)

# zdefiniowanie współrzędnych punktów materialnych
x1 = L1*sin(y[:, 0])
x2 = L2*sin(y[:, 2]) + x1

y1 = -L1*cos(y[:, 0])
y2 = -L2*cos(y[:, 2]) + y1



# tworzenie wykresu
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-5, 5), ylim=(-5, 5))
ax.set_aspect('equal')
ax.grid()

# grubosc wykresu
line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

# wgranie animacji
def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*dt))
    return line, time_text

# wyłączenie siatki wsp i dodanie tła
ax.grid(False)
img = plt.imread("earth.png")
ax.imshow(img, extent=[-5, 5, -5, 5])

# sama animacja, interwały czasowe(pm)
ani = animation.FuncAnimation(fig, animate, range(1, len(y)),
                              interval=dt*1000, blit=True, init_func=init)

# wyświetlenie wykresu
plt.show()


pozegnanie()