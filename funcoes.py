

# criando uma função
def soma(a, b):
    return a + b

print(soma(1, 2))

# criando uma função com parametro opcional
def soma(a, b=0):
    return a + b

print(soma(1))

notas = [7, 8, 9, 10]

def media(notas):
    return sum(notas) / len(notas)

print(media(notas))

# criando uma função com parametro variadico
def soma(*numeros):
    return sum(numeros)

# crie uma função que vai receber uma lista de notas de um aluno e retorna para saber se ele
# foi aprovado ou reprovado

def status_aluno(notas):
    media = sum(notas) / len(notas)
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

print(status_aluno(notas))

# criando uma função que recebe uma lista de notas e retorna a maior nota