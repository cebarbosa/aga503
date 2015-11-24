# -*- coding: utf-8 -*-
"""

Created on 24/11/15

@author: Carlos Eduardo Barbosa

Solution for exercise 4 of activity 3.

"""
import numpy as np

from ep2ex1 import GaussElimination

class chi2_minimization():
    """ Calculate coefficients for linear combination of functions that
        minimize the chi^2. """
    def __init__(self, x, y, fs):
        self.x = x
        self.y = y
        self.fs = fs
        self.dim = len(fs)
        self.make_system()
        self.M = GaussElimination(self.A, self.b)
        self.M.solve()
        self.sol = self.M.sol

    def make_system(self):
        """ Calculate the least square standard system"""
        fx  = np.zeros((self.dim, len(self.x)))
        self.b = np.zeros((self.dim))
        for i in range(self.dim):
            fx[i] = self.fs[i](self.x)
            self.b[i] = np.sum(self.fs[i](self.x) * self.y)
        self.A = np.dot(fx, fx.T)

if __name__ == "__main__":
    x = np.arange(11)
    y = np.array([2.6, 0.35, -7.2, -21, -30, -60, -91, -127, -165, -213, -264])
    f1 = lambda x: 1
    f2 = lambda x: x
    f3 = lambda x: x * x
    chi2 = chi2_minimization(x, y, [f1, f2, f3])
    print "The solution of the system in the following: "
    print chi2.sol


