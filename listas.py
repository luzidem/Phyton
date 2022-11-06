#Trabajando con listas

print('###### Definimos elementos de Mi_Lista #############')
mi_lista = [1,2,3,4,5]
print(mi_lista)
print('\n')

print('###### Imprime el tipo #############')
print(type(mi_lista))
print('\n')

print(' ####### Probamos imprimiendo pisiciones en la lista ############')
print('Imprime posicion 1: ', mi_lista[0])
print('Imprime posicion 2: ', mi_lista[1])
print('\n')

#cambiando un elemento de la lista
print(' ####### Probamos cambiando el valor de un elemento [1] de la lista ############')
mi_lista[1]= 7
print('Imprime resultado de la nueva lista de elementos: ', mi_lista)
print('\n')

print(' ####### Definimos una lista de estudiantes ############')
lista_estudiantes = ['Luz','José','Carlos', 'Bet','Teo']
print(lista_estudiantes)
print('\n')

print(' ####### Imprime desde la posición 0 en adelante 3 elementos de la lista ############')
print(lista_estudiantes[0:3])
print('\n')

print(' ####### Imprime desde la posición 0 en adelante 1 elementos de la lista ############')
print(lista_estudiantes[0:1])
print('\n')

print(' ####### Imprime desde la posición 0 en adelante 3 elementos de la lista ############')
print(lista_estudiantes[:3])
print('\n')

print(' ####### Imprime desde la posición 1 hasta una posición antes de la última de la lista ############')
print(lista_estudiantes)
print(lista_estudiantes[1:-1])
print('\n')

print(' ####### Imprime desde la posición 1 en adelante todo ############')
print(lista_estudiantes[1:])
print('\n')

print(' ####### LISTAS COMBINADAS ############')
lista_combinada = ['Hola',0,1.3,True,'Bienvenido']
print('La lista combinada es: ',lista_combinada)
print('\n')


nueva_lista = [[1,2,3],[4,5,6],[7,8,9]]
print('Las listas son: ', nueva_lista)
print('\n')
print('imprime la lista de la posición 0: ',nueva_lista[0])
print('\n')

print('imprime la lista de la posición 1: ',nueva_lista[1])
print('\n')

print('imprime la lista de la posición 1 su elemento 2: ',nueva_lista[1][2])
print('\n')

print(' ####### Modifico las listas iniciales ############')
nueva_lista = [[1,2,3],[4,5,6],[7,8,9],lista_combinada]
print('Las listas son: ', nueva_lista)
print('\n')

print(' ####### Añadir elementos con append ############')
lista_combinada.append('Nuevo dato con append')
print(lista_combinada)
print('\n')

print(' ####### Añadir elementos con insert ############')
lista_combinada.insert(0,'posicion 0')
print(lista_combinada)
print('\n')
print(' ####### Añadir elementos con pop ############')
lista_combinada.pop()
print(lista_combinada)
print('\n')
print(' ####### eliminar elementos con pop ############')
lista_combinada.pop(1)
print(lista_combinada)
print('\n')

print(' ####### eliminar elementos con remove ############')
lista_combinada.remove(True)
print(lista_combinada)
print('\n')
print(' ####### Contar elementos de lista ############')
lista_contador=[1,2,3,4,5,6,7,'Hola','Hola']
print(lista_contador)
print(len(lista_contador))
print('\n')

print(' ####### Contar elementos repetidos de lista ############')
lista_contador=[1,2,3,4,5,6,7,'Hola','Hola']
print(lista_contador)
print(lista_contador.count('Hola'))
print('\n')

print(' ####### Imprime la posición de lo que busco ############')
lista_contador=[1,2,3,4,5,6,7,'Hola','Hola','Chau']
print(lista_contador)
print(lista_contador.index('Hola'))
print('\n')