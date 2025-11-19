#imprimirlo para el parcial
"""
try:
    division = 10/numero #0
except ValueError:
    print("ocurrio un error en la division")
except ZeroDivisionError:
    print("no se puede dividir por cero")
#el else se ejecuta si no hay errores
else:
    print("el resultado es: ", resultado)
finally:
    print("fin del programa")
# _______________________________________________________________________________________________   

#ahi se crean las excepciones que quierea generar 
class MiExcepcion(Exception):
    def __init__(self,mensaje):
        self.mensaje = mensaje
        super().__init__(self,mensaje)
#así se llama la excepsion         
raise MiExcepcion("Error de inevtario")

#____________________________________________________________________________________________________
#para no usar print se usa

import logging

logging.basiclonfig(
    
    level = logging.info
    format = "%(astine)s- %(name)s- %(levelname)s - %(messages)s"
)
logger = logging.getLogging(__name__)
logger.debug("mensaje")
logger.info("mensaje")
logger.warning("mensaje")
logger.error("mensaje")
logger.critical("mensaje")

#______________________________________________________________________________________________________
#1 forma de hacerlo para leer un archivo
try:
    archivo = open("datos.txt")
    contenido = archivo.read()
    print(contando)
except FileNotFoundError:
    print("Error: el archivo no existe")
finally:
    archivo.close()

#2 forma de hacerlo para leer un archivo
try:
    with open("datos.txt","r") as archivo:
    contenido.read()
    prin(contenido)
except FileNotFoundError:
    print("Error: el archivo no existe.")     

#___________________________________________________________________________________
clase de excepciones
   
log

debug 0 Error 4
warn 1    info 2
info 2    Exception 3
exception 3    warn 1
critical   debuy 0
"""
#REPASAR

#para que es un logger daemon?
#para que el logger se ejecute en segundo plano
#para que es un lock
#para evitar condiciones de carrera

#historial de tareas de el trello
#epicas trabajos grande y documentadas, cronometradas, estados claros
#dentro de las epicas van las tareas
#tareas pequeñas, concretas, con un objetivo claro
#cada tarea tiene un estado (por hacer, en progreso, hecho)
#se pueden asignar etiquetas y prioridades a las tareas
#se pueden asignar tareas a miembros del equipo

#repasar conceptos de hilos, locks, condiciones de carrera, eventos
#repasar manejo de hilos daemon
#repasar sincronizacion de hilos con eventos
#


