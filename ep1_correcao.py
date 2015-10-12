# -*- coding: utf-8 -*-
"""

Created on 12/10/15

@author: Carlos Eduardo Barbosa

Correção do EP 1
"""
import numpy as np

def ex2():
    # Solucao para o exercicio 2
    def calc_decimal(mantissa, potencia):
        val = 0
        for i,m in enumerate(mantissa):
            val += int(m) * (2 ** (-(i+1)))
        val *= 2 ** potencia
        return val
    print "Solucao do exercicio 2"
    x1 = calc_decimal("1011011011", 2)
    x2 = calc_decimal("1011011010", 2)
    print "a) x1 = {0}".format(x1)
    print "b) eps_m = {0}".format(abs(x1 - x2))
    return

def ex345(x0 = None):
    """ Solucao do exercicios 3 ao 5. x0 são os chutes iniciais."""
    if x0 == None:
        x0 = [1.01, 2.0, 1.01, 1.01, 1.0]
    tol = 0.0001 # precisao relativa
    print "Solucao para todos os problemas: {0:.5f} +/- {1:.5f}".format(np.sqrt(2),
                                                                tol / np.sqrt(2))
    print "Interacoes tem que parar no intervalo: [{0:.5f}, {1:.5f}]".format(
        np.sqrt(2) - tol / np.sqrt(2), np.sqrt(2) + tol / np.sqrt(2))
    ##########################################################################
    # Funcao a ser minimizada
    f = lambda x: np.log10(x * x - 1)
    ##########################################################################
    # Chutes iniciais
    x1 = x0[0]
    x2 = x0[1]
    eps = 1.
    nint = 0
    ##########################################################################
    # Resolvendo pelo método da biseccao mostrando os valores intermediarios
    print 70 * "=="
    print "Solucao do exercicio 3"
    print 70 * "=="
    header = ["x_a", "x_b", "x_m", "f(x_a)", "f(x_b)", "f(x_m)", "epsilon"]
    header = ["{0:20s}".format(x) for x in header]
    print "".join(header)
    while eps > tol:
        nint += 1
        xm = 0.5 * (x1 + x2)
        f1 = f(x1)
        f2 = f(x2)
        fm = f(xm)
        eps = abs(2. * (x1 - x2) / (x2 + x2))
        display = [x1, x2, xm, f1, f2, fm, eps]
        if f1 * fm < 0.:
            x2 = xm
        else:
            x1 = xm
        display = ["{0:20s}".format(str(y)) for y in display]
        print "".join(display)
    x = 0.5 * (x1 + x2)
    print "Raiz encontrada em x = {0:.5f} ({1} interacoes).".format(x, nint)
    ##########################################################################
    print 70 * "=="
    print "Solucao do exercicio 4"
    print 70 * "=="
    # Defining the derivative of the function
    flinha = lambda x: 2. * x / (np.log(10.) * (x * x - 1.))
    ##########################################################################
    # Chutes iniciais (redefinindo)
    eps = 1.
    nint = 0
    x = x0[2]
    header = ["x", "f(x)", "f'(x)", "delta", "epsilon"]
    header = ["{0:20s}".format(y) for y in header]
    print "".join(header)
    while eps > tol:
        nint += 1
        fx = f(x)
        fxlinha = flinha(x)
        delta = -  fx / fxlinha
        display = [x, fx, fxlinha, delta]
        x += delta
        eps = abs(x - display[0]) / display[0]
        display += [eps]
        display = ["{0:20s}".format(str(y)) for y in display]
        print "".join(display)
    print "Raiz encontrada em x = {0:.5f} ({1} interacoes).".format(x, nint)
    ##########################################################################
    print 70 * "=="
    print "Solucao do exercicio 5"
    print 70 * "=="
    # Chutes iniciais (redefinindo)
    eps = 1.
    nint = 0
    x1 = x0[3]
    x2 = x0[4]
    while eps > tol:
        nint += 1
        f1 = f(x1)
        f2 = f(x2)
        display = [x1, x2, f1, f2]
        delta = (f(x2) - f(x1)) / (x2 - x1)
        x2 = x1 - f1 / delta
        x1 = display[1]
        eps = abs(x2 - x1) / x1
        display += [eps]
        display = ["{0:20s}".format(str(y)) for y in display]
        print "".join(display)
    print "Raiz encontrada em x = {0:.5f} ({1} interacoes).".format(x2, nint)
    print 70 * "=="

if __name__ == "__main__":
    # ex2()
    # ex345()
    # ex6()
