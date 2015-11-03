# -*- coding: utf-8 -*-
"""

Created on 12/10/15

@author: Carlos Eduardo Barbosa

"""

import math


def Blamb(lamb, T):
    """ Blackbody function (Planck's law) for a given wavelenght and
    temperaturein CGS units. """
    h = 6.6260755e-27 # erg s
    c = 2.99792458e10 # cm / s
    k = 1.380658e-16 # erg / k
    return 2. * h * c * c / math.pow(lamb, 5) / \
           (math.exp(h * c / k / lamb / T) - 1.) # erg / s / cm**3

def f(n):
    """ Function that we want to find the root. """
    JmK = 0.8
    Rsun = 6.955e+10
    R = 20 * Rsun# Solar radius
    Teff = 2000 # K
    Ri = 100 * Rsun # Rsol
    Re = 1200 * Rsun # Rsol
    a = 0.25e-4 # centimeter
    Tdust = 600 # K
    J = 1.6e-4 # centimeter
    K = 2.2e-4 # centimeter
    num = R**2 * Blamb(J, Teff) + (4 * math.pi * a**2 / 3) * (Re**3 - Ri**3) \
                                  * Blamb(J, Tdust) * n
    den = R**2 * Blamb(K, Teff) + (4 * math.pi * a**2 / 3) * (Re**3 - Ri**3) \
                                  * Blamb(K, Tdust) * n
    return JmK + 2.5 * math.log10(num / den)

def biseccao(f, x1, x2, tol=0.00001):
    eps = 1.
    while eps > tol:
        xm = 0.5 * (x1 + x2)
        f1 = f(x1)
        fm = f(xm)
        eps = abs(2. * (x1 - x2) / (x2 + x2))
        if f1 * fm < 0.:
            x2 = xm
        else:
            x1 = xm
    x = 0.5 * (x1 + x2)
    return x




if __name__ == "__main__":
    print f(0), f(0.0001)
    n = biseccao(f, 0, 0.0001)
    print "Densidade numerica de graos (cm**-3); ", n
    print "Densidade numerica de graos (m**-3); ", n * 1e6

