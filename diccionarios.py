# Diccionarios en python

mi_diccionario = {}
print(type(mi_diccionario))

diccionario_traduccion = {'Hola':'Hello', 'Rojo':'Red','Black':'Negro'}
print(diccionario_traduccion)

# Cambiando valor de un item del diccionario
diccionario_traduccion ['Rojo']='Rojito'
print(diccionario_traduccion)


# para eliminar items del diccionario
del(diccionario_traduccion['Hola'])
print(diccionario_traduccion)

# Creamos otro diccionario
estudiante = {
'Nombre':'Juan',
'Apellido':'Jaramillo',
'Edad':38,
'Curso':'Python'
}
print(estudiante)

estudiante = {
'Nombre':'Juan',
'Apellido':'Jaramillo',
'Edad':38,
'Curso':[
        {'Nombre':'Python','Nivel':'Básico'},
        {'Nombre':'Javascript','Nivel':'Avanzado'},
        {'Nombre':'PHP','Nivel':'Master'}
        ]
}
print(estudiante)

print('\n')

estudiante1 = {
'Nombre':'Juan',
'Apellido':'Jaramillo',
'Edad':38,
'Curso':[
        {'Nombre':'Python','Nivel':'Básico'},
        {'Nombre':'Javascript','Nivel':'Avanzado'},
        {'Nombre':'PHP','Nivel':'Master'}
        ]
}

estudiante2 = {
'Nombre':'Luz',
'Apellido':'Altuna',
'Edad':29,
'Curso':[
        {'Nombre':'Python','Nivel':'Básico'},
        {'Nombre':'Javascript','Nivel':'Avanzado'},
        {'Nombre':'PHP','Nivel':'Master'}
        ]
}

estudiantes = []
estudiantes.append(estudiante1)
estudiantes.append(estudiante2)
print(estudiantes)

print('\n')