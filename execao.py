# try:
#   O codigo a ser executado. Caso uma exceção seja lançada, pare imediatamente
# except Exception as e:
#   O que fazer caso uma exceção seja lançada
# else:
#   O que fazer caso nenhuma exceção seja lançada
# finally:
#   O que fazer independente de uma exceção ser lançada ou não

# raise execao(mensagem de erro)




notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0],
         'Cláudia': [5.5, 6.6, 8.0], 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 
         'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}

try:
    nome = input('Digite o nome do aluno(a): ')
    resultado = notas[nome]
except Exception as e:
    print(f'Ocorreu um erro ao ler o nome: {e}')
else:
    print(f"o resultado é {resultado}")
finally:
    print('Fim do programa.')

def media(lista: list=[0]) -> float:
    """Calcula a média dos elementos de uma lista.
    lista, list, default [0]
    lista com as notas para calcular a média.
    return, calculo, float
    media calculada.
    """

    calculo = sum(lista) / len(lista) if lista else 0

    if len(lista) > 4:
        raise Exception('A lista não pode ter mais de 4 elementos.')
    return calculo

try:
    notas = [6.0, 7.0, 8.0, "0"]
    resultado = media(notas)
except TypeError:
    print('Erro: A lista deve conter apenas números.')
except ValueError as e:
    print(f'Erro: {e}')
else:
    print(f'A média é {resultado}')
finally:
    print('Fim do programa.')