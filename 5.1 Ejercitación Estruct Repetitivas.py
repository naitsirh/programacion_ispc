# Importo la función "sleep" para demorar un poquito la ejecución del código
# entre la carga de los datos por el usuario y la salida en pantalla (sólo para
# diversión)

from time import sleep

'''
  ==================================================================
    EJERCICIOS ESTRUCTURAS REPETITIVAS Y ESTRUCTURAS CONDICIONALES
  ==================================================================


EJERCICIO 1. Realice un programa que lea 4 números y diga cuántos son pares y
cuantos impares y devuelva la sumatoria de los pares.

i = 0
num = None
pares = 0
impares = 0
suma_pares = 0

while i < 4:
	num = int(input('Ingrese un número: '))
	if num % 2 == 0:
		pares+=1
		suma_pares+=num
	else:
		impares+=1

	i+=1
	sleep(0.1)

if pares >= 1:
	print('\nLa cantidad total de los pares es: ', pares)
	print('La suma de todos los números pares es: ', suma_pares)
else:
	print('\nNo hay números pares.')

if impares >= 1:
	print('La cantidad total de los impares es: ', impares)
else:
	print('No hay números impares.')


  ================================================================


EJERCICIO 2. Leer 10 números y obtener la cantidad de mayores y la cantidad de
menores a 100, cuál es el número máximo y cuál es el número mínimo.

i = 0
mayor_100 = 0
menor_100 = 0
num_max = 0
num_min = 1000

while i < 10:
	num = int(input('Ingrese un número: '))
	if num > 100:
		mayor_100+=1
	else:
		menor_100+=1

	if num > num_max: num_max = num
	if num < num_min: num_min = num

	i+=1
	sleep(0.1)

print('\nLa cantidad de números mayores que 100 es: ', mayor_100)
print('La cantidad de números menores que 100 es: ', menor_100)
print('\nEl número máximo es: ', num_max)
print('El número mínimo es: ', num_min)


  ================================================================


EJERCICIO 3. Ingresar las edades y el sexo de 15 personas y determinar cuántas
son mujeres, cuántos varones, cuántos mayores de edad y cuántos
menores de edad.

i = 0
mujeres = 0
varones = 0
mayores_edad = 0
menores_edad = 0

for i in range(15):
	sexo = input('Ingrese sexo (F/M): ')
	if sexo == 'f' or sexo == 'F': mujeres+=1
	if sexo == 'm' or sexo == 'M': varones+=1

	edad = int(input('Ingrese la edad: '))
	if edad >= 18: mayores_edad+=1
	else: menores_edad+=1

	sleep(0.1)


print('\nLa cantidad de mujeres es: ', mujeres)
print('La cantidad de varones es: ', varones)

print('\nLa cantidad de mayores de edad es: ', mayores_edad)
print('La cantidad de menores de edad es: ', menores_edad)


  ================================================================


EJERCICIO 4. Leer 10 números y mostrar solamente los números positivos, y su 
sumatoria.

i = 0
sumatoria = 0
lista_positivos = []

num = int(input('Ingrese un número: '))
if num >= 0:
	sumatoria+=num
	lista_positivos.append(num)

for i in range(9):
	num = int(input('Ingrese otro número: '))

	if num >= 0:
		sumatoria+=num
		lista_positivos.append(num)


print('\nLa lista de los números ingresados positivos es: ', lista_positivos)
print('La sumatoria de los números ingresados positivos es: ', sumatoria)


  ================================================================


EJERCICIO 5. Leer 15 números negativos y convertirlos a positivos e imprimir 
dichos números.
'''

i = 0
lista_num = []

num = int(input('Ingrese un número: '))
if num < 0:
	positivo = abs(num)
	lista_num.append(positivo)
	i+=1

while i < 15:
	num = int(input('Ingrese otro número: '))
	
	if num < 0:
		positivo = abs(num)
		lista_num.append(positivo)
		i+=1

print('\nLa lista de los números ingresados negativos convertidos a positivos es: ', lista_num)
