from tdalista import Lista

lista_personajes = Lista()
lista_aux = Lista()

lista1 = [
    {'nombre':'Scalet Witch','año_aparicion': 2013, 'heroe' : True},
    {'nombre':'Capitana Marvel','año_aparicion': 2005, 'heroe' : True},
    {'nombre':'Thanos','año_aparicion': 2020, 'heroe' : False},
    {'nombre':'Black Panther','año_aparicion': 2008, 'heroe': True},
    {'nombre':'Star-Lord','año_aparicion': 2012, 'heroe' : True},
    {'nombre':'Thor','año_aparicion': 2014, 'heroe' : True},
    {'nombre':'Dr. Strange','año_aparicion': 2015, 'heroe' : True},]

listaux = [
    {'nombre':'Loki','año_aparicion': 2003, 'heroe' : False},
    {'nombre':'Hulk','año_aparicion': 2001, 'heroe' : True},
    {'nombre':'Rocket Raccoon','año_aparicion': 2014, 'heroe' : True},
    {'nombre':'Black Widow','año_aparicion': 2010, 'heroe' : True}]

for personajes in lista1:
    lista_personajes.insertar(personajes, 'nombre')

for personajes in listaux:
    lista_aux.insertar(personajes, 'nombre')

print('')
print('Ejercicio A')
print('')
#A
pos = lista_personajes.busqueda('Thor', 'nombre')
if(pos != -1):
    print('La posicion de Thor es:', pos)
else:
    print('No se encuentra en la lista')

print('')
print('Ejercicio B')
print('')
#B
pos = lista_personajes.busqueda('Scalet Witch', 'nombre')
lista_personajes.obtener_elemento(pos)['nombre'] = 'Scarlet witch'
print(lista_personajes.obtener_elemento(pos))

print('')
print('Ejercicio C')
print('')
#C
for i in range (lista_aux.tamanio()):
    pos = lista_personajes.busqueda(lista_aux.obtener_elemento(i)['nombre'], 'nombre')
    if pos == -1:
        lista_personajes.insertar(lista_aux.obtener_elemento(i), 'nombre')
        print(pos)

print('')
print('Ejercicio D')
print('')
#D
"""Estan ordenados alfabeticamente"""
for i in range (lista_personajes.tamanio()):
    aux = lista_personajes.obtener_elemento(i)
    print('Barrido ascendente:', aux)

print('')

for i in range (lista_personajes.tamanio()-1,-1,-1):
    aux = lista_personajes.obtener_elemento(i)
    print('Barrido descendente:', aux)

print('')
print('Ejercicio E')
print('')
#E
for i in range (0, lista_personajes.tamanio()):
    pos = lista_personajes.obtener_elemento(i)
if (i == 7):
    print('El personaje en la posicion 7 es:', pos['nombre'])
else:
    print('No hay ningun personaje en esa posicion')

print('')
print('Ejercicio F')
print('')
#F
for i in range(0, lista_personajes.tamanio()):
    personaje = lista_personajes.obtener_elemento(i)
    if (personaje['nombre'][0] in ['C', 'S']):
        print(personaje['nombre'])

print('')
print('Ejercicio G')
print('')
#G
lista_nueva = Lista()


for i in range(0, lista_personajes.tamanio()):
    lista_nueva.insertar(lista_personajes.obtener_elemento(i), 'año_aparicion')

print('Ordenado por nombre:')
lista_personajes.barrido()
print()
print('Ordenado por año de aparicion:')
lista_nueva.barrido()