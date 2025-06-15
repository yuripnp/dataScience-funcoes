# desafio 1
lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

def somar(lista: list([0])) -> list: # type: ignore
    """Cria uma lista com a soma dos elementos de cada sublista."""
    return [sum(sublista) for sublista in lista]

lista_soma = somar(lista_de_listas)
print(lista_soma)

# desafio 2, 3, 4
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

peso = [tupla[2] for tupla in lista_de_tuplas] #2
nomes_tuplas = [(i, lista_de_tuplas[i][0]) for i in range(len(lista_de_tuplas))] #3
print(nomes_tuplas)

aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

aluguel_apartamento = [aluguel[i][1] for i in range(len(aluguel)) if aluguel[i][0] == 'Apartamento'] #4
print(aluguel_apartamento)

# desafio 5
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

dic_despesas = {meses[i]: despesa[i] for i in range(len(meses))} #5
print(dic_despesas)

# desafio 6
