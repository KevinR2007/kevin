import re

class Validaciones():
    
    def validar_letras(texto):
        RE_LETRAS = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü ]+$")
        return texto == "" or RE_LETRAS.match(texto)

    def validar_numeros(texto):
        RE_NUMEROS = re.compile(r"^/\d+$")
        return texto == "" or RE_NUMEROS.match(texto)
