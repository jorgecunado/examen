import os

class Pregunta:
	def __init__(self, texto="", respuesta="", nivel=0):
		self.texto = texto
		self.respuesta = respuesta
		self.nivel = nivel

	def get_texto(self):	
		return self.texto

	def get_respuesta(self):
		return respuesta

	def get_nivel(self):
		return nivel

class Enunciado:
	def __init__(self, nombre):	
		self.lista_preguntas = []
		self.nombre = nombre
	
	def set_pregunta(self, ppregunta):
		self.lista_preguntas.append(ppregunta)	

	def obtener_pregunta(self, numero):
		if len(self.lista_preguntas) > numero:	
			return self.lista_preguntas[numero - 1]
		elif len(self.lista_preguntas) == 0:
			print("No hay preguntas aun en este enunciado")
			a=input("Seguir...")
			return None
		else:	
			print("No existe ese numero de pregunta, solo hay desde {} a {}".
				format(1,len(self.lista_preguntas)))
			a=input("Seguir...")
			return None

	def permutar_pregunta(self, posicion1, posicion2):
		if self.obtener_pregunta(posicion1) is not None and self.obtener_pregunta(posicion2) is not None:
			soporte = self.lista_preguntas[posicion1]
			self.lista_preguntas[posicion1] = self.lista_preguntas[posicion2]
			self.lista_preguntas[posicion2] = soporte
			return True
		else:	
			print("Revise los numeros a permutar, o compruebe que hay preguntas en enunciado")
			a=input("Seguir...")
			return False
	
	def borrar_pregunta(self, tipo_borrado, numero = 0, ppregunta = "" ):
		if tipo_borrado == 1:
			if (self.obtener_pregunta(numero) is not None):
				self.lista_preguntas.pop(numero)
				return True
			else:
				print("No se pudo borrar la pregunta {}".format(numero))
				a = input("Seguir...")
				return False	
		elif tipo_borrado == 2:
			if contiene_pregunta(ppregunta):
				self.lista_preguntas.pop(ppregunta)
				return True
			else:	
				print("No se encontró la pregunta '{}'".format(ppregunta))
				return False			

	def contiene_pregunta(self, ppregunta):
		encontrado = False
		for pregunta in self.lista_preguntas:
			if pregunta.get_texto() == ppregunta:
				encontrado=True
				break
		if encontrado:
			return True
		else:
			return False	 		

	def numero_de_preguntas(self):
		return len(self.lista_preguntas)		

	def get_enunciado(self):	
		print("Enunciado de Examen")
		for indice,pregunta in enumerate(self.lista_preguntas):
			print("{},-{}".format(indice,pregunta.get_texto()))

pregunta1 = Pregunta()
pregunta1.texto="El triangulo escaleno tiene los tres lados iguales"	
pregunta1.respuesta = "Falso"	
pregunta2 = Pregunta()
pregunta2.texto="El teorema de pitagoras calcula la hipotenusa de un triangulo?"	
pregunta1.respuesta = "Verdadero"	
pregunta3 = Pregunta()
pregunta3.texto="El area de un triangulo es = lado * 2"	
pregunta3.respuesta = "Falso"	
pregunta4 = Pregunta()
pregunta4.texto="Un triangulo se forma cuando la suma de dos de su lados es > que el tercer lado"	
pregunta4.respuesta = "Verdadero"	

os.system("cls")
enunciado = Enunciado("Primer_enunciado")
enunciado.set_pregunta(pregunta1)
enunciado.set_pregunta(pregunta2)
enunciado.set_pregunta(pregunta3)
enunciado.set_pregunta(pregunta4)
enunciado.get_enunciado()
a = input("Seguir")
enunciado.permutar_pregunta(1,2)
enunciado.get_enunciado()
enunciado.borrar_pregunta(1,3)
enunciado.get_enunciado()
os.system("cls")
print(enunciado.obtener_pregunta(0))
a = input("Seguir")
print(" ")
print(enunciado.obtener_pregunta(1))
a = input("Seguir")