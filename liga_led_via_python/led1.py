import serial

porta = '/dev/ttyACM0'
taxa = 9600

def escreve_porta():
	try:
		valor = (raw_input("1 - Para ligar o led\n2 - Para desligar\n"))
		obj_porta = serial.Serial(porta, taxa)
		obj_porta.write(valor)
		ler_porta()
		obj_porta.close()

	except serial.SerialException:
		print "Erro : Nao foi conectado"

def ler_porta():
	try:
		obj_porta1 = serial.Serial(porta, taxa)
		valor1 = obj_porta1.readline()
		print "Arduino disse: ", valor1
		obj_porta1.close()

	except serial.SerialException:
		print "Erro : Nao foi conectado"

##########################################

if __name__ == '__main__':
	escreve_porta()