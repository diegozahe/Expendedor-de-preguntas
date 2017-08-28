import argparse #necesario para introducir valores por parametro 
import sys
import random
from tkinter import *
from tkinter import ttk

class Aplicacion():
	# Define la ventana principal de la aplicación
	def __init__(self):
		# Cargamos el archivo
		archivo = open("preguntasEjemplo.txt","r")
		self.listaPre = []
		listaOp = []
		self.listaRes = []

		self.cont = 0
		self.esAleatorio = False


		variasR = True
		for linea in archivo.readlines():
			if(linea == "\n"):
				continue

			if(linea[0].isdigit()):
				variasR = True
				self.listaPre.append(listaOp) #Este elemento lo eliminamos luego
				listaOp = []
				listaOp.append(linea[0:len(linea)-1])

			# Para añadir respuestas
			else:
				if "True!" in linea:
					listaOp.append(linea[0:len(linea)-6])
					if variasR:
						self.listaRes.append(linea[0])
						variasR = False
					else:
						num =len(self.listaRes)-1
						letra = linea[0]+self.listaRes[num]
						self.listaRes.append(letra)
				else:
					listaOp.append(linea[0:len(linea)-1])
				
		self.listaPre.pop(0)
		archivo.close()


		

		# Creamos la ventana!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		self.raiz = Tk()
		self.raiz.geometry('600x300') # anchura x altura
		self.raiz.resizable(width=False,height=False) # impedimos reajustar el tamaño de la ventana
		self.raiz.title('Aplicación') #asignamos un titulo a la ventana
		
		self.respuesta = StringVar()

		# Creamos el cuadro de texto tinfo
		self.tinfo = Text(self.raiz, width=65, height=12)
		self.tinfo.place(x=0,y=0) # lo situamos arriba

		# Escribimos la primera pregunta directamente!
		palabra = ""
		for linea in self.listaPre[self.cont]:
			palabra+=linea+"\n"

		self.tinfo.insert("1.0", palabra)
		
		# Creamos los botones
		self.bcorregir = ttk.Button(self.raiz, text='Corregir', command=self.corregir)
		self.bcorregir.place(x=0,y=200)

		self.bsalir = ttk.Button(self.raiz, text='Salir',command=self.raiz.destroy)
		self.bsalir.place(x=525,y=260)	
		
		# Creamos un boton para hacer las preguntas aleatorias
		self.bAleatorio = ttk.Button(self.raiz, text='Aleatorio',command=self.aleatorio)
		self.bAleatorio.place(x=525,y=10)

		# Creamos el cuadro de texto para introducir la respuesta
		self.trespuesta = ttk.Entry(self.raiz,textvariable=self.respuesta, width=5)
		self.trespuesta.place(x=80,y=202) # lo ponemos a la izquierda despues del boton

		# Creamos un cuadro de texto para mostrar el resultado
		self.tresultado = Text(self.raiz, width=50, height=5)
		self.tresultado.place(x=120,y=202) # lo ponemos a la izquierda despues del boton


		# Hace que este "marcado" el boton binfo
		self.bcorregir.focus_set() 

		# Hace que se pueda ver xD
		self.raiz.mainloop()


	def corregir(self):
		# Si le hemos dado al boton aleatorio el valor del numAl es aleatorio
		if self.esAleatorio:
			self.numAl = random.randrange(len(self.listaPre))
		else:
			self.numAl = self.cont # sino es el mismo que el contador


		# Eliminamos el contenido de la caja
		self.tinfo.delete("1.0", END)
		self.tresultado.delete("1.0",END)
		#Añadimos el resultado de la anterior pregunta
		if(self.trespuesta.get()==self.listaRes[self.numAl]):
			# Añadimos texto a la caja
			res = "Correcto!\n"

		else:
			res = "La respuesta correcta era la "
			res += self.listaRes[self.numAl]
			res += "\n"
		for x in self.listaPre[self.numAl]:
			if x[0].isdigit():
				res += x + "\n"
			if(x[0]==self.listaRes[self.numAl]):
				res += x + "\n"

		self.cont+=1
		self.numAl+=1
		pregunta =""
		for linea in self.listaPre[self.numAl]:
			pregunta+=linea+"\n"

		self.tinfo.insert("1.0", pregunta)

		self.tresultado.insert("1.0", res)

	def aleatorio(self):
		if self.esAleatorio:
			self.esAleatorio = False
		else:
			self.esAleatorio = True

def main():
	mi_app = Aplicacion()
	return 0

if __name__ == '__main__':
	main()
