# Funções
def criaMatriz(linhas, colunas):
  matriz = []

  for i in range(linhas):
    linha = []
    for j in range(colunas): # Adiciona os elementos na linha,
      elem = int(input(f'Digite o elemento da pos[{i+1}][{j+1}]: '))
      linha.append(elem) 

    matriz.append(linha) # Adiciona a linha na matriz
  
  return matriz

def imprimir_matriz(matriz):
  for linha in matriz:
    for elemento in linha:
      print(elemento, end=" ")
    print()

def contaQtdAparicoesNum(matriz, num):
  cont = 0
  for i in range(linhas):
    for j in range(colunas):
      if matriz[i][j] == num:
        cont += 1
  return cont

# Interação com o usuário
linhas = int(input('Digite a quantidade de linhas da matriz: '))
colunas = int(input('Digite a quantidade de colunas da matriz: '))

num = int(input('Digite o número a ser analisado: '))
print('\n')

# Cria a matriz
matriz = criaMatriz(linhas, colunas)

# Imprime a matriz
print('\nA matriz é: \n')
imprimir_matriz(matriz)

# Conta quanta vezes o num apareceu 
print(f'\nO número {num} apareceu {contaQtdAparicoesNum(matriz, num)} vezes na matriz.')