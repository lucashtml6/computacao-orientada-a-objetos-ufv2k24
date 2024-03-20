# Insertion Sort

def insertionSort(lista):
  n = len(lista)
  for i in range(1, n):
    elemAnalisado = lista[i]
    j =  i - 1
    while j >= 0 and elemAnalisado < lista[j]:
      lista[j+1] = lista[j]
      j -= 1
    lista[j+1] = elemAnalisado

insertionSort([2, 3, 1, 8, 7])