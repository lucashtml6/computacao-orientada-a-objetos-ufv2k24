valorBombom = float(input('Digite o valor do bombom: '))
dinheiro = float(input('Digite o seu dinheiro: '))

def transacao(valorBombom, dinheiro): 
	qtdBombom = dinheiro // valorBombom
	troco = dinheiro % valorBombom
	print(qtdBombom, troco)
	
transacao(valorBombom, dinheiro)
