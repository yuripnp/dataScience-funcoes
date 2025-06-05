lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

print(f"O tamanho da lista é: {len(lista)}")
print(f"O maior valor da lista é: {max(lista)}")
print(f"O menor valor da lista é: {min(lista)}")
print(f"A soma dos valores da lista é: {sum(lista)}")

listaDeValores = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
def tabuada(numero: int) -> None:
    """
    Função que imprime a tabuada de um número.
    :param numero: Número para o qual a tabuada será gerada.
    """
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def multiplos_de_tres(listaDeNumeros):
    """
    Função que imprime os múltiplos de 3 até um número.
    :param numero: Número limite para os múltiplos de 3.
    """
    lista_multiplos = []
    for numero in listaDeNumeros:
        if numero % 3 == 0:
            lista_multiplos.append(numero)
    return lista_multiplos
            
tabuada(5)
multiplos = multiplos_de_tres(listaDeValores)
print(f"Múltiplos de 3 na lista: {multiplos}")

lista_de_dez = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_de_quadrados = list(map(lambda x: x**2, lista_de_dez))
print(f"Lista de quadrados: {lista_de_quadrados}")
