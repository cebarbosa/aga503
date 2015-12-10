# -*- coding: utf-8 -*-
"""

Created on 05/11/15

@author: Carlos Eduardo Barbosa

Resposta do exercicio 4

"""
import os

import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

def planck(wave, temp):
    """ Returns the Planck's Law intensities.

    Wavelengths are in Angstroms
    Temperatures in K.

    Output is converted to ergs/cm2/s/A to reproduce IDL version."""
    w = wave * 1.e-8 # Convertion to cm
    B = 2 * h * c * c * np.power(w, -5) / (np.exp(h * c / (w * k * temp)) - 1.)
    # Returns Planck's Law in units of ergs/cm2/s/A
    return np.pi * B * 1e-8

def model(wave, T1, T2):
    return planck(wave, T1) / (sigma * T1 * T1 * T1 * T1) + \
           planck(wave, T2) / (sigma * T2 * T2 * T2 * T2)

def chi2(wave, flux, err, T1, T2):
    """ Return the Chi2 map. """
    chi2map = np.zeros_like(T1)
    for w,f,e in zip(wave,flux,err):
        chi2map += np.power((f - model(w, T1, T2)) / e, 2.)
    return chi2map / (len(wave) - 1)

if __name__ == "__main__":
    ## Physical constants ####################################################
    k = 1.380658e-16 # Boltzmann constant in erg / K
    h = 6.6260755e-27 # Planck constant in erg / s
    c = 2.99792458e10 # Speed of light in cm / s
    sigma = 5.670367e-5 # Stefan-Boltzman constant in erg / cm2 / s / K4
    ##########################################################################
    table = "/home/kadu/Dropbox/aga503/ep4/dados_vinicius.txt"
    wave, flux, err = np.loadtxt(table).T
    ##########################################################################
    # fig1 = plt.figure(1)
    # ax1 = plt.subplot(211)
    # ax1.errorbar(wave, flux, yerr=err)
    # ax1.minorticks_on()
    # plt.pause(0.001)
    ##########################################################################
    t1 = np.linspace(3000, 6000., 100)
    t2 = np.linspace(700, 1000., 100)
    # t1 = np.linspace(5100, 5150., 100)
    # t2 = np.linspace(100, 1000., 100)
    T1, T2 = np.meshgrid(t1,t2)
    # fig3 = plt.figure(3)
    # plt.imshow(np.sqrt(T1**2 + T2**2), origin="bottom")
    # plt.colorbar()
    fig2 = plt.figure(2)
    plt.minorticks_on()
    map = chi2(wave, flux, err, T1, T2)
    print map.min(), map.max()
    # map = np.clip(map, map.min(), 10* map.min())
    idx =np.where(map == map.min())[0]
    plt.imshow(map, origin="bottom", extent=[t1[0], t1[-1], t2[0], t2[-1]],
               aspect="auto", vmin=1, vmax=5)
    plt.xlabel(r"$T_1$ [K]")
    plt.ylabel(r"$T_2$ [K]")
    plt.colorbar(label=r"$\chi^2_\nu$")
    plt.tight_layout()
    plt.savefig("chi2.png")
    plt.show(block=1)



