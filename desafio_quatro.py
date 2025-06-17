
#  desafio 1
"""
try:
    numero_um = float(input("Digite o primeiro numero: "))
    numero_dois = float(input("Digite o segundo numero: "))
    divisao = numero_um/numero_dois
except ValueError as e:
    print(f"valor invalido {e}")
except ZeroDivisionError as e:
    print(f"O segundo numero não pode ser zero {e}")
else:
    print(f"A divisão desses dois numeros é {divisao}")
"""
# desafio 2

"""
idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}

try:
    nome = input("Digite um nome: ")
    idade_do_usuario = idades[nome]
except KeyError as e:
    print(f"Valor não encontrado {e}")
else:
    print(f"a idade do {nome} é {idade_do_usuario}")
"""

# desafio 3
"""
lista_valores = [10, 4, 9, 2, "a"]
def converter_lista(lista: list=[0]):
    lista_convertida = []
    for valor in lista:
        try:
            valor_convertido = float(valor)
        except ValueError as e:
            print(f"valor invalido {e}")
        else:
            lista_convertida.append(valor_convertido)
        finally:
            print(lista_convertida)

converter_lista(lista_valores)
"""

# desafio 4

"""
lista1 = [4,6,7,9,10]
lista2 = [-4,6,8,7,9]

lista3 = [4,6,7,9,10,4]
lista4 = [-4,6,8,7,9]

lista5 = [4,6,7,9,'A']
lista6 = [-4,'E',8,7,9]

def juncao_de_listas(listaUm, listaDois) -> list:
    lista_de_tuplas = []
    for i in range(len(listaUm)):
        try:
            valor_um_convertido = float(listaUm[i])
            valor_dois_convertido = float(listaDois[i])
        except ValueError as e:
            print("valor invalido na lista {e}")
            break
        except IndexError as e:
            print(f"listas não são compativeis {e}")
        else:
            lista_de_tuplas.append((valor_um_convertido, valor_dois_convertido, i))
    return lista_de_tuplas

tuplas_um = juncao_de_listas(lista1, lista2)
print(tuplas_um)

tuplas_dois = juncao_de_listas(lista3, lista4)
tuplas_tres = juncao_de_listas(lista5, lista6)
"""

# desafio 5
gabarito = ['D', 'A', 'B', 'C', 'A']

testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

