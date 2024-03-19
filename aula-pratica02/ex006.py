elem = 0
lista = []

# coleta os elementos da lista
while True:
    elem = int(input('Digite o elemento (-1 p/ sair): '))
    if elem == -1:
        break
    lista.append(elem)

# define um ponto de partida para ser analisado
maior = lista[0]

# vai comecar analisando o item na pos [1]
for c in range(1, len(lista)):
    if lista[c] > maior: 
        maior = lista[c]


print(maior)
