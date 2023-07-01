'''
  ================================================
                  REPASO FUNCIONES
  ================================================


Repaso1 decoradores del canal en yt Píldoras Informáticas
Recurso: https://www.youtube.com/embed/DQXm6bIZgvk


def funcion_decoradora(funcio_parametro):
	def funcion_interior():
		# Acciones adicionales que agregan
		print('Vamos a realizar un cálculo:')

		funcio_parametro()

		# Más acciones
		print('Hemos terminado el cálculo.\n')

	return funcion_interior


@funcion_decoradora
def suma():
	print(3+5)

@funcion_decoradora
def resta():
	print(5-3)

suma()
resta()
#funcion_decoradora(suma())


======== ======== ======== ======== ======== ======== ======== ========


Repaso2 decoradores del canal en yt Píldoras Informáticas
Recurso: https://www.youtube.com/embed/_IwlE3Z7U04
Recurso2: https://www.youtube.com/embed/KOw0tpcspH4


def funcion_decoradora(funcio_parametro):
	def funcion_interior(*args, **kwargs):
		# Acciones adicionales que agregan
		print('Vamos a realizar un cálculo:')

		funcio_parametro(*args, **kwargs)

		# Más acciones
		print('Hemos terminado el cálculo.\n')

	return funcion_interior


@funcion_decoradora
def suma(num1, num2, num3):
	print(num1 + num2 + num3)

@funcion_decoradora
def resta(num1, num2):
	print(num1 - num2)

#@funcion_decoradora
#def sumita():
#	print(3+5)
#sumita()

@funcion_decoradora
def potencia(base, exponente):
	print(pow(base, exponente))


suma(5,3,9)
resta(5,3)
#funcion_decoradora(suma())
potencia(base=5,exponente=3)


======== ======== ======== ======== ======== ======== ======== ========


Ejemplo pasado por un compañero (sacado de chatGPT)
'''
'''


def imprimir_tipo_triangulo(func):
    def wrapper(*args):
        tipo = func(*args)
        print("El triángulo es:", tipo)
        return tipo
    return wrapper

# Función para verificar si los lados forman un triángulo
def es_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Funciones para determinar el tipo de triángulo

@imprimir_tipo_triangulo
def tipo_equilatero(a, b, c):
    if es_triangulo(a, b, c) and a == b == c:
        return "Equilátero"
    return "No es un triángulo equilátero"

@imprimir_tipo_triangulo
def tipo_isosceles(a, b, c):
    if es_triangulo(a, b, c) and (a == b or a == c or b == c):
        return "Isósceles"
    return "No es un triángulo isósceles"

@imprimir_tipo_triangulo
def tipo_rectangulo(a, b, c):
    if es_triangulo(a, b, c):
        lados = [a, b, c]
        lados.sort()
        if lados[0]*2 + lados[1] == lados[2]*2:
            return "Rectángulo"
    return "No es un triángulo rectángulo"

# Solicitar al usuario los lados del triángulo
a = float(input("Ingrese el primer lado del triángulo: "))
b = float(input("Ingrese el segundo lado del triángulo: "))
c = float(input("Ingrese el tercer lado del triángulo: "))

# Calcular y mostrar el tipo de triángulo
tipo_equilatero(a, b, c)
tipo_isosceles(a, b, c)
tipo_rectangulo(a, b, c)


======== ======== ======== ======== ======== ======== ======== ========


1. Realice un programa que contengan funciones de los tres tipos de triángulos.
Los mismos deben estar acompañados de los mensajes respecto a la función
decoradora. Para mejorarlo pueden agregar los nombres de cada función según los
triángulos.

# Basándome en los ejemplos anteriores y con algunas modificaciones, implemento
# el ejercicio

# Pequeña prueba
print("Línea 1", end="")
print("Línea 2")


def funcion_pre_titulo(funcio_parametro):
	def funcion_interior(*args):
		# Agrego un "pre-título"
		print('El triángulo ', end="")

		funcio_parametro(*args)

	return funcion_interior



def es_triangulo(a, b, c):
	return a + b > c and a + c > b and b + c > a

@funcion_pre_titulo
def tipo_equilatero(a, b, c):
	if es_triangulo(a, b, c):
		if a == b == c: print("Es equilátero")
		else: print("No es equilátero")
	else: print("No existe")

@funcion_pre_titulo
def tipo_isosceles(a, b, c):
	if es_triangulo(a, b, c):
		if (a == b or a == c or b == c): print("Es isósceles")
		else: print("No es isósceles")
	else: print("No existe")

@funcion_pre_titulo
def tipo_rectangulo(a, b, c):
	if es_triangulo(a, b, c):
		lados = [a, b, c]
		lados.sort()
		if lados[0]*2 + lados[1] == lados[2]*2: print("Es rectángulo")
		else: print("No es rectángulo")
	else: print("No existe")




# Solicitamos los lados del triángulo
a = float(input("Ingrese el primer lado del triángulo: "))
b = float(input("Ingrese el segundo lado del triángulo: "))
c = float(input("Ingrese el tercer lado del triángulo: "))

# Calcular y mostrar el tipo de triángulo
tipo_equilatero(a, b, c)
tipo_isosceles(a, b, c)
tipo_rectangulo(a, b, c)


======== ======== ======== ======== ======== ======== ======== ========


2. Realizar un programa de funciones que contengan funciones con bucles y control
de flujo fuera de la función decoradora. Al menos se deben tener dos condicionales
o bucles.
'''


