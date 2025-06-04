notas = [7, 8, 9, 10]

acrescimo_do_professor = 0.5

notas_ajustadas = list(map(lambda nota: nota + acrescimo_do_professor, notas))
print(f"Notas ajustadas: {notas_ajustadas}")