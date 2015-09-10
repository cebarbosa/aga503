# -*- coding: utf-8 -*-
"""

@author: Carlos Eduardo Barbosa

Esse programa constroi uma funcao para calcular o fatorial de um inteiro
dado pelo usuario.

"""

def fatorial(x):
    """ Calcula o fatorial de um numero positivo por recursao."""
    if x == 0:
        return 1
    else:
        return x * fatorial(x - 1)

arg = input("Entre com um numero inteiro: ")

# Verifica se o numero fornecido eh positivo antes de calcular seu fatorial
if arg >= 0:
    print fatorial(arg)
else:
    # Ao inves de apenas mostrar o erro utilizando o print, estou mostrando o
    # uso da keyword raise, que serve para parar a execucao do programa
    # e indicar o problema encontrado
    raise Exception("Erro: o numero tem que ser positivo!")
