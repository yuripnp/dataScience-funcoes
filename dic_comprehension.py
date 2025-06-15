# {chave: valor for item in lista}

valores = [[('joão', 'JOÃ6537853642'), ('maria', 'MAR9821780952'), ('pedro', 'PED2298970559'), ('ana', 'ANA8311369289')], 
           [9.2, 8.2, 5.2, 9.2],
           [[10.0, 9.5, 8.0], [9.0, 8.5, 7.0], [6.0, 5.5, 4.0], [10.0, 9.5, 8.0]],
           ['Aprovado(a)', 'Aprovado(a)', 'Reprovado(r)', 'Aprovado(a)']]

colunas = ['media', 'notas', 'situacao']

cadastro = {colunas[i]: valores[i+1] for i in range(len(colunas))}
print(cadastro)

#cadastro['nomes'] = valores[0]
cadastro['nomes'] = [valores[0][i][0] for i in range(len(valores[0]))]
print(cadastro)