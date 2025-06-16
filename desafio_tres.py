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
vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), 
          ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), (
              '2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), 
              ('2022', 5616)]

vendas_2022_maiores_seismil = [vendas[i][1] for i in range(len(vendas)) if vendas[i][0] == '2022' and vendas[i][1] >= 6000] #6
print(vendas_2022_maiores_seismil)

# desafio 7

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

diagnostico = [('Hipoglicemico', glicose) if glicose <= 70 else ('Normal', glicose) 
               if 70 < glicose < 100 else ('Alterado', glicose) 
               if 100 < glicose < 125 else ('Diabetes', glicose) for glicose in glicemia] #7
print(diagnostico)

# desafio 8

id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

lista_completa =  [(id[i], quantidade[i], preco[i]) for i in range(len(id))]  #8
print(lista_completa)

# desafio 9
estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']
frequencia = {estado: estados.count(estado) for estado in set(estados)}  #9
print(frequencia)

# desafio 10
funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), 
                ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), 
                ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), 
                ('ES', 14), ('SP', 10), ('MG', 12)]