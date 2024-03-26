from Pessoa import Pessoa

# instanciação dos objetos
pessoa1 = Pessoa()

pessoa1.nome = 'Pedro'
pessoa1.setIdade(20)
pessoa1.setAltura(1.9)
pessoa1.setPeso(60.0)

pessoa2 = Pessoa()
pessoa2.nome = 'Pedro'
pessoa2.setIdade(20)
pessoa2.setAltura(1.7)
pessoa2.setPeso(70.0)

#a
pessoa1.imprimirDados()
pessoa2.imprimirDados()

#b
def verificaMaisVelha(pessoa1, pessoa2):
  if pessoa1.getIdade() > pessoa2.getIdade():
    return pessoa1
  elif pessoa1.getIdade() < pessoa2.getIdade():
    return pessoa2
  else:
    return None
  

maisVelha = verificaMaisVelha(pessoa1, pessoa2)

if maisVelha == None:
  print('iGUAIS')
else:
  maisVelha.imprimirDados()

# c
print(pessoa1.retornaIMC())
print(pessoa2.retornaIMC())