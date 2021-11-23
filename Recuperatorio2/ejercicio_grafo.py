from grafo import Grafo
from lista import Lista

red = Grafo(dirigido=False)

red.insertar_vertice('Manjaro', data = {'PC'})
red.insertar_vertice('Parrot', data = {'PC'})
red.insertar_vertice('Fedora', data = {'PC'})
red.insertar_vertice('Mint', data = {'PC'})
red.insertar_vertice('Ubuntu', data = {'PC'})
red.insertar_vertice('Arch', data = {'Notebook'})
red.insertar_vertice('Debian', data = {'Notebook'})
red.insertar_vertice('Red Hat', data = {'Notebook'})
red.insertar_vertice('Router 1', data = {'Router'})
red.insertar_vertice('Router 2', data = {'Router'})
red.insertar_vertice('Router 3', data = {'Router'})
red.insertar_vertice('Guarani', data = {'Servidor'})
red.insertar_vertice('MongoDB', data = {'Servidor'})
red.insertar_vertice('Switch 1', data = {'Switch'})
red.insertar_vertice('Switch 2', data = {'Switch'})   
red.insertar_vertice('Impresora', data = {'impresora'})


red.insertar_arista(40, 'Manjaro', 'Switch 2')
red.insertar_arista(12, 'Parrot', 'Switch 2')
red.insertar_arista(5, 'MongoDB', 'Switch 2')
red.insertar_arista(56, 'Arch', 'Switch 2')
red.insertar_arista(40, 'Manjaro', 'Switch 2')
red.insertar_arista(61, 'Router 3', 'Switch 2')
red.insertar_arista(43, 'Router 1', 'Router 3')
red.insertar_arista(50, 'Router 2', 'Router 3')
red.insertar_arista(37, 'Router 2', 'Router 1')
red.insertar_arista(9, 'Router 2', 'Guarani')
red.insertar_arista(25, 'Router 2', 'Red Hat')
red.insertar_arista(29, 'Router 1', 'Switch 1')
red.insertar_arista(17, 'Switch 1', 'Debian')
red.insertar_arista(18, 'Switch 1', 'Ubuntu')
red.insertar_arista(22, 'Switch 1', 'Impresora')
red.insertar_arista(80, 'Switch 1', 'Mint')

#2
pos = red.buscar_vertice('Red Hat') 
print('Barrido en profundidad de Red Hat:')
red.barrido_profundidad(pos)
red.marcar_no_visitado()
print('')
print('Barrido en amplitud de Red Hat:')
red.barrido_amplitud(pos)
red.marcar_no_visitado()
print('')

pos = red.buscar_vertice('Debian') 
print('Barrido en profundidad de Debian:')
red.barrido_profundidad(pos)
red.marcar_no_visitado()
print('')
print('Barrido en amplitud de Debian:')
red.barrido_amplitud(pos)
red.marcar_no_visitado()
print('')

pos = red.buscar_vertice('Arch')
print('Barrido en profundidad de Arch:')
red.barrido_profundidad(pos)
red.marcar_no_visitado()
print('')
print('Barrido en amplitud de Arch:')
red.barrido_amplitud(pos)
red.marcar_no_visitado()
print('')


#3
def camino_mas_corto(uno,dos):
    ver_origen = red.buscar_vertice(uno)
    ver_destino = red.buscar_vertice(dos)
    pila_camino = red.dijkstra(ver_origen, ver_destino)
    costo = None
    destino = dos
    while(not pila_camino.pila_vacia()):
        dato = pila_camino.desapilar()
        if(dato[1][0] == destino):
            if(costo is None):
                costo = dato[0]
            print(dato[1][0])
            destino = dato[1][1]

    print('El costo total del camino es', costo)

print('El camino más corto de Debian a MongoDB:')
camino_mas_corto('Debian', 'MongoDB')
print('')
print('El camino más corto de Red Hat a MongoDB:')
camino_mas_corto('Red Hat', 'MongoDB')
print('')


#4
exp_mini = red.prim()
peso = 0
print('Árbol de expansión mínima:')
for elemento in exp_mini:
    print(elemento[1])
    peso += elemento[0]
print('El costo total es', peso, 'km.')
print('')


#5
red.eliminar_vertice('Impresora')
print('Barrido en profundidad para corroborar que se elimino Impresora')
red.barrido_profundidad(0)