from time import sleep


def funcion_iniciador(funcio_parametro):
	def funcion_interior(*args):
		# Agrego un "pre-título"
		print('¿Qué fue primero?')

		funcio_parametro(*args)

	return funcion_interior


@funcion_iniciador
def el_cuento_de_la_gallina(dato):
	print('¿La gallina?')
	for i in range(dato):
		sleep(0.1), print('¿O el huevo?')
		sleep(0.1), print('¿O la gallina?')


while True:
	dato = int(input('Tirá un número: '))

	if dato > 100: print('Te pasaste, tirá un número más bajo :)')
	else: el_cuento_de_la_gallina(dato)

	print('\n¿Querés probar de nuevo? Presiona una tecla..')
	decidir = input('Para salir presiona "s": ')
	if decidir == 's':
		break
	print()
	print()



'''
======== ======== ======== ======== ======== ======== ======== ========


3. Escribir una función que calcule el total de una factura tras aplicarle el
IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar,
y devolver el total de la factura. Si se invoca la función sin pasarle el
porcentaje de IVA, deberá aplicar un 21%.


def calcIVA(subtotal, iva=21):
	total = subtotal * iva / 100 + subtotal

	print('El monto ingresado (sin IVA) es: $', subtotal)
	print('El monto ingresado una vez aplicado el IVA es: $', total)


calcIVA(200)
#calcIVA(200,11)


======== ======== ======== ======== ======== ======== ======== ========


4. Escribir una función que convierta un número decimal en los otros dos sistemas:
Binario y Hexadecimal. Mostrar mensajes pertenecientes a cada función.


def conversor(decimal):
	# obtengo el binario a partir del número pasado como parámetro
	# dejo afuera los dos primeros caracteres ya que la función "bin" los agrega
	# para indicar que es un número en base 2
	binario = bin(decimal)[2:]
	print('El número introducido en el sistema binario es >>', binario)

	# obtengo el octal igual que antes, y cuento a partir del tercer caracter
	octal = oct(decimal)[2:]
	print('El número introducido en el sistema octal es >>', octal)

	# todo igual pero para hexadecimal
	hexa = hex(decimal)[2:]
	print('El número introducido en el sistema hexa es >>', hexa)


# meto todo en un bucle while para realizar varias veces la operación si se desea
while True:
	dec = int(input('Ingrese un número: '))
	conversor(dec)

	decidir = input('Presiona una tecla para repetir, para salir presiona "s": ')
	if decidir == 's':
		break
	print()
	print()
'''

