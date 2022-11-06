# Trabajando con variables

'''
# imprime nombre de variable
nombre_curso='Python'
print('Bienvenido al curso de ' + nombre_curso)

#solicitando variable
nombre_curso = input('ingrese nombre del curso:')
print('Bienvenido al curso de ' + nombre_curso)

estudiante1, estudiante2, estudiante3='Pablo','Luz','Kiara'
print(estudiante1,estudiante2,estudiante3)

mensaje ='Aprender python es muy fácil'
print('El varlor de mi variable es: '+ mensaje)

'''

mensaje ='Aprender python es muy fácil'
print('El varlor de mi variable es:{}'.format(mensaje))

mensaje ='Aprender python es muy fácil'
print(f'El varlor de mi variable es: {mensaje}')