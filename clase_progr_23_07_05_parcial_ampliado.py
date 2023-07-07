'''
# Realizar un programa en Python que conste de la conversión de °C a °F, °K.
#
# El mismo debe permitirle al usuario el ingreso del número a convertir en el
# tipo de dato que se considere correspondiente y con un mensaje que justifique
# cada conversión mostrándolo por pantalla.
# ======== ======== ======== ======== ======== ======== ======== ========
#
# Mejorado incluyendo todas las escalas de temperatura conocidas, actuales y en
# desuso, y permitiendo la elección del tipo ingresado
# ======== ======== ======== ======== ======== ======== ======== ========
#
#
#
#  ###  Abreviaturas utilizadas:  ###
#  celc = Celcius    = (°C) = Centígrados 
#  fahr = Fahrenheit = (°F)
#  kelv = Kelvin     = (°K)
#  rank = Rankine    = (°R)
#  reau = Réaumur    = (°Ré)
#  newt = Newton     = (°N)
#  rome = Rømer      = (°Rø)
#
#
#
#  ### Tabla de todas las conversiones  ###

+--------------+----------------------+------------------------+-----------------------------+----------------------------+-----------------------+-------------------------+-----------------------------+
|              | Celsius (°C)         | Fahrenheit (°F)        | Kelvin (°K)                 | Rankine (°R)               | Réaumur (°Ré)         | Newton (°N)             | Rømer (°Rø)                 |
+--------------+----------------------+------------------------+-----------------------------+----------------------------+-----------------------+-------------------------+-----------------------------+
| Celsius (°C) |      -               | °F = °C×9/5+32         | °K = °C+273.15              | °R = (°C+273.15)×9/5       | °Ré = °C×4/5          | °N = °C×33/100          | °Rø = °C×21/40+7.5          |
| Fahrenheit ()| °C = (°F-32)×5/9     |      -                 | °K = (°F+459.67)×5/9        | °R = °F+459.67             | °Ré = (°F-32)×4/9     | °N = (°F-32)×11/60      | °Rø = (°F-32)×7/24+7.5      |
| Kelvin (°K)  | °C = °K-273.15       | °F = °K×9/5-459.67     |      -                      | °R = °K×9/5                | °Ré = (°K-273.15)×4/5 | °N = (°K-273.15)×33/100 | °Rø = (°K-273.15)×21/40+7.5 |
| Rankine (°R) | °C = (°R-491.67)×5/9 | °F = °R-459.67         | °K = °R×5/9                 |      -                     | °Ré = (°R-491.67)×4/9 | °N = (°R-491.67)×11/60  | °Rø = (°R-491.67)×7/24+7.5  |
| Réaumur (°Ré)| °C = °Ré×5/4         | °F = °Ré×9/4+32        | °K = °Ré×5/4+273.15         | °R = °Ré×9/4+491.67        |       -               | °N = °Ré×33/80          | °Rø = °Ré×7/32+7.5          |
| Newton (°N)  | °C = °N×100/33       | °F = °N×60/11+32       | °K = °N×100/33+273.15       | °R = °N×60/11+491.67       | °Ré = °N×80/33        |      -                  | °Rø = °N×35/22+7.5          |
| Rømer (°Rø)  | °C = (°Rø-7.5)×40/21 | °F = (°Rø-7.5)×24/7+32 | °K = (°Rø-7.5)×40/21+273.15 | °R = (°Rø-7.5)×24/7+491.67 | °Ré = (°Rø-7.5)×32/21 | °N = (°Rø-7.5)×22/35    |       -                     |
+--------------+----------------------+------------------------+-----------------------------+----------------------------+-----------------------+-------------------------+-----------------------------+
'''


print(
	'Conversor de todas las escalas de temperatura conocidas, actuales y en desuso.\n'
	'Primero selecciona la escala (el tipo) de la temperatura que deseas convertir,\n'
	'ingresando una letra según la siguiente tabla:\n\n'
	'| Celsius | Fahrenheit | Kelvin | Rankine | Réaumur | Newton | Rømer |\n'
	'+---------+------------+--------+---------+---------+--------+-------+\n'
	'|    c    |     f      |   k    |    r    |   re    |   n    |  ro   |\n\n'	
)


