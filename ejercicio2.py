from tdacola import Cola
from tdapila import Pila

cola_notificaciones = Cola()
cola_aux = Cola()
pila_instagram = Pila()

Notificaciones = [['facebook','12:36', 'desea escribir algo'],['twitter', '17:30', 'Python'],['instagram', '20:30', 'se ha subido la foto']]

for element in Notificaciones:
    cola_notificaciones.arribo(element)
for element in Notificaciones:
    pila_instagram.apilar(element)

#C
# while not cola_notificaciones.cola_vacia():
#     aux = cola_notificaciones.atencion()
#     if (aux[0] in ['facebook']):
#         cola_notificaciones.atencion()
#         cola_aux.arribo(aux)

# while(not cola_aux.cola_vacia()):
#     dato = cola_aux.atencion()
#     print(dato)


#D
# while not cola_notificaciones.cola_vacia():
#     aux = cola_notificaciones.atencion()
#     if (aux[0] in ['twitter'] and aux[2] in ['Python']):
#            print('Los datos de Twitter son: ',aux[0], aux[1], aux[2])
#     cola_aux.arribo(aux)

# print('')

# while(not cola_aux.cola_vacia()):
#     dato = cola_aux.atencion()
#     print(dato)

#E
# while not pila_instagram.pila_vacia():
#     aux = pila_instagram.desapilar()
#     if aux[0] in ['instagram']:
#         print('Notificaciones de instagram:', aux[0], aux[1], aux[2])

# while(not pila_instagram.pila_vacia()):
#     dato = pila_instagram.desapilar()
#     print(dato)