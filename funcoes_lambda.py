# situação 4
# Nesta demanda precisamos criar uma calculadora que calcula a  média ponderada de notas
# de uma dada matéria. Vamos requisitar ao usuário a entrada das 3 notas (N1, N2, N3)

notas = []
nota = 0
while nota != -1:
    nota = float(input("Digite a nota do aluno (ou -1 para sair): "))
    if nota != -1:
        notas.append(nota)

media = lambda notas: sum(notas) / len(notas) if notas else 0
situacao = lambda media: "Aprovado" if media >= 7 else "Reprovado"
media_calculada = round(media(notas), 2)
print(f"Média: {media_calculada}, Situação: {situacao(media_calculada)}")

delta = lambda a, b, c: b**2 - 4*a*c

