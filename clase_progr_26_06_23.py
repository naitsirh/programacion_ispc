# Realice un programa que contenga una función que se llame “conversion”, que
# la misma contenga tres parámetros. Se pide convertir los segundos ingresados 
# en horas, minutos y segundos


'''
======== ======== ======== ======== ======== ======== ======== ========
De un compañero


def conversion(seg):
	horas = seg / 3600 # 1h = 3600s
	minutos = (seg % 3600) / 60
	segundos = (seg % 3600) % 60
	print(f"{horas:.0f}h : {minutos:.0f}m : {segundos:.0f}s")

conversion(500)


======== ======== ======== ======== ======== ======== ======== ========
De un compañero


def conversion(segundos):
	horas = segundos / 3600
	minutos = segundos / 60
	print (f'{segundos}, corresponden a {horas} hora')
	print (f'{segundos}, corresponden a {minutos} minutos')

conversion(500)


======== ======== ======== ======== ======== ======== ======== ========
De una compañera


def conversion(segundos):
	horas = segundos // 3600
	minutos = (segundos % 3600) // 60
	segundos = (segundos % 3600) % 60

	return horas, minutos, segundos


segundos_totales = int(input("Ingrese la cantidad total de segundos: "))
horas, minutos, segundos = conversion(segundos_totales)
print("Horas:", horas, "Minutos:", minutos, "Segundos:", segundos)


======== ======== ======== ======== ======== ======== ======== ========
De una compañera


def conversion(segundos):
	horas = int(segundos / 3600)
	segRestantes = segundos - (horas*3600)
	minutos = int(segRestantes / 60)
	segRestantes = segRestantes - (minutos * 60)

	print(f"{horas} horas, {minutos} minutos, {segRestantes} segundos. ")


======== ======== ======== ======== ======== ======== ======== ========
De un compañero


def conversion(segundos):
	horas = segundos // 3600
	min = (segundos % 3600) // 60
	seg = (segundos % 3600) % 60
	return horas, min, seg

segundos = int(input("Ingrese la cantidad de segundos: "))
horas, minutos, segundos = conversion(segundos)
print("La conversión es: {} horas, {} minutos, {} segundos".format(horas, minutos, segundos))



======== ======== ======== ======== ======== ======== ======== ========
Primero hecho por mi


def conversion(segundos):
	horas = segundos//3600
	minutos = segundos//60

	print(horas, 'horas', minutos, 'minutos', segundos, 'segundos')

conversion(15000)


======== ======== ======== ======== ======== ======== ======== ========
Primero con 'f'



def conversion(segundos):
	horas = segundos//3600
	minutos = segundos//60

	print(f'{horas} horas, {minutos} minutos, {segundos} segundos')

conversion(15000)


======== ======== ======== ======== ======== ======== ======== ========
Segundo


def conversion(segundos):
	horas = segundos//3600
	minutos = segundos//60

	if horas > 0: print(horas, 'horas')
	if minutos > 0: print(minutos, 'minutos')
	if segundos > 0: print(segundos, 'segundos')

conversion(15000)


'''
'''
======== ======== ======== ======== ======== ======== ======== ========
Segundo con resta de mostrados


def conversion(segundos):
	horas = segundos // 3600
	minutos = (segundos % 3600) // 60
	seg_finales = (segundos % 3600) % 60

	if horas > 0: print(horas, 'horas')
	if minutos > 0: print(minutos, 'minutos')
	if seg_finales > 0: print(seg_finales, 'segundos')


while True:
	seg = int(input('Ingrese una cantidad de segundos: '))
	conversion(seg)

	decidir = input('Presiona una tecla para repetir, para salir presiona "s": ')
	if decidir == 's':
		break
	print()


======== ======== ======== ======== ======== ======== ======== ========
Tendiente a como lo pidió la profesora
'''


def conversion(horas, minutos, segundos):
	total = horas*3600 + minutos*60 + segundos

	horas = total // 3600
	minutos = (total % 3600) // 60
	seg_finales = (total % 3600) % 60

	print('\nEl total del tiempo ingrasado corresponde a:')
	if horas > 0: print(horas, 'horas')
	if minutos > 0: print(minutos, 'minutos')
	if seg_finales > 0: print(seg_finales, 'segundos')


while True:
	hor = int(input('Ingrese una cantidad de horas: '))
	mns = int(input('Ingrese una cantidad de minutos: '))
	seg = int(input('Ingrese una cantidad de segundos: '))
	conversion(hor, mns, seg)

	decidir = input('Presiona una tecla para repetir, para salir presiona "s": ')
	if decidir == 's':
		break
	print()
	print()


