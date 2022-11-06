#Conversiones

numero1 = 9
numero2=1
suma = numero1 + numero2

print('El resultado es ' + str(suma))


numero_decimal=1.2
print(type(numero_decimal))


numero_decimal=str(1.2)
print(type(numero_decimal))

booleano = str(True)
print(type(booleano))

numero_entero = 6
texto='2.4'
print(type(numero_entero), ' ' ,type(texto))

#convertir a número flotante
texto=float('2.4')
print(type(texto))


#convertir a tipos de datos enteros
numero_decimal = 2.7
texto = '5'
print(type(numero_decimal), ' ' ,type(texto))

numero_decimal = int(2.7)
texto = int('5')
print(type(numero_decimal), ' ' ,type(texto))

#convertir a booleanos
print(bool(0), ' ', bool(''),' ', bool('Hola'), ' ',bool(1.2))

#convertir texto a entero no se puede
print(int('Convierteme a entero'))
