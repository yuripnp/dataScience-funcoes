
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

"""
gabarito = ['D', 'A', 'B', 'C', 'A']
escolhas_possiveis = ['A', 'B', 'C', 'D']

testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

def verificar_nota(nota: str, possibilidades: list) -> bool:
    if nota not in possibilidades:
        return False
    else:
        return True

def analise_de_testes(testes: list):
    pontuacoes = []
    try:
        for teste in testes:
            nota = 0
            for i in range(len(teste)):
                valido = verificar_nota(teste[i],  escolhas_possiveis)
                if(valido):
                    if teste[i] == gabarito[i]:
                        nota += 1
                else:
                    raise ValueError(f'a alternativa {teste[i]} não é uma opção')
            pontuacoes.append(nota)
    except Exception as e:
        print(e)
    else:
        return pontuacoes
    
notas_sem_erro = analise_de_testes(testes_sem_ex)
print(notas_sem_erro)
notas_com_erro = analise_de_testes(testes_com_ex)
"""

# desafio 6
"""
lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
                  'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']

lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
                  'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']


def verificar_caracter(lista_de_palavras: list):
    try:
        for palavra in lista_de_palavras:
            if ("," in palavra) or (";" in palavra) or ("!" in palavra) or ("?" in palavra):
                raise ValueError(f"Palavra contem caracter especial não autorizado {palavra}")
    except Exception as e:
        print(e)
    else:
        print(palavra)
        

verificacao_sem_error = verificar_caracter(lista_tratada)
verificacao_com_error = verificar_caracter(lista_nao_tratada)
"""

# desafio 7
"""
pressoes = [100, 120, 140, 160, 180]
temperaturas = [20, 25, 30, 35, 40]

pressoes_divide_por_zero = [60, 120, 140, 160, 180]
temperaturas_divide_por_zero = [0, 25, 30, 35, 40]

pressoes_tamanho_diferente = [100, 120, 140, 160]
temperaturas_tamanho_diferente = [20, 25, 30, 35, 40]

def validacao_listas(pressao, temperatura):
    try:
        if len(pressao) != len(temperatura):
            raise ValueError(f"listas imcompativeis")
        resultado = [round(pressao[i]/temperatura[i]) for i in range(len(pressao))]
    except ZeroDivisionError as e:
        print(f"Não pode dividir por zero! {e}")
    else:
        return resultado

#print(validacao_listas(pressoes, temperaturas))
#print(validacao_listas(pressoes_divide_por_zero, temperaturas_divide_por_zero))
print(validacao_listas(pressoes_tamanho_diferente, temperaturas_tamanho_diferente))
"""

