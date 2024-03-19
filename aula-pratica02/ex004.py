seq = input('Digite a string: ')
c = input('Digite o caractere: ')

def stringManipulada(seq, c):
    posCaracter = seq.index(c)
    return seq[posCaracter+1:]
    
print(stringManipulada(seq, c))
    

