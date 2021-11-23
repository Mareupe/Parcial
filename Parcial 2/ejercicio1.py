from arbol_binario import Arbol
from random import randint

arbol = Arbol()
arbolN = Arbol()
arbolC = Arbol()

datos = [
    {'nombre':'Mosasaurus', 'Codigo': '14548', 'ubicacion': '2F'},
    {'nombre':'T-Rex', 'Codigo': '14100', 'ubicacion': '4P'},
    {'nombre':'Triceratops', 'Codigo': '5693', 'ubicacion': '1T'},
    {'nombre':'T-Rex', 'Codigo': '8765', 'ubicacion': '0D'},
    {'nombre':'Raptor', 'Codigo': '21500','ubicacion': '9C'},
    {'nombre':'Raptor ', 'Codigo': '6580', 'ubicacion': '4T'},
    {'nombre':'T-Rex', 'Codigo': '792', 'ubicacion': '8V'},
    {'nombre':'Diplodocus', 'Codigo': '00127', 'ubicacion': '7A'},
    {'nombre':'Raptor ', 'Codigo': '8979','ubicacion': '2U'},
    {'nombre':'Sgimoloch', 'Codigo': '98547','ubicacion': '6F'},
    {'nombre':'Diplodocus', 'Codigo': '20202', 'ubicacion': '3A'},
    {'nombre':'T-Rex', 'Codigo': '9876', 'ubicacion': '9Q'},
    {'nombre':'Diplodocus', 'Codigo': '768234', 'ubicacion': '1B'},
    {'nombre':'Raptor ', 'Codigo': '5124', 'ubicacion': '6Y'},
    {'nombre':'Raptor ', 'Codigo': '6329', 'ubicacion': '8O'},
]

#2
for elemento in datos:
    arbolN = arbolN.insertar_nodo(elemento['nombre'],elemento)
for elemento in datos:
    arbolC = arbolC.insertar_nodo(elemento['Codigo'],elemento)

#3
print('Barrido por nombre')
arbolN.inorden()
print('')


#4
print('informacion del Dinosaurio con Codigo 792:')
arbolC.mostrar_792('792')
print('')

#5
print('La info de los T-Rex que hay en la isla:')
arbolN.busqueda_Trex('T-Rex')
print('')

#6
buscado = input('ingrese a quien buscar:')
arbolN.busqueda_proximidad(buscado)
buscado = input('ingrese a quien quiere cambiar el nombre:')
buscado2 = input('ingrese nuevo nombre:')
clave, dato = arbolN.eliminar_nodo(buscado)
dato['nombre'] = buscado2
arbolN = arbolN.insertar_nodo(buscado2,dato)
arbolN.inorden()
print('')

# buscado = input('ingrese a quien buscar:')
# arbolC.busqueda_proximidad(buscado)
# buscado = input('ingrese a quien quiere cambiar el nombre:')
# buscado2 = input('ingrese nuevo nombre:')
# clave, dato = arbolC.eliminar_nodo(buscado)
# dato['nombre'] = buscado2
# arbolC = arbolC.insertar_nodo(buscado2,dato)
# arbolC.inorden()
# print('')

#7
print('Ubicacion de los Raptores')
arbolN.busqueda_Raptor('Raptor')
print('')
#8
print('Cantidad de diplodocus en el parque:', arbolN.contar_ocurrencias('Diplodocus'))
