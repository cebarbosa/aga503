# -*- coding: utf-8 -*-
"""

Created on 01/11/15

@author: Carlos Eduardo Barbosa

Resposta do exercicio 4

"""

import numpy as np

if __name__ == "__main__":
    A = np.array([[18., -9, -3],
                  [3, 15, -9],
                  [1, 1, -3]])
    b = np.array([13., 8, 4])
    print "solucao esperada: "
    print np.linalg.solve(A, b)
