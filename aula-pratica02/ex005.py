l1 = []
l2 = []
l3 = []

for c in range(3):
    elem = input(f'Digite o {c+1} elemento da primeira lista: ')
    l1.append(elem)
    
for c in range(3):
    elem = input(f'Digite o {c+1} elemento da segunda lista: ')
    l2.append(elem)
    
for c in range(3):
    l3.append(l1[c])
    l3.append(l2[c])
    
print(l3)
