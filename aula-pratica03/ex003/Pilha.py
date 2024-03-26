class Pilha:
    __elementos = []

    def empilhar(self, elemento):
        self.__elementos.append(elemento)
    
    def desempilhar(self):
        if len(self.__elementos) == 0:
            print('Pilha vazia')
            return None
        else:
            ultimoElemento = self.__elementos[-1]
            self.__elementos.pop()
            return ultimoElemento

    def getPilha(self):
        return self.__elementos.copy()
    
    def lenPilha(self):
        return len(self.__elementos)