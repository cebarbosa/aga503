# -*- coding: utf-8 -*-
"""

Created on 25/10/15

@author: Carlos Eduardo Barbosa

Resolução do exercício 1 do EP 2 usando Python + Numpy

"""
import numpy as np

class GaussElimination():
    """ Metodo de eliminação de Gauss para sistemas lineares. """
    def __init__(self,A,b, tol=0.01):
        """ Calcula a solucao de um sistema."""
        self.A = A
        self.b = b
        # Tolerancia para o determinante para testar se o sistema é
        # bem condicionado.
        self.tol = tol
        self.test_for_linear_combination()

    def test_for_linear_combination(self):
        """ Testa se uma coluna é multipla de outra. """
        pass

    def solve(self):
        # Fazendo a matriz expandida
        self.M = np.column_stack((self.A, self.b))
        self.normalize()
        self.partial_pivoting()
        self.forward_elimination()
        self.backward_substitution()
        self.test_solution()

    def normalize(self):
        """ Normalizacao da matriz. """
        self.norm = np.sqrt(np.sum(self.A*self.A, axis=1))
        self.M = np.transpose(self.M.T / self.norm)

    def partial_pivoting(self):
        self.idx = np.arange(len(self.b)) # Guarda a ordem original da matrix
        for i in range(len(self.b)):
            j = i + np.argmax(np.abs(self.M[i:,i]))
            self.M[[i,j]] =  self.M[[j,i]]
            self.idx[[i,j]] = self.idx[[j,i]]
        return

    def forward_elimination(self):
        """ Eliminação para frente. """
        self.multiplicadores = np.zeros_like(self.A)
        for i in range(1,len(self.b)):
            a = self.M[i:,i-1] / self.M[i-1,i-1]
            for k,j in enumerate(range(i,len(self.b))):
                self.M[j] -= self.M[i-1] * a[k]
            self.multiplicadores[i:,i-1] = a
        # Calculo do determinante na matrix triangulada
        self.detnorm = np.prod(np.diag(self.M[:,:-1]))
        self.det = np.prod(np.diag(self.M[:,:-1] * self.norm))
        if np.abs(self.detnorm) < self.tol:
            print "Warning: System may be not well conditioned. "
        # Estou trabalhando com a matrix expandida para simplificar, mas a
        # solucao para a matrix triangular com os multiplicadores eh dada
        # abaixo
        self.Amulti = self.multiplicadores + self.M[:,:-1]
        return

    def backward_substitution(self):
        """ Eliminacao para tras. """
        self.sol = np.zeros_like(self.b)
        for i in range(len(self.b))[::-1]:
            if i == len(self.b) - 1:
                self.sol[i] = self.M[i,-1] / self.M[i,i]
            else:
                self.sol[i] = (self.M[i,-1] - np.sum(self.M[i,i+1:-1] *
                               self.sol[i+1:])) / self.M[i,i]

    def test_solution(self):
        """ Test if all elements are finite. """
        self.is_valid = np.all(np.isfinite(self.sol))
        if not self.is_valid:
            print "System is ill conditioned!"


if __name__ == "__main__":
    A = np.array([[4, 3, 2, 2],
                  [2, 1, 1, 2],
                  [2, 2, 2, 4],
                  [6, 1, 1, 4]], dtype=float)
    b = np.array([5, 8, 3, 1], dtype=float)
    M = GaussElimination(A,b)
    M.solve()
    print "The solution for the system is: {0}".format(M.sol)



