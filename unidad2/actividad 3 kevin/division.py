


try:
    division = 10/numero
except:
    print("Ocurrio un error en la división.")
    
    
except ZeroDivisionError:
    print("No se puede dividir por cero.")

else:
    print("El resultado es:", resultado)
    
finally:
    print("Fin del programa")
    
    
    
class Miexepcion(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
        

raise Miexepcion("Error de invertario"):
    
    
    
#Para no utilizar print

import logging(

logging.baseConfig
level=logging.INFO
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

)

logger = logging.getLogger(__name__)
logger.debug(" mensaje")
logger.info(" mensaje")
logger.warning(" mensaje")

logger.critical(" mensaje")











try:
    archivo = open("archivo.txt", "r")
    contando = archivo.read()
    print(contando)
    
except FileNotFoundError:
    print("El archivo no existe.")
    
finally:
    archivo.close()
    
    
    
    
    
    
    
    
    #otro
    
    try:
        with open ("datos.txt", "r") as archivo:
            contenido read()
            print(contenido)
    except FileNotFoundError:
        print("El archivo no existe.")