import matplotlib # importanto biblioteca sem alias
import matplotlib.pyplot as plt # importando a biblioteca com alias
from random import choice # importando uma função especifica da biblioteca random

# criando uma lista de estudantes
estudantes = ['João', 'Maria', 'Pedro', 'Ana', 'Bruno']
notas = [7, 8, 9, 6, 10]

# criando um grafico de barras
plt.bar(estudantes, notas)
plt.savefig("grafico.png")

estudante = choice(estudantes)
print(f"O estudante escolhido foi: {estudante}")




