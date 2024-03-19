qtdElementos = int(input('Digite a quantidade de elementos: '))
lista = []

# for para armazenar elementos em uma lista
for c in range(qtdElementos):
  elemento = int(input(f'Digite o item {c+1}:'))
  lista.append(elemento)

lista.sort()

print(lista)