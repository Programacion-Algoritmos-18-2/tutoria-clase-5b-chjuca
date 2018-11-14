from paquete_academico.modelado import *
est1=EstDistancia()						# Creamos el Objeto 
est1.setNombre("Jose")				# Llamamos a la funcion setNombre con el parametro "Jose"
est1.setApellido("Diaz")			# Llamamos a la funcion setApellido con el parametro "Diaz"
est1.setCodigo("11012")				# Llamamos a la funcion setCodigo con el parametro "11012"
est1.setNumMaterias(5)				# Llamamos a la funcion setNumMaterias con el parametro 5
est1.setModulo("Noveno")			# Llamamos a la funcion setModulo con el parametro "Noveno"			
p=Pais("Ecuador","Quito")			# Creamos el Objeto Pais y le enviamos el vaor de sus atributos
est1.setPais(p)						# Llamamos a la funcion setPais y le enviamos el objeto p
print(est1.presentarInformacion())	# Presentamos 