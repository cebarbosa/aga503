# -*- coding: utf-8 -*-
"""

Created on 03/09/15

@author: Carlos Eduardo Barbosa

Escrever um programa que calcule o valor de pi usando  a serie abaixo,
com uma precisao pre-definida pelo usuario e que imprima o resultado
e o numero de termos que foram somados

pi / 4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...

"""
eps = input("Give the precision for the calculation of pi:")
i = 1.
atual = 1.
anterior = 0.
precisao = abs(atual - anterior) / atual
while precisao > eps:
    anterior = atual
    i += 1
    atual = anterior - (-1)**(i) / (2. * i - 1.)
    precisao = abs(atual - anterior) / atual
print "Number of terms: ", int(i)
print "Value of pi: ", 4. * atual
