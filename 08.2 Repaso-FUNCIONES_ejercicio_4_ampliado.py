#
#  ###  ENUNCIADO ORIGINAL  ###
#
# 4. Escribir una función que convierta un número decimal 
# en los otros dos sistemas: Binario y Hexadecimal. Mostrar 
# mensajes pertenecientes a cada función.
# 
# 
# ###  AMPLIACION  ###
# 
# Convertir un número ingresado en cualquier base menor o igual a
# 36, a otro número en cualquier base también menor o igual a 36
# 








'''
###  PRUEBAS VARIAS  ###

n = bin(30)
print(n[2:])

nu_05='100000'
nu_10 = int(nu_05, 5)
print(f'{nu_05} en base 5 == {nu_10} en base 10\n')

ns = str(5)
print(type(ns))

#print(int('f', 16))
#print(hex(15)[2:])

n = '40'
print(int(n, 11))
print(36**2)

try: a = int('12', 2); print(a)
except ValueError: print('alguito')

'''








'''
# prueba para salir de una función sin que finalice el programa
# (por caso de que se lo quiera seguir utilizano y no tener que relanzarlo)

def calcular_raiz_cuadrada(numero):
	if numero < 0:
		print("El número debe ser no negativo")
		return

	print('printeo algo')

	return 8

calcular_raiz_cuadrada(-8)
print(calcular_raiz_cuadrada(9))
'''








'''
# de decimal a base 9

def decimal_a_base9(numero):
    if numero == 0:
        return "0"

    resultado = ""
    negativo = False
    if numero < 0:
        negativo = True
        numero = abs(numero)

    while numero > 0:
        digito = numero % 9
        resultado = str(digito) + resultado
        numero //= 9

    if negativo:
        resultado = "-" + resultado

    return resultado


numero_decimal = nu_10
numero_base9 = decimal_a_base9(numero_decimal)

print(f"Número decimal: {numero_decimal}")
print(f"Número en base 9: {numero_base9}\n")
'''








'''
# de base 5 a base 9

def base5_a_base9(numero):
    if not all(digito.isdigit() and int(digito) < 5 for digito in str(numero)):
        raise ValueError("El número debe estar en base 5")

    decimal = int(str(numero), 5)
    base9 = ""

    while decimal > 0:
        digito = decimal % 9
        base9 = str(digito) + base9
        decimal //= 9

    return base9


numero_base5 = nu_05
numero_base9 = base5_a_base9(numero_base5)

print(f"Número en base 5: {numero_base5}")
print(f"Número en base 9: {numero_base9}")
'''








'''
# de bases menores o iguales a 10, a bases menores o iguales a 10

def base_a_base(baseEntrada, numero, baseSalida):
	if baseEntrada > 10:
		print('El número debe estar en una base menor o igual a 10.')
		return

	if not all(digito.isdigit() and int(digito) < baseEntrada for digito in str(numero)):
		print(f'El número debe estar en base {baseEntrada}')
		return

	if int(numero) == 0:
		print('Cero == cero')
		return


	decimal = int(str(numero), baseEntrada)
	salida = ""

	while decimal > 0:
		digito = decimal % baseSalida
		salida = str(digito) + salida
		decimal //= baseSalida

	print(f'{numero} en base {baseEntrada} == {salida} en base {baseSalida}')


numero_ent = '13'
base_a_base(3, numero_ent, 16)
'''








'''
# convertir un número de base 10 a base menor o igual a 36
# (sólo disponemos de 26 símbolos alfabéticos o símbolos directos,
# pero se puede producir salida con la base de cualquier tamaño si
# dispusiéramos de símbolos suficientes)

def base10_a_base_36(numero, baseSalida):
	if numero == 0:
		print('Cero == cero')
		return

	# imprimo el número ingresado antes de que sea
	# utilizado o transformado en la función
	print(numero, end='')

	digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	salida = ""

	while numero > 0:
		digito = numero % baseSalida
		salida = digitos[digito] + salida
		numero //= baseSalida

	#print(f' en base 10 == {salida} en base {baseSalida}')


#base10_a_base_36(30, 36)
'''








'''
'''
# convertir un número de bases menores o iguales a
# 36, a un número de bases menores o iguales a 36
#
# igual que antes, se podría trabajar con bases de
# salida iguales al número de símbolos disponibles
#
# para transformación de números de entrada utilizo la función "int"
# de Python, que sólo admite números con una base máxima igual a 36
#
#
#  ###  ATENCION  ###
# números en bases mayores que 10 conviene ingresarlos entrecomillados
# números que incluyen letras deben ir si o si entrecomillados, ya que
# sin comillas Python entiende que son el nombre de una variable

def base_36_a_base_36(baseEntrada, numero, baseSalida):
	# capturo una base incorrecta ingresada y finalizo la función
	if baseEntrada > 36 or baseSalida > 36:
		print('La base máxima de entrada o salida debe ser 36.')
		return

	# capturo el uno o el cero si son ingresados y finalizo la función
	if numero == 0: print('Cero == cero'); return
	if numero == 1: print('1 == 1'); return

	# paso el número ingresado en cualquier base, a decimal
	# y en el mismo paso constato que pueda el número ingresado
	# concuerde con la base asignada para dicho número
	try:
		numeroDec = int(str(numero), baseEntrada)
	# si no concuerda capturo el error y finalizo la función
	except ValueError:
		print('El número no coincide con la base declarada.')
		return

	# declaro los "dígitos" o símbolos que se
	# utilizarán para formar el número de salida
	digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	# declaro la variable que será la salida
	salida = ""

	# ESTRUCTURA CENTRAL DE LA FUNCION
	# con esta estructura convertimos cualquier número en base
	# 10 (decimal) a un número en cualquier base hasta 36
	while numeroDec > 0:
		digito = numeroDec % baseSalida
		salida = digitos[digito] + salida
		numeroDec //= baseSalida

	print(f'{numero} en base {baseEntrada} == {salida} en base {baseSalida}')


# números que incluyen letras deben ir si o si entrecomillados, ya que
# sin comillas Python entiende que son el nombre de una variable
base_36_a_base_36(33, 'y', 10)







'''
# la misma función anterior pero "desnudita"
def base_36_a_base_36_b(baseEntrada, numero, baseSalida):
	if baseEntrada > 36 or baseSalida > 36:
		print('La base máxima de entrada o salida debe ser 36.')
		return

	if numero == 0: print('Cero == cero'); return
	if numero == 1: print('1 == 1'); return

	try: numeroDec = int(str(numero), baseEntrada)
	except ValueError: print('El número no coincide con la base declarada.'); return

	digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	salida = ""

	while numeroDec > 0:
		digito = numeroDec % baseSalida
		salida = digitos[digito] + salida
		numeroDec //= baseSalida

	print(f'{numero} en base {baseEntrada} == {salida} en base {baseSalida}')
'''



