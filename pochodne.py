def derivs(stan, t):
    # funkcja która liczy pochodne w punkcie t0

    dydx = np.zeros_like(stan)  # tablica o nazwie dydx wypełniona zerami wielkości stan
    dydx[0] = stan[1]

    delta = stan[2] - stan[0]
    den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
    dydx[1] = ((M2 * L1 * stan[1] * stan[1] * sin(delta) * cos(delta)
                + M2 * G * sin(stan[2]) * cos(delta)
                + M2 * L2 * stan[3] * stan[3] * sin(delta)
                - (M1+M2) * G * sin(stan[0]))
               / den1)

    dydx[2] = stan[3]

    den2 = (L2/L1) * den1
    dydx[3] = ((- M2 * L2 * stan[3] * stan[3] * sin(delta) * cos(delta)
                + (M1+M2) * G * sin(stan[0]) * cos(delta)
                - (M1+M2) * L1 * stan[1] * stan[1] * sin(delta)
                - (M1+M2) * G * sin(stan[2]))
               / den2)

    return dydx