# matriz transposta

# captar a matriz
def criaMatriz(linhas, colunas):
  matriz = []

  for i in range(linhas):
    linha = []
    for j in range(colunas): # Adiciona os elementos na linha,
      elem = int(input(f'Digite o elemento da pos[{i+1}][{j+1}]: '))
      linha.append(elem) 

    matriz.append(linha) # Adiciona a linha na matriz
  
  return matriz

# imprimir a matriz
def imprimir_matriz(matriz):
  for linha in matriz:
    for elemento in linha:
      print(elemento, end=" ")
    print()

# criar transposta
def matrizTransposta(matriz, linhas, colunas):
  matrizTransposta = []

  for i in range(colunas):
    linha = []
    for j in range(linhas):
      linha.append(matriz[j][i])
    matrizTransposta.append(linha)
  
  return matrizTransposta
    
linhas = int(input('Digite a quantidade de linhas da matriz: '))
colunas = int(input('Digite a quantidade de colunas da matriz: '))

matriz = criaMatriz(linhas, colunas)
print('\nMatriz normal: ')
imprimir_matriz(matriz)

matrizT = matrizTransposta(matriz, linhas, colunas)
print('\nMatriz transposta: ')
imprimir_matriz(matrizT)
