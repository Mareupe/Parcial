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
def elminar_notificacion(cola):
    while not cola_notificaciones.cola_vacia():
        aux = cola_notificaciones.atencion()
        if (aux[0] != 'facebook'):
            cola_notificaciones.atencion()
            cola_aux.arribo(aux)

    while(not cola_aux.cola_vacia()):
        dato = cola_aux.atencion()
        print(dato)

#D
while not cola_notificaciones.cola_vacia():
    aux = cola_notificaciones.atencion()
    if (aux[0] in ['twitter'] and aux[2] in ['Python']):
           print('Los datos de Twitter son: ',aux[0], aux[1], aux[2])
    cola_aux.arribo(aux)

print('')

while(not cola_aux.cola_vacia()):
    dato = cola_aux.atencion()
    print(dato)


print('')
#E
while not cola_notificaciones.cola_vacia():
    aux = cola_notificaciones.atencion()
    cola_aux.arribo(aux)
    if aux[0] in ['instagram']:
        pila_instagram.apilar(aux)

while(not cola_aux.cola_vacia()):
    cola_notificaciones.arribo(cola_aux.atencion)

print('Datos de la pila:', aux)