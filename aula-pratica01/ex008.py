competidores = int(input('Digite a quantidade de competidores: '))
qtdPapelCompradas = int(input('Digite a quantidade de papel compradas: '))
qtdPapelCompetidor = int(input('Digite a quantidade de papel por competidor: '))

if qtdPapelCompradas < (competidores * qtdPapelCompetidor):
  print('Insuficiente')
else:
  print('Suficiente')