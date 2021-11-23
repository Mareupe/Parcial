

"""
vector = []

vector.append(2)
vector.append(1)
vector.append(0)
vector.append(4)
#vector.insert(1, 3)

print(vector)

#print(vector.pop(1))
#print(vector.pop())

print(vector)
"""

class Pila(object):

    def __init__(self):
        self.__elementos = []
    
    def apilar(self, dato):
        self.__elementos.append(dato)

    def desapilar(self):
        return self.__elementos.pop()

    def pila_vacia(self):
        return len(self.__elementos) ==0

    def tamanio(self):
         return len(self.__elementos)

    def elemento_cima(self):
        return self.__elementos[-1]

#pila = Pila()
#pila.apilar(5)
#pila.apilar(7)
#pila.apilar(9)
#pila.apilar(3)

#print(pila)

