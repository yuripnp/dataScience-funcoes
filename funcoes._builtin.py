notas = {"1º trimestre": 7, "2º trimestre": 8, "3º trimestre": 9, "4º trimestre": 10}
soma = 0

for nota in notas.values():
    soma += nota
print(f"A soma das notas é: {soma}")

# ou
somatoria = sum(notas.values())
print(f"A soma das notas é: {somatoria}")

tamanho = len(notas.values())
print(f"O tamanho da lista é: {tamanho}")

print(f"A media das notas é: {sum(notas.values()) /len(notas.values())}")

# arendondando
media = sum(notas.values()) / len(notas.values())
print(f"A media das notas é: {round(media, 2)}")
