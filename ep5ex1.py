# -*- coding: utf-8 -*-
"""

Created on 11/12/15

@author: Carlos Eduardo Barbosa

Solution for exercise 1 of EP 5

"""
import numpy as np

def ponto_medio(x,y):
    """ Calculate the integral of y in the interval given by x using the
        method of the mean point. """
    deltax = np.diff(x[:-1] + 0.5 * np.diff(x))
    first = 0.5 * (x[1] - x[0]) * y[0]
    last = 0.5 * (x[-1] - x[-2]) * y[-1]
    return np.sum(y[1:-1] * deltax) + first + last

if __name__ == "__main__":
    w, f = np.loadtxt("halpha.txt").T
    f0 = 1.
    W = ponto_medio(w, 1. - f / f0)
    print W



