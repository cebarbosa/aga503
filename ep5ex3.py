# -*- coding: utf-8 -*-
"""

Created on 12/12/15

@author: Carlos Eduardo Barbosa

Solution for exercise 3

"""
import numpy as np
import matplotlib.pyplot as plt

from ep4 import planck

def simpson(f, x0, x1, eps=0.005, maxit=20, full_output=False,
             dtype=np.float64):
    x = np.array([x0, x1], dtype=dtype)
    y = np.array([f(x0), f(x1)], dtype=dtype)
    h = x[1] - x[0]
    trap0 = 0.5 * h * np.sum((y[:-1] + np.roll(y,-1)[:-1]))
    simp0 = trap0
    for k in np.arange(1, maxit+1):
        h = (x[-1] - x[0]) / 2**k
        x = np.linspace(x[0], x[-1], 2**(k)+1)
        n_interv = len(x) - 1
        y = np.repeat(y, 2)[:-1]
        y[1::2] = f(x[1::2])
        trap = 0.5 * h * np.sum((y[:-1] + np.roll(y,-1)[:-1]))
        # Correction for Simpson Rule
        simp = trap + (trap - trap0) / 3.
        error = np.abs((simp - simp0)/simp)
        if error < eps:
            break
        trap0 = trap
        simp0 = simp
    if full_output:
        return trap, n_interv
    return trap

if __name__ == "__main__":
    f = lambda a: planck(a, 2500.)
    epsilons = np.power(10, np.arange(-2., -11, -1))
    nint_double = np.zeros_like(epsilons)
    nint_single = np.zeros_like(epsilons)
    for i, eps in enumerate(epsilons):
        print i
        F, nint_double[i] = simpson(f, 5000., 100000., full_output=1, eps=eps)
        F, nint_single[i] = simpson(f, 5000., 100000., full_output=1, eps=eps,
                                     dtype=np.float32)
    plt.loglog(nint_double, epsilons, "ok", label="Double precision")
    plt.loglog(nint_single, epsilons, "xr", ms=8, label="Single precision")
    plt.loglog(nint_double, 2**15 * nint_double**-4., "--k", ms=8,
               label="$\propto 1 / {N^4}$")
    plt.axvline(2**20, ls="--", label="Maximum number of iteractions allowed")
    plt.legend(loc=1, prop={'size':12})
    plt.ylabel(r"$\varepsilon$")
    plt.xlabel(r"Number of intervals")
    plt.grid()
    plt.savefig("ep5ex3.png")
    plt.show(block=1)
