from random import randint

def gerar_id_aleatorio():
    """Gera um ID aleatório de 10 dígitos."""
    return ''.join(str(randint(0, 9)) for _ in range(10))

def calcular_media(notas: list=[0]) -> float:
    """Calcula a média de uma lista de notas."""
    return sum(notas) / len(notas) if notas else 0.0

# nomes = [expressao for item in lista]
# nomes = [expressao for item in lista if condicao]
# [resultado_if if condicao else resultado_else for item in lista]


codigo_estudantes = []
estudantes = ['joão', 'maria', 'pedro', 'ana']
notas_alunos = [[10.0, 9.5, 8.0], [9.0, 8.5, 7.0], [6.0, 5.5, 4.0], [10.0, 9.5, 8.0]]

for i in range(len(estudantes)):
    codigo_estudantes.append((estudantes[i], estudantes[i][0:3].upper() + gerar_id_aleatorio()))

# exemplo de list comprehension para calcular a média das notas dos alunos
medias = [round(calcular_media(notas), 1) for notas in notas_alunos]

nomes = [item[0] for item in codigo_estudantes]
print(nomes)
print(medias)

candidatos = list(zip(nomes, medias))
print(candidatos)

candidatos_aprovados = [candidato[0] for candidato in candidatos if candidato[1] >= 7.0]
print(candidatos_aprovados)

situacao_candidatos = ["Aprovado(a)" if media >= 6 else "Reprovado(r)" for media in medias]
print(situacao_candidatos)

cadastrados = [x for x in [nomes, medias, situacao_candidatos]]
print(cadastrados)

