# Importo la función "sleep" para demorar un poquito la ejecución del código
# entre la carga de los datos por el usuario y la salida en pantalla (sólo para
# diversión)

from time import sleep

'''
  ================================================================
    EJERCICIOS ESTRUCTURA CONDICIONAL SIMPLE
  ================================================================


EJERCICIO 1. Realice un programa que solicite dos letras ingresadas por el
usuario y verifique si son iguales o no, mostrando un mensaje.

primera_letra = input('Ingresa una letra: ')
segunda_letra = input('Ingresa una letra más por favor: ')
print('Vamos a comprobar si las letras son iguales ...')

sleep(2)

if (primera_letra == segunda_letra):
	print('¡Las dos letras son iguales!')
else:
	print('Las dos letras no son iguales... bleh')


  ================================================================


EJERCICIO 2. Hacer un programa que permita decidir si dos palabras son iguales
o diferentes. Mostrar mensaje por pantalla.

primera_palabra = input('Ingresa una palabra: ')
segunda_palabra = input('Ingresa una palabra más por favor: ')
print('Vamos a comprobar si las palabras son iguales ...')

sleep(2)

if (primera_palabra == segunda_palabra):
	print('¡Las dos palabras son iguales!')
else:
	print('Las dos palabras no son iguales... bleh')


  ================================================================


EJERCICIO 3. Realizar un programa que permita ingresar “f” o “m” y determinar
si vota en mesa femenina o masculina.

print('Usted está a punto de emitir un voto.')
print('Para votar en mesa femenina ingrese "f", o para votar en mesa masculina ingrese "m".')
opcion = input('Su opción es: ')

if (opcion == 'f' or opcion == 'F'):
	print('Usted vota en mesa femenina.')
elif (opcion == 'm' or opcion == 'M'):
	print('Usted vota en mesa masculina.')
else:
	print('Usted ha ingresado una opción incorrecta.')


  ================================================================


EJERCICIO 4. Realice un programa que lea dos números y diga cuál es el mayor.

primer_numero = input('Ingresa un número: ')
segundo_numero = input('Ingresa un número más por favor: ')
print('Vamos a comprobar cuál de los dos números es el mayor ...')

sleep(2)

if (primer_numero > segundo_numero):
	print('¡El primer número es el mayor!')
elif (primer_numero < segundo_numero):
	print('¡El segundo número es el mayor!')
else:
	print('¡CHAN! ¡Los dos números son iguales!')


  ================================================================


EJERCICIO 5. Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo
el cambio de dólares a pesos y que sea el usuario quien decida qué tipo de cambio
quiere, si de dólares a pesos o viceversa.


print('Si desea cambiar pesos a dólares ingrese "p", si desea cambiar dólares a pesos ingrese "d".')
opcion = input('Su opción es: ')

if (opcion == 'p' or opcion == 'P'):
	# si elige pesos pido la cantidad de pesos a cambiar
	cant_pesos = input('Ingrese la cantidad de pesos a cambiar: ')
	# hago el cambio de dólares a pesos y redondeo a dos decimales
	cambio_peso_dolar = round((float(cant_pesos) / 400), 2)
	# imprimo el resultado
	print(cant_pesos + ' pesos equivalen a ' + str(cambio_peso_dolar) + ' dólares.')
elif (opcion == 'd' or opcion == 'D'):
	# si elige dólares pido la cantidad de dólares a cambiar
	cant_dolares = input('Ingrese la cantidad de dólares a cambiar: ')
	# hago el cambio de pesos a dólares y redondeo a dos decimales
	cambio_dolar_peso = round((float(cant_dolares) * 400), 2)
	# imprimo el resultado
	print(cant_dolares + ' dólares equivalen a ' + str(cambio_dolar_peso) + ' pesos.')
else:
	print('Usted ha ingresado una opción incorrecta.')


  ================================================================


EJERCICIO 5. Mejorado según la clase del 22.05.23

Pequeño código de prueba para meter un while y repetir la operación

continuar = True
while continuar:
	letrita = input('ingresa un carácter: ')
	print(letrita)
	decidir = input('presiona una tecla para repetir, para salir presiona "s": ')
	if decidir == 's':
		print('gracias')
		break
	print()
'''


# envuelvo todo el código en un bucle while simulando un comoportamiento "do-while"
while True:

	# inicio la ejecución del programa pidiendo la moneda que desea cambiar la persona
	print('Si desea cambiar pesos a dólares ingrese "p", si desea cambiar dólares a pesos ingrese "d".')
	opcion = input('Su opción es: ')

	# pido el tipo de cambio según lo que haya elegido antes
	if opcion == 'p' or opcion == 'P':
		# si eligió pesos pido el precio de venta del día
		tipo_venta = float(input('Ingrese el precio de venta del dolar: '))
	elif opcion == 'd' or opcion == 'D':
		# si eligió dólares pido el precio de compra del día
		tipo_compra = float(input('Ingrese el precio de compra del dolar: '))
	else:
		print('Usted ha ingresado una opción incorrecta.')


	# realizo las conversiones
	# lo hago en un bloque de código separado para mayor claridad al momento de leerlo
	if opcion == 'p' or opcion == 'P':
		# si eligió pesos pido la cantidad de pesos a cambiar
		cant_pesos = input('Ingrese la cantidad de pesos a cambiar: ')
		# hago el cambio de dólares a pesos y redondeo a dos decimales
		cambio_peso_dolar = round((float(cant_pesos) / tipo_venta), 2)
		# imprimo el resultado
		print(cant_pesos + ' pesos equivalen a ' + str(cambio_peso_dolar) + ' dólares.')
	# la opción "if" es para que se ejecute exclusivamente si se introdujo "d" o "D"
	# dado que no hay otras opcines luego en este grupo, no uso un "elif"
	if opcion == 'd' or opcion == 'D':
		# si eligió dólares pido la cantidad de dólares a cambiar
		cant_dolares = input('Ingrese la cantidad de dólares a cambiar: ')
		# hago el cambio de pesos a dólares y redondeo a dos decimales
		cambio_dolar_peso = round((float(cant_dolares) * tipo_compra), 2)
		# imprimo el resultado
		print(cant_dolares + ' dólares equivalen a ' + str(cambio_dolar_peso) + ' pesos.')


	# pregunto al usuario si desea realizar otra conversión
	decidir = input('Para realizar otra conversión presiona una tecla, para salir presiona "s": ')
	# en caso de que el usuario no desee volver a intentarlo salgo del bucle
	# y finaliza el programa
	print()
	if decidir == 's' or decidir == 'S':
		print('Gracias por utilizar la herramienta.')
		break


