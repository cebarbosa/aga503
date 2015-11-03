# -*- coding: utf-8 -*-
"""

Created on 01/11/15

@author: Carlos Eduardo Barbosa

"""

import numpy as np

class GaussSeidel():
    def __init__(self, a, b, x0, maxit=100, tol=1e-5):
        """ Class for calculation of a linear system using the Gauss-Seidel
            method. """
        self.a = a
        self.b = b
        self.x0 = x0
        self.tol = tol
        self.maxit = maxit
        self.check_lines()
        self.check_sassenfeld()

    def check_lines(self):
        self.has_dominant_diag = True
        for i in range(len(self.b)):
            if 2 * np.abs(self.a[i,i]) <  np.sum(np.abs(self.a[i])):
                self.has_dominant_diag = False
        print "Is the diagonal dominant: ", self.has_dominant_diag

    def check_sassenfeld(self):
        self.beta = np.zeros_like(self.x0)
        for i in range(len(self.x0)):
            self.beta[i] = (np.sum(np.abs(self.a[i,:i])) + \
                            np.sum(np.abs(self.a[i,i+1:]))) / \
                           np.abs(self.a[i,i])
        self.pass_sassenfeld =  self.beta.max() < 1.
        return

    def solve(self):
        """ Calculate the solution. """
        xn = np.zeros_like(self.x0)
        xp = np.copy(self.x0)
        self.niter = 0
        for iter in range(self.maxit):
            self.niter += 1
            for i in np.arange(len(self.x0)):
                xn[i] = -(-self.b[i] + \
                              np.sum(self.a[i,i+1:] * xp[i+1:]) + \
                              np.sum(self.a[i,:i] * xn[:i])) / self.a[i,i]
            if np.abs(xn - xp).max() < self.tol:
                self.sol = xn
                break
            else:
                xp = xn
                xn = np.zeros_like(self.x0)
        return


if __name__ == "__main__":
    A = np.array([[10, -2, -2, 1],
                  [-2, 5, -1, -1],
                  [1, 0.5, -6, 1],
                  [-1, -1, 0, 20]])
    b = np.array([3., 5, -9, 17])
    x0 = np.array([100., 100, 100, 100])
    M = GaussSeidel(A, b, x0)
    M.solve()
    print "Solucao: ", M.sol