class Persona(object):							#Creamos la clase Persona 

	def __init__(self):							#Creamos el Metodo __init__
		self.nombre = " "						#Atributos de la clase Persona 
		self.apellido= " "
		self.pais= Pais("","")

	def setNombre(self,nombre):					#Funciones set que da valor a los atributos
		self.nombre=nombre

	def setApellido(self,apellido):
		self.apellido=apellido	

	def setPais(self,p):
		self.pais=p

	def getPais(self):							#Estas funciones devuelven los atributos
		return	self.pais.presentarPais()

	def getNombre(self):
		return self.nombre

	def getApellido(self):
		return self.apellido

	def presentarInformacion(self):				# Presentamos los Datos
		cadena = "INFORMACION\nNombre Completo: %s %s\nPocedencia: %s"%(self.getNombre(),self.getApellido(),self.getPais())
		return cadena



class Estudiante(Persona):						#Creamos la clase Estudiante que es una Persona 
	def __init__(self):							#Creamos el Metodo __init__
		super(Estudiante, self).__init__()		#Heredamos los atributos de la clase Persona 
		self.codigo=""							#Atributo de la clase Estudiante

	def setCodigo(self,codigo):					#Funciones set que da valor a los atributos
		self.codigo=codigo

	def getCodigo(self):						#Estas funciones devuelven los atributos					
		return self.codigo

	def presentarInformacion(self):				# Presentamos los Datos
		cadena = "INFORMACION\nNombre Completo: %s %s\nCodigo: %s\nPocedencia: %s"%(self.getNombre(),self.getApellido(),self.getCodigo(),self.getPais())
		return cadena
		

class EstPresencial(Estudiante):				#Creamos la clase Estudiante que es un Estudiante
	def __init__(self):							#Creamos el Metodo __init__
		super(EstPresencial, self).__init__()	#Heredamos los atributos de la clase Estudiante 
		self.numCreditos = 0					#Atributo de la clase EstPresencial
		self.ciclo=""

	def setNumCreditos(self,num):				#Funciones set que da valor a los atributos
		self.numCreditos=num

	def setCiclo(self,ciclo):
		self.ciclo=ciclo

	def getNumCreditos(self):					#Estas funciones devuelven los atributos
		return self.numCreditos

	def getCiclo(self):
		return self.ciclo

	def presentarInformacion(self):				# Pesentamos los Datos
		cadena = "INFORMACION\n\tNombre Completo: %s %s\n\tCodigo: %s\n\tPocedencia: %s\tCiclo: %s\tNumero Creditos: %d"%(self.getNombre(),self.getApellido(),self.getCodigo(),self.getPais(),self.getCiclo().upper(),self.getNumCreditos())
		return cadena
		

class EstDistancia(Estudiante):					#Creamos la clase Estudiante que es un Estudiante
	def __init__(self):							#Creamos el Metodo __init__
		super(EstDistancia, self).__init__()	#Heredamos los atributos de la clase Estudiante 
		self.numMaterias=0						#Atributo de la clase EstPDistancia
		self.modulo=""

	def setNumMaterias(self,num):				#Funciones set que da valor a los atributos
		self.numMaterias=num

	def setModulo(self,modulo):
		self.modulo=modulo

	def getNumMaterias(self):					#Estas funciones devuelven los atributos
		return self.numMaterias

	def getModulo(self):
		return self.modulo

	def presentarInformacion(self):				# Presentamos los Datos
		cadena = "INFORMACION\n\tNombre Completo: %s %s\n\tCodigo: %s\n\tPocedencia: %s\tModulo: %s\n\tNumero Materias: %d"%(self.getNombre(),self.getApellido(),self.getCodigo(),self.getPais(),self.getModulo().upper(),self.getNumMaterias())
		return cadena

class Pais():									#Creamos la clase Pais
	def __init__(self,nombre,capital):							#Creamos el Metodo __init__
		self.nombre = nombre					#Atributo de la clase Pais
		self.capital = capital

	def setNombre(self,nombre):					#Funciones set que da valor a los atributos
		self.nombre=nombre

	def setCapital(self,capital):
		self.capital=capital

	def getNombre(self):						#Estas funciones devuelven los atributos
		return	self.nombre

	def getCapital(self):
		return	self.capital

	def presentarPais(self):					# Presentamos los Datos
		cadena = "Pais - %s - Capital - %s\n"%(self.getNombre(),self.getCapital())
		return cadena
		