import numpy as np
from random import choice
from random import randrange
import math

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

print(f"O estudante escolhido foi: {choice(lista)}")
print(f"O numero aleatorio escolhido foi: {randrange(1, 100)}")

numero = choice(lista)
print(f"potencia de {numero} é: {math.pow(numero, 2)}")



