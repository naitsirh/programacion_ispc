

'''
Ejercicio N° 1: Desarrollar un programa que cargue los datos de un triángulo.
Implementar una clase con los métodos para inicializar los atributos, imprimir 
el valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero,
isósceles o escaleno).
'''








'''
# DE LA PROFE

# Parte 1: creamos la clase
class Triangulo:
	# inicializamos
	def inicializar(self):
		self.lado1 = int(input("Ingrese el valor del primer lado: "))
		self.lado2 = int(input("Ingrese el valor del segundo lado: "))
		self.lado3 = int(input("Ingrese el valor del tercer lado: "))

	# Parte 2: imprimimos 
	def imprimir(self):
		print("Los lados del triángulo tienen el valor de")
		print("Lado 1:", self.lado1)
		print("Lado 2:", self.lado2)
		print("Lado 3:", self.lado3)

	# Parte 3: comprobamos el lado mayor
	def mayor(self):
		print("El lado mayor es")
		if self.lado1 > self.lado2 and self.lado1 > self.lado3:
			print("Lado 1:", self.lado1)
		elif self.lado2 > self.lado3:
			print("Lado 2:", self.lado2)
		else:
			print("Lado 3:", self.lado3)

	# Parte 4: comprobamos el tipo de triángulo
	# equilátero -> todos los lados iguales
	# isósceles -> dos lados iguales
	# escaleno -> todos los lados desiguales
	def tipo(self):
		if self.lado1 == self.lado2 and self.lado1 == self.lado3:
			print("Es un triángulo equilátero")
		elif self.lado1 != self.lado2 and self.lado1 != self.lado3:
			print("Es un triángulo escaleno")
		else:
			print("Es un triángulo isósceles")


figura = Triangulo()
figura.inicializar()
figura.imprimir()
figura.mayor()
figura.tipo()
'''








'''
# DE MARIA ITATI PAULINA

class Trianngulo:
	lado1 = 0
	lado2 = 0
	lado3 = 0

	def __init__(self, lado1, lado2, lado3):
		self.lado1 = lado1
		self.lado2 = lado2
		self.lado3 = lado3

	def __str__(self):
		return str(self.lado1) + '' + str(self.lado2) + '' + str(self.lado3)

	def perimetro(self):
		perimetro = self.lado1 * 2 + self.lado * 2 * 2 + self.lado * 3
		return perimetro

	def area(self): 
		area = self.lado1 * self.lado2 * self.lado3
		return area

lado1 = int(input("Ingrese el lado 1 del triangulo:"))
lado2 = int(input("Ingrese el lado 2 del triangulo:"))
lado3 = int(input("Ingrese el lado 3 del triangulo:"))
triang = Trianngulo(lado1, lado2,lado3)
'''








'''
# DE MATEO BELTRAMORE

class Triangulo:

	def __init__(self):
		self.lado1 = int(input("Ingrese el primer lado: "))
		self.lado2 = int(input("Ingrese el segundo lado: "))
		self.lado3 = int(input("Ingrese el tercer lado: "))

	def LadoLargo(self):
		if self.lado1 > self.lado2 and self.lado1 > self.lado3:
			return self.lado1
		elif self.lado2 > self.lado3:
			return self.lado2
		else:
			return self.lado3

	def Tipo(self):
		if self.lado1 == self.lado2 and self.lado2 == self.lado3:
			return ("Es un triangulo Equilatero")
		elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
			return ("Es un triangulo isósceles")
		else:
			return ("Es un triangulo escaleno")
'''








'''
# DE PAOLA NAVARRO

class Triangulo:
	def __init__(self, lado1, lado2, lado3):
		self.lado1 = lado1
		self.lado2 = lado2
		self.lado3 = lado3

	def determinar_tipo(self):
		if self.lado1 == self.lado2 == self.lado3:
			return 'equilátero'
		elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
			return 'isósceles'
		else:
			return 'escaleno'

	def lado_mayor(self):
		return max(self.lado1, self.lado2, self.lado3)

	def imprimir_informacion(self):
		print(f'Lado mayor: {self.lado_mayor()}')
		print(f'Tipo de triángulo: {self.determinar_tipo()}')


# Solicitar al usuario que ingrese los lados del triángulo
lado1 = float(input('Ingrese el valor del primer lado: '))
lado2 = float(input('Ingrese el valor del segundo lado: '))
lado3 = float(input('Ingrese el valor del tercer lado: '))

# Crear un objeto Triangulo
triangulo = Triangulo(lado1, lado2, lado3)

# Imprimir información sobre el triángulo
triangulo.imprimir_informacion()

#print(triangulo.lado_mayor())
'''








