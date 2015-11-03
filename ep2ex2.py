# -*- coding: utf-8 -*-
"""

Created on 01/11/15

@author: Carlos Eduardo Barbosa

Solution for exercise 2.

"""

import numpy as np

from ep2ex1 import GaussElimination

def circle4points(p, tol=1e-1):
    A = np.column_stack((2. * p[:,0], 2. * p[:,1], [-1,-1,-1]))
    b = np.sum(p**2, axis=1)
    # Normalizing the vectors
    norm = np.sqrt(np.sum(A*A, axis=1))
    An = np.transpose(A.T / norm)
    bn = b / norm
    # Solving the system
    M = GaussElimination(An,bn)
    M.solve()
    sol = M.sol
    # Calculating determinant of a 3x3 matrix
    det = An[0,0] * An[1,1] * An[2,2] + An[0,1] * An[1,2] * An[2,0] + \
          An[0,2] * An[1,0] * An[2,1] - An[0,2] * An[1,1] * An[2,0] - \
          An[0,1] * An[1,0] * An[2,2] - An[0,0] * An[1,2] * An[2,1]
    r = np.sqrt(sol[0]**2 + sol[1]**2 - sol[2])
    eps = np.finfo(float).eps
    if np.abs(det) < eps:
        print "System does not have a solution (det=0)"
    elif np.abs(det) < tol:
        print "System is ill conditioned: |det| = {0}".format(np.abs(det))
    else:
        print "System has a determined solution: det = {0}".format(det)
    print "Solution is x = {0:.5f}, y={1:.5f} and r={2:.5f}".format(sol[0],
                                                                    sol[1],r)
    return


if __name__ == "__main__":
    # Input points
    pa = np.array([[1,1],[2,2],[3,3]], dtype=float) # colinear
    pb = np.array([[1,1],[2,2],[3,3.01]], dtype=float) # almost colinear
    pc = np.array([[1,1],[2,4],[5,2]], dtype=float) # well conditioned
    # Solution
    # sa = circle4points(pa)
    # sb = circle4points(pb)
    # sc = circle4points(pc)
    p = np.array([[2,0],[0,2],[-2,0]], dtype=float)
    sd = circle4points(p)