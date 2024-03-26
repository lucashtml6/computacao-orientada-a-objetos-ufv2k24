class Pessoa:
  nome = ""
  __idade = 0
  __peso = 0.0
  __altura = 0.0

  def setIdade(self, idade):
    self.__idade = idade

  def setPeso(self, peso):
    self.__peso = peso

  def setAltura(self, altura):
    self.__altura = altura

  def getIdade(self):
    return self.__idade
  
  def getPeso(self):
    return self.__peso
  
  def getAltura(self):
    return self.__altura
  
  def imprimirDados(self):
    print(f'Nome: {self.nome}')
    print(f'Idade: {self.__idade}')
    print(f'Peso: {self.__peso}')
    print(f'Altura: {self.__altura}')
  
  def retornaIMC(self):
    return (self.__peso / (self.__altura ** 2)) 