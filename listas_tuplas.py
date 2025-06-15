from random import randint

def gerar_id_aleatorio():
    """Gera um ID aleatório de 10 dígitos."""
    return ''.join(str(randint(0, 9)) for _ in range(10))

estudantes = ['joão', 'maria', 'pedro', 'ana']

codigo_estudantes = []

for i in range(len(estudantes)):
    codigo_estudantes.append((estudantes[i], estudantes[i][0:3].upper() + gerar_id_aleatorio()))

print(codigo_estudantes)
