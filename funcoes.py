

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

def status_aluno(notas: list[0]) -> tuple[float, str]:
    """
    Função que recebe uma lista de notas e retorna a média e a situação do aluno.
    :param notas: Lista de notas do aluno
    """

    
    media = sum(notas) / len(notas)
    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    return (media, situacao)

media, situacao = status_aluno(notas)
print(f"Média: {media}, Situação: {situacao}")

# criando uma função que recebe uma lista de notas e retorna a maior nota