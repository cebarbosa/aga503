# -*- coding: utf-8 -*-
"""

@author: Carlos Eduardo Barbosa

Programa de exemplo para usar a funcao raizes utilizando modulos
das bibliotecas padrao de Python (ou seja, que nao necessitam instalacao)

"""
# Carregar biblioteca de funcoes matematicas
import math

# Todos os modulos devem ser carregados no inicio dos programas!

# Diferentemente do Fortran, funcoes e classes sao colocadas no inicio

def raizes(x):
    """ Funcao que calcula raizes da variavel x. """
    # Raiz quadrada
    x2 = math.sqrt(x)
    # Outras raizes calculadas usando logaritmos
    logx = math.log(x)
    x3 = math.exp(logx / 3.)
    x4 = math.exp(logx / 4.)
    x5 = math.exp(logx / 5.)
    # Retorna os resultados
    return x2, x3, x4, x5

# O programa "main" de Python é definido apenas pela identacao
arg = input("Entre com o valor do argumento: ")
print "Raizes = ", raizes(arg)