'''
||    ||    ||    ||    ||    ||    ||    ||    ||    ||    ||    
||    ||    ||    ||    ||    ||    ||    ||    ||    ||    ||    
||    ||    ||    ||    ||    ||    ||    ||    ||    ||    ||    
# Creamos la clase
class Triangulo:
	# pedimos/cargamos los datos
	# (inicializamos los atributos)
	def init(self):
		self.lado1 = int(input('Cargue el pirmer lado: '))
		self.lado2 = int(input('Cargue el segundo lado: '))
		self.lado3 = int(input('Cargue el tercer lado: '))


	# definimos los valores mayor, menor y del medio
	def mayor(self):
		return max(self.lado1, self.lado2, self.lado3)

	def minim(self):
		return min(self.lado1, self.lado2, self.lado3)

	def medio(self):
		return self.lado1 + self.lado2 + self.lado3 - self.mayor() - self.minim()


	# imprimimos el valor del lado con un tamaño mayor
	def ladoMayor(self):
		# calculamos si hay dos o más lados iguales
		if self.lado1 == self.lado2 and self.lado1 == self.lado3:
			print('Los tres lados son iguales y miden', self.lado1)
		elif (self.lado1 == self.lado2 and self.lado1 > self.lado3) or \
			(self.lado2 == self.lado3 and self.lado2 > self.lado1) or \
			(self.lado3 == self.lado1 and self.lado3 > self.lado2):
				print('Hay dos lados mayores y miden', self.mayor())

		elif self.lado1 > self.lado2 and self.lado1 > self.lado3:
			print('El lado mayor es el 1 y mide:', self.lado1)
		elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
			print('El lado mayor es el 2 y mide:', self.lado2)
		else: print('El lado mayor es el 3 y mide:', self.lado3)


	# imprimimos el tipo de triángulo que es
	def tipoTriangulo(self):
		# comprobamos que sea un triángulo
		if self.mayor() >= (self.minim() + self.medio()):
			print('¡No existe el triángulo!')

		elif self.lado1 == self.lado2 == self.lado3:
			print('¡El triángulo es equilátero!')
		elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
			print('¡El triángulo es isósceles!')
		else:
			print('¡El triángulo es escaleno!')


t = Triangulo()
t.init()
t.ladoMayor()
t.tipoTriangulo()
#print(t.medio())
'''








'''
# Primer modelo propuesto por chatGPT

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def determinar_tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "isósceles"
        else:
            return "escaleno"

    def imprimir_lado_mayor(self):
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado con mayor tamaño es {mayor}")

# Solicitar al usuario ingresar los lados del triángulo
lado1 = int(input("Ingrese la longitud del primer lado: "))
lado2 = int(input("Ingrese la longitud del segundo lado: "))
lado3 = int(input("Ingrese la longitud del tercer lado: "))

triangulo = Triangulo(lado1, lado2, lado3)

# Imprimir el tipo de triángulo y el lado mayor
tipo = triangulo.determinar_tipo()
triangulo.imprimir_lado_mayor()
print(f"El triángulo es {tipo}")
'''








'''
# Segundo modelo propuesto por chatGPT

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def mayor_lado(self):
        return max(self.lado1, self.lado2, self.lado3)

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

# Pedimos al usuario que ingrese los lados del triángulo
lado1 = int(input("Ingrese la longitud del primer lado: "))
lado2 = int(input("Ingrese la longitud del segundo lado: "))
lado3 = int(input("Ingrese la longitud del tercer lado: "))

# Creamos una instancia de la clase Triangulo
triangulo = Triangulo(lado1, lado2, lado3)

# Imprimimos el lado más largo
print(f"El lado con mayor longitud es: {triangulo.mayor_lado()}")

# Determinamos el tipo de triángulo
#tipo = triangulo.tipo_triangulo()
#print(f"El triángulo es de tipo: {tipo}")

print(f"El triángulo es de tipo:", triangulo.tipo_triangulo())
'''








