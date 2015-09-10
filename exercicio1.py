# -*- coding: utf-8 -*-
"""

@author: Carlos Eduardo Barbosa

Calcular a parte inteira e fracionaria de um número inteiro

Comentarios em Python podem ser escritos utilizando triple quotes (chamados de
docstrings), como neste espaco. Isso permite a utilizacao de quaisquer tipo de
caracteres, incluindo multiplas linhas. Esse metodo permite documentacoes com
formatacao mais rica e complexa, incluindo exemplos de codigos. Alem disso,
comentarios de uma linha podem ser feitos com o simbolo #, similar ao utilizado
em Fortran.

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