# Función principal. Aquí re realizan todas las conversiones según la escala 
# elegida e introducida como el primer parámetro de la función
def conversorTemp(escala, magnitud):
	# Operación secundaria. Aquí se realiza la conversión de la temperatura
	# ingresada en Celcius a todas las demás escalas
	if escala == 'c':
		celc = magnitud
		celc_fahr = round(((celc * 9/5) + 32), 2)
		celc_kelv = round((celc + 273.15), 2)
		celc_rank = round(((celc + 273.15) * 9/5), 2)
		celc_reau = round((celc * 4/5), 2)
		celc_newt = round((celc * 33/100), 2)
		celc_rome = round((celc * 21/40 + 7.5), 2)

		# Se imprimen todos los resultados para esta escala (elegida)
		print(magnitud, 'grados Celcius equivalen a:')
		print(celc_fahr, 'grados Fahrenheit' )
		print(celc_kelv, 'grados Kelvin')
		print(celc_rank, 'grados Rankine')
		print(celc_reau, 'grados Réaumur')
		print(celc_newt, 'grados Newton')
		print(celc_rome, 'grados Rømer')


	# Operación secundaria. Aquí se realiza la conversión de la temperatura
	# ingresada en Fahrenheit a todas las demás escalas
	elif escala == 'f':
		fahr = magnitud
		fahr_celc = round(((fahr - 32) * 5/9), 2)
		fahr_kelv = round(((fahr + 459.67) * 5/9), 2)
		fahr_rank = round((fahr + 459.67), 2)
		fahr_reau = round(((fahr - 32) * 4/9), 2)
		fahr_newt = round(((fahr - 32) * 11/60), 2)
		fahr_rome = round(((fahr - 32) * 7/24 + 7.5), 2)

		# Se imprimen todos los resultados para esta escala (elegida)
		print(magnitud, 'grados Fahrenheit equivalen a:')
		print(fahr_celc, 'grados Celcius' )
		print(fahr_kelv, 'grados Kelvin')
		print(fahr_rank, 'grados Rankine')
		print(fahr_reau, 'grados Réaumur')
		print(fahr_newt, 'grados Newton')
		print(fahr_rome, 'grados Rømer')


	# Operación secundaria. Aquí se realiza la conversión de la temperatura
	# ingresada en Kelvin a todas las demás escalas
	elif escala == 'k':
		kelv = magnitud
		kelv_celc = round((kelv - 273.15), 2)
		kelv_fahr = round((kelv * 9/5 - 459.67), 2)
		kelv_rank = round((kelv * 9/5), 2)
		kelv_reau = round(((kelv - 273.15) * 4/5), 2)
		kelv_newt = round(((kelv - 273.15) * 33/100), 2)
		kelv_rome = round(((kelv - 273.15) * 21/40 + 7.5), 2)

		# Se imprimen todos los resultados para esta escala (elegida)
		print(magnitud, 'grados Kelvin equivalen a:')
		print(kelv_celc, 'grados Celcius' )
		print(kelv_fahr, 'grados Fahrenheit' )
		print(kelv_rank, 'grados Rankine')
		print(kelv_reau, 'grados Réaumur')
		print(kelv_newt, 'grados Newton')
		print(kelv_rome, 'grados Rømer')


	# Operación secundaria. Aquí se realiza la conversión de la temperatura
	# ingresada en  a todas las demás escalas
	elif escala == 'r':
		rank = magnitud
		rank_celc = round(((rank - 491.67) * 5/9), 2)
		rank_fahr = round((rank - 459.67), 2)
		rank_kelv = round((rank * 5/9), 2)
		rank_reau = round(((rank - 491.67) * 4/9), 2)
		rank_newt = round(((rank - 491.67) * 11/60), 2)
		rank_rome = round(((rank - 491.67) * 7/24 + 7.5), 2)

		# Se imprimen todos los resultados para esta escala (elegida)
		print(magnitud, 'grados Rankine equivalen a:')
		print(rank_celc, 'grados Celcius' )
		print(rank_fahr, 'grados Fahrenheit' )
		print(rank_kelv, 'grados Kelvin')
		print(rank_reau, 'grados Réaumur')
		print(rank_newt, 'grados Newton')
		print(rank_rome, 'grados Rømer')


	# Operación secundaria. Aquí se realiza la conversión de la temperatura
	# ingresada en Réaumur a todas las demás escalas
	elif escala == 're':
		reau = magnitud
		reau_celc = round((reau * 5/4), 2)
		reau_fahr = round((reau * 9/4 + 32), 2)
		reau_kelv = round((reau * 5/4 + 273.15), 2)
		reau_rank = round((reau * 9/4 + 491.67), 2)
		reau_newt = round((reau * 33/80), 2)
		reau_rome = round((reau * 7/32 + 7.5), 2)

		# Se imprimen todos los resultados para esta escala (elegida)
		print(magnitud, 'grados Réaumur equivalen a:')
		print(reau_celc, 'grados Celcius' )
		print(reau_fahr, 'grados Fahrenheit' )
		print(reau_kelv, 'grados Kelvin')
		print(reau_rank, 'grados Rankine')
		print(reau_newt, 'grados Newton')
		print(reau_rome, 'grados Rømer')


	# Operación secundaria. Aquí se realiza la conversión de la temperatura
	# ingresada en Newton a todas las demás escalas
	elif escala == 'n':
		newt = magnitud
		newt_celc = round((newt * 100/33), 2)
		newt_fahr = round((newt * 60/11 + 32), 2)
		newt_kelv = round((newt * 100/33 + 273.15), 2)
		newt_rank = round((newt * 60/11 + 491.67), 2)
		newt_reau = round((newt * 80/33), 2)
		newt_rome = round((newt * 35/22 + 7.5), 2)

		# Se imprimen todos los resultados para esta escala (elegida)
		print(magnitud, 'grados Newton equivalen a:')
		print(newt_celc, 'grados Celcius' )
		print(newt_fahr, 'grados Fahrenheit' )
		print(newt_kelv, 'grados Kelvin')
		print(newt_rank, 'grados Rankine')
		print(newt_reau, 'grados Réaumur')
		print(newt_rome, 'grados Rømer')


	# Operación secundaria. Aquí se realiza la conversión de la temperatura
	# ingresada en Rømer a todas las demás escalas
	elif escala == 'ro':
		rome = magnitud
		rome_celc = round(((rome - 7.5) * 40/21), 2)
		rome_fahr = round(((rome - 7.5) * 24/7 + 32), 2)
		rome_kelv = round(((rome - 7.5) * 40/21 + 273.15), 2)
		rome_rank = round(((rome - 7.5) * 24/7 + 491.67), 2)
		rome_reau = round(((rome - 7.5) * 32/21), 2)
		rome_newt = round(((rome - 7.5) * 22/35), 2)

		# Se imprimen todos los resultados para esta escala (elegida)
		print(magnitud, 'grados Rømer equivalen a:')
		print(rome_celc, 'grados Celcius' )
		print(rome_fahr, 'grados Fahrenheit' )
		print(rome_kelv, 'grados Kelvin')
		print(rome_rank, 'grados Rankine')
		print(rome_reau, 'grados Réaumur')
		print(rome_newt, 'grados Newton')


	# Imprimimos un aviso en caso de ingreso/elección incorrecta de escala
	else:
		print('Ingresaste una opción no reconocida.')

	# Final de la función principal



# Metemos todo adentro del bucle while para 
# poder realizar cuantas operaciones se desee
while True:
	# Solicitamos el ingreso o la elección de una escala
	# según la tabla mostrada al principio del programa
	escala = input('Ingresa la escala elegida: ').lower()
	# Solicitamos el ingreso de la magnitud (cantidad de grados)
	magnitud = float(input('Ingresa una temperatura que desees convertir: '))

	# Llamamos a la función principal
	conversorTemp(escala, magnitud)

	# Con esta operación se decide si NO se sale del bucle y
	# por tanto se vuelve a realizar una nueva operación, o
	# al contrario se rompe el bucle con la sentencia "break"
	decidir = input('Presiona una tecla para repetir, para salir presiona "s": ').lower()
	if decidir == 's':
		break
	print()
	print()