'''
# Tercer modelo de chatGPT sin el `__init__`

class Triangulo:
    def determinar_tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "isósceles"
        else:
            return "escaleno"

    def imprimir_lado_mayor(self):
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado con mayor tamaño es {mayor}")

# Solicitar al usuario ingresar los lados del triángulo
lado1 = int(input("Ingrese la longitud del primer lado: "))
lado2 = int(input("Ingrese la longitud del segundo lado: "))
lado3 = int(input("Ingrese la longitud del tercer lado: "))

triangulo = Triangulo()
triangulo.lado1 = lado1
triangulo.lado2 = lado2
triangulo.lado3 = lado3

# Imprimir el tipo de triángulo y el lado mayor
tipo = triangulo.determinar_tipo()
triangulo.imprimir_lado_mayor()
print(f"El triángulo es {tipo}")
'''








'''
lado1 = int(input("Ingrese la longitud del primer lado: "))
lado2 = int(input("Ingrese la longitud del segundo lado: "))
lado3 = int(input("Ingrese la longitud del tercer lado: "))
mayor = max(lado1, lado2, lado3)
minim = min(lado1, lado2, lado3)
medio = lado1 + lado2 + lado3 - mayor - minim

if lado1 == lado2 and lado1 == lado3:
	print('Los tres lados son iguales y miden', lado1)
elif (lado1 == lado2 and lado1 > lado3) or (lado2 == lado3 and lado2 > lado1) or (lado3 == lado1 and lado3 > lado2):
	print('Hay dos lados mayores y miden', mayor)

if mayor >= (minim + medio):
	print('¡No existe el triángulo!')
'''
























































































'''
Ejercicio N° 2: Realizar un programa en el cual se declaren dos valores enteros
por teclado utilizando el método __init__. Calcular después la suma, resta,
multiplicación y división. Utilizar un método para cada una e imprimir los
resultados obtenidos. Llamar a la clase Calculadora.
'''








'''
||    ||    ||    ||    ||    ||    ||    ||    ||    ||    ||    
||    ||    ||    ||    ||    ||    ||    ||    ||    ||    ||    
||    ||    ||    ||    ||    ||    ||    ||    ||    ||    ||    
# Primer modelo, como antes, sin usar `__init__`
'''
class Calculadora:
	def __init__(self, num1, num2):
		self.n1 = num1
		self.n2 = num2

	def suma(self):
		print(self.n1 + self.n2)

	def resta(self):
		print(self.n1 - self.n2)

	def multiplicacion(self):
		print(self.n1 * self.n2)

	def division(self):
		if self.n2 != 0:
			div = round((self.n1 / self.n2), 2)
			print(div)
		else:
			print('Error: No se puede dividir por cero.')


'''
num1 = float(input('Ingrese el primer número: '))
num2 = float(input('Ingrese el segundo número: '))
c = Calculadora(num1, num2)
#c.suma()
#c.resta()
#c.multiplicacion()
c.division()
'''

while True:
	num1 = float(input('Ingrese el primer número: '))
	num2 = float(input('Ingrese el segundo número: '))

	print('\nIngrese la operación a realizar de la siguiente manera:')
	print('Suma => "S"  |  Resta => "R"  |  Multiplicación => "M"  |  División => "D" ')
	elec = input('Operación: ')
	c = Calculadora(num1, num2)

	if elec == 's' or elec == 'S': c.suma()
	elif elec == 'r' or elec == 'R': c.resta()
	elif elec == 'm' or elec == 'M': c.multiplicacion()
	elif elec == 'd' or elec == 'D': c.division()
	else: print('Elección no válida.')

	decidir = input('\nPara realizar otra operación presione una tecla, para salir presione "X": ')
	print()
	if decidir == 'x' or decidir == 'X':
		print('Gracias por utilizar la herramienta.')
		break