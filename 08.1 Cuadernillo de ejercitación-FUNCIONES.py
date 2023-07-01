'''
  =========================================
    CUADERNILLO DE EJERCITACION FUNCIONES
  =========================================


1. Realice un programa que muestre el mensaje "Hola Aula X (Indicar el número de
aula a la que pertenecen), ¿Qué tal?" en tres veces intercambiados entre ellos otro
mensajes a su elección.

num = int(input('Ingrese el número de aula: '))

def saludoAula(num):
	print(f'Hola Aula {num}. ¿Qué tal?\n')


print()
print('Primera invocación de la función.')
saludoAula(num)
print('Segunda invocación de la función.')
saludoAula(num)
print('Tercera invocación de la función.')
saludoAula(num)


  ================================================================


2. A partir del siguiente ejemplo "Hola Ana, ¿Qué tal?" realizar el programa la
ejecución del mismo con al menos otros dos nombres más, es decir, tres mensajes
con tres nombres distintos. Recuerda: en estos ejercicios trabajamos argumentos.

i = 0

def saludoPersonal(nombre):
	print(f'Hola {nombre}. ¿Qué tal?\n')

while i < 3:
	nombre = input('Ingrese un nombre: ')
	saludoPersonal(nombre)
	i+=1


  ================================================================


3. Realizar un programa de funciones que contengan 3 parámetros, el cual derive
en una suma. Mostrar el resultado dos veces.

def sumaTriple(num1, num2, num3):
	suma = num1 + num2 + num3
	print('El resultado de sumar los tres números ingresados es: ', suma)

primerN = int(input('Ingrese un número: '))
segundoN = int(input('Ingrese otro número: '))
tercerN = int(input('Ingrese uno más: '))

print()
sumaTriple(primerN, segundoN, tercerN)
sumaTriple(primerN, segundoN, tercerN)



  ================================================================


4. Realice un programa que lea dos números (dos parámetros), compare si son IGUALES,
en ese caso, mostrar un mensaje que muestre TRUE.

def igualdad(num1, num2):
	if num1 == num2: print('TRUE')
	else: print('ALGO')

n1000 = int(input('Ingrese un número: '))
n1001 = int(input('Ingrese otro número: '))

print()
igualdad(n1000, n1001)


  ================================================================


5. Realice un programa que contenga una función que se llame "sumayresta", que la
misma contenga dos variables locales nombradas suma y resta, respectivamente.
Recuerda: en estos ejercicios trabajamos argumentos para este ejercicio sería dos.

def sumayresta(algo, alguito):
	suma = None
	resta = None
	#if "suma" in locals() and "resta" in locals(): print('Las variables locales "suma" y "resta" existen.')
	if "suma" and "resta": print('Las variables locales "suma" y "resta" existen.')

sumayresta(3, 3)

'''
# Una implementación un poco más elaborada del mismo ejercicio

def sumayresta(num1, num2):
	suma = num1 + num2
	if num1 >= num2: resta = num1 - num2
	else: resta = num2 - num1
	print('La suma de los números ingresados es: ', suma)
	print('La diferencia de los números ingresados es: ', resta)

n1 = int(input('Ingrese un número: '))
n2 = int(input('Ingrese otro número: '))

sumayresta(n1, n2)

'''
  ================================================================



nombres=["Jose","Maria","Pedro","Lucas"]
print(nombres[-1])

'''