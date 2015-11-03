# -*- coding: utf-8 -*-
"""

Created on 13/10/15

@author: Carlos Eduardo Barbosa

Solution for EP 1

"""

import numpy as np

import matplotlib.pyplot as plt

def hand_sort(a):
    """ Sort and array like a card player. """
    # Create array of the same dimension of the output
    asorted = np.empty_like(a)
    # For the remaining cards, do the sorting
    nsteps = 0
    for i in range(len(a)):
        asorted[i] = a[i]
        for j in range(i)[::-1]:
            nsteps += 1
            if asorted[j+1] < asorted[j]:
                asorted[j:j+2] = asorted[j:j+2][::-1]
            else:
                break
    return asorted, nsteps

if __name__ == "__main__":
    results = []
    for n in range(5,501,5):
        a = np.random.random(n)
        asorted, nsteps = hand_sort(a)
        results.append([n, nsteps])
        if n == 20:
            print "Results for N=20"
            print "Input array: "
            print a
            print "Output array"
            print asorted
    ##########################################################################
    # Saving results in a file
    with open("nsteps.txt", "w") as f:
        f.write("{0:15s}{1:15s}\n".format("#SIZE", "NSTEPS"))
        # Saving results in a single line using list comprehension
        # The complication is just to have a nicely formatted table
        f.write("\n".join(["".join(["{0!s:15}".format(y) for y in x]) for x in
                           results]))
    ##########################################################################
    # Ploting the results
    x, y = np.array(results).T
    plt.plot(x, y, "ok", label="Nsteps")
    plt.plot(np.linspace(0,500,100), np.linspace(0,500,100)**2/4,
             label=r"$\frac{N^2}{4}$")
    plt.legend(loc=0)
    plt.xlabel("N")
    plt.ylabel("Nsteps")
    plt.minorticks_on()
    plt.pause(0.001)
    plt.savefig("ex1.png")
    plt.show(block=True)


