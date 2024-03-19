vitoriasCor = int(input('Digite o numero de vitorias do Cormengo: '))
empatesCor = int(input('Digite o numero de empates do Cormengo: '))
saldoCor = int(input('Digite o numero de saldo de gols do Cormengo: '))

vitoriasFla = int(input('Digite o numero de vitorias do Flaminthians: '))
empatesFla = int(input('Digite o numero de empates do Flaminthians: '))
saldoFla = int(input('Digite o numero de saldo de gols do Flaminthians: '))

pontosCor = (vitoriasCor * 3) + empatesCor
pontosFla = (vitoriasFla * 3) + empatesFla


if pontosCor > pontosFla or (pontosCor == pontosFla and saldoCor > saldoFla):
  print('Cormengo')
elif pontosCor < pontosFla or (pontosCor == pontosFla and saldoCor < saldoFla):
  print('Flaminthians')
else:
  print('Empate')