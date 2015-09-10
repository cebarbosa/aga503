# -*- coding: utf-8 -*-
"""

Created on 09/09/15

@author: Carlos Eduardo Barbosa

Calcular a parte inteira e fracionaria de um número inteiro

"""

# Ler o numero real
x = input("Entre com um numero: ")

# Armazena a parte inteira em uma nova variavel
i = int(x)

# Calcula a parte fracionaria
frac = x - i

# Escrever o resultado
print "Numero fornecido: ", x
print "Parte inteira: ", i
print "Parte fracionaria: ", frac
print "Bonus: Parte fracionaria usando o operador %: ", x % i


