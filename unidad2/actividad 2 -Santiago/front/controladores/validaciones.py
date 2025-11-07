import re

class Validaciones:
    
    def __init__(self):
        pass

    def validar_letras(valor):
        patron = re.compile("^[A-Za-z ]*$")
        resultado = patron.match(valor.get()) is not None
        if not resultado:
            return False
        return True
    
    def validar_numeros(valor):
        patron = re.compile(r'^[0-9cmlCML/ ]*$')
        resultado = patron.match(valor.get()) is not None
        if not resultado:
            return False
        return True
