import re

class Validaciones:
    def __init__(self):
        pass

    
    def validar_letras(valor):
       
        patron = re.compile(r'^[A-Za-zÁÉÍÓÚáéíóúÑñÜü ]*$')
        return patron.match(valor.get()) is not None

    
    def validar_numeros(valor):
        
        patron = re.compile(r'^[0-9cCmM/]*$')
        return patron.match(valor.get()) is not None
