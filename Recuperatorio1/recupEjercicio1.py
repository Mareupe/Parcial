vector = ['Luke', 'Darth Vader', 'Yoda','Leia Organa', 'Han Solo']

#a
def barrido_recursivo(vec, i):
    if i == len(vec)-1:
        print (vec[i])
    else:
        print (vec[i]) 
        barrido_recursivo(vec, i+1)

barrido_recursivo(vector, 0)

print('')

#b
def busqueda_recursiva(vector, pos):
    if (pos < len(vector)):
        if vector[pos] == 'Yoda':
            return(pos)
        else:
            return busqueda_recursiva(vector, pos+1)
    else:
        return -1

pos = busqueda_recursiva(vector, 0)
if(pos != -1):
    print('Yoda se encuentra en el vector y esta en la posicion:', pos)
else:
    print('Yoda no se encuenta')