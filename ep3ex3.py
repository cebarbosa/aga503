# -*- coding: utf-8 -*-
"""

Created on 25/11/15

@author: Carlos Eduardo Barbosa

Prints the solution for the question 3.

"""
import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

if __name__ == "__main__":
    x = np.arange(1.,7)
    y = np.array([-3, -0.5, -1., 0., 0.5, 1.])
    l = lagrange(x,y)
    l1 = lagrange(x[1:4], y[1:4])
    l2 = lagrange(x[2:5], y[2:5])
    plt.plot(x,y,"ok")
    plt.plot(np.linspace(1,6,50), l(np.linspace(1,6,50)), "--r")
    plt.plot(np.linspace(x[1],x[3],20), l1(np.linspace(x[1],x[3],20)), "--b")
    plt.plot(np.linspace(x[2],x[4],20), l2(np.linspace(x[2],x[4],20)), "--g")
    print l(3.2), l1(3.2), l2(3.2)
    plt.show()
