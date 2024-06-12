import random
import string

class Generador():
    def transformar(pPalabra):
        vocales = {'a': '4',
               'e': '3', 
               'i': '1', 
               'o': '0', 
               'u': '5'}
        palabra_transformada=""
        for ref,valor in enumerate(pPalabra):
            if valor.isalpha():
                if valor.lower() in vocales:
                    palabra_transformada += vocales[valor.lower()]
                else:
                    if valor.islower():
                        palabra_transformada += valor.upper()
                    elif valor.isupper():
                        palabra_transformada += valor.lower()
            elif valor.isdigit():
                palabra_transformada += random.choice(string.ascii_lowercase)
            else:
                palabra_transformada += valor
        return palabra_transformada