'''
  ================================================================


EJERCICIO 6. Realice un programa donde el usuario ingrese su edad. Si es mayor
de 16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.

edad = int(input('Ingrese su edad: '))
print('Vamos a ver qué hacemos con usted ...')

sleep(2)

if (edad > 16):
	print('Usted puede votar.')
else:
	print('No vota.')


  ================================================================
    EJERCICIOS ESTRUCTURA CONDICIONAL COMPUESTA (IF anidados)
  ================================================================


EJERCICIO 1. Introducir los lados de un triángulo y visualizar por pantalla si
dicho triángulo es equilátero, isósceles o escaleno.

lado1 = float(input('Introduzca el primer lado del triángulo: '))
lado2 = float(input('Introduzca el segundo lado del triángulo: '))
lado3 = float(input('Introduzca el tercer lado del triángulo: '))

if lado1 == lado2 == lado3:
	print('¡El triángulo es equilátero!')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
	print('¡El triángulo es isósceles!')
else:
	print('¡El triángulo es escaleno!')


  ================================================================


EJERCICIO 2. Realice un programa que le permita al usuario simular el pago
ingresando el importe y la forma de pago:
	• Contado (1): se aplica un descuento del 10% al importe
	• Tarjeta (2): se aplica un interés de 10%
	• Débito (3): se aplica un descuento del 5%
Mostrar el importe, el descuento o interés y el importe total.

importe = float(input('Ingrese el importe a pagar: '))

print(
	'\nIngrese la forma de pago de la siguiente manera:\n',
	'• Contado (1): se aplica un descuento del 10% al importe\n',
	'• Tarjeta (2): se aplica un interés de 10%\n',
	'• Débito (3): se aplica un descuento del 5%\n'
)

forma_pago = int(input('Su elección es: '))

descuento = 0
interes = 0
final = 0

if forma_pago == 1:
	descuento = round((importe * 0.1), 2)
	final = importe * 0.9
elif forma_pago == 2:
	interes = round((importe * 0.1))
	final = round((importe * 1.1), 2)
elif forma_pago == 3:
	descuento = round((importe * 0.05), 2)
	final = round((importe * 0.95), 2)

print(
	'\n • El importe a pagar es:', importe, '\n',
	'• Descuento:', descuento, '\n',
	'• Interés:', interes, '\n',
	'• El importe total es:', final, '\n'
)


  ================================================================


EJERCICIO 3. Realice un programa que lea tres números, muestre cuál es el mayor
y determine si es par o impar.

primer_numero = float(input('Ingresa un número: '))
segundo_numero = float(input('Ingresa un número más: '))
tercer_numero = float(input('Ingresa otro número más por favor: '))

if primer_numero > segundo_numero and primer_numero > tercer_numero:
	print('\n¡El primer número es el mayor!')
	if primer_numero % 2 == 0: print('Y además es par.')
	else: print('Y además es impar.')
elif segundo_numero > primer_numero and segundo_numero > tercer_numero:
	print('\n¡El segundo número es el mayor!')
	if segundo_numero % 2 == 0: print('Y además es par.')
	else: print('Y además es impar.')
else:
	print('\n¡El tercer número es el mayor!')
	if tercer_numero % 2 == 0: print('Y además es par.')
	else: print('Y además es impar.')


  ================================================================


EJERCICIO 4. Confeccione un programa que pida un número del 1 al 7 y diga el día
de la semana correspondiente.

dia = int(input('Ingrese un número del 1 al 7: '))

if dia == 1 : print('¡El día ingresado es Lunes!')
elif dia == 2 : print('¡El día ingresado es Martes!')
elif dia == 3 : print('¡El día ingresado es Miércoles!')
elif dia == 4 : print('¡El día ingresado es Jueves!')
elif dia == 5 : print('¡El día ingresado es Viernes!')
elif dia == 6 : print('¡El día ingresado es Sábado!')
elif dia == 7 : print('¡El día ingresado es Domingo!')
else: print('Usted ha ingresado una opción incorrecta.')


  ================================================================

EJERCICIO 5. Realice un programa que pida un número del 1 al 12 y diga el nombre
del mes correspondiente.


mes = input('Ingrese un número del 1 al 12: ')

if mes == '1' : mes = 'Enero'
elif mes == '2' : mes = 'Febrero'
elif mes == '3' : mes = 'Marzo'
elif mes == '4' : mes = 'Abril'
elif mes == '5' : mes = 'Mayo'
elif mes == '6' : mes = 'Junio'
elif mes == '7' : mes = 'Julio'
elif mes == '8' : mes = 'Agosto'
elif mes == '9' : mes = 'Setiembre'
elif mes == '10' : mes = 'Octubre'
elif mes == '11' : mes = 'Noviembre'
elif mes == '12' : mes = 'Diciembre'
else: print('Usted ha ingresado una opción incorrecta.')

print('¡El mes ingresado es ' + mes + '!')
'''