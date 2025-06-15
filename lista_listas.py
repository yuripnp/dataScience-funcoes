# recebemos o desafio de organizar essa lista com nomes e notas de alunos separados por uma lista de nomes com notas

lista = ['joão', 10, 4, 10, 'maria', 9, 8, 7, 'pedro', 6, 5, 4, 'ana', 10, 9, 8]

nomes = []
notas = []
for i in range(len(lista)):
    if isinstance(lista[i], str):
        nomes.append(lista[i])
    else:
        notas.append(lista[i])
lista_organizada = []
for i in range(len(nomes)):
    lista_organizada.append([nomes[i], notas[i*3], notas[i*3+1], notas[i*3+2]])
    print(f'Aluno: {nomes[i]} - Notas: {notas[i*3:i*3+3]}')
print(lista_organizada)

