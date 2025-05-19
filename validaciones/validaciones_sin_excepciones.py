                                                                                                                                                                                      
# Función 1: Validar float
#CUANDO VEAMOS STRINGS Y VECTORES REHACER ESTE EJERCICIO PARA QUE VALIDE SI EL USUARIO INGRESA UN STRING
#DE LA SIGUIENTE MANERA : "1.23.23.PEPE"

def es_float(valor):
    """
    Verifica si el valor es de tipo float o un string que representa un número decimal.
    """
    if type(valor) == float:
        return True
    #return False
    # HOLA MUNDO CRUEL [0]=HOLA [1]=MUNDO [2]=CRUEL
    #"1.23.pepe"
    if type(valor) == str and "." in valor: #"3.14" ¨[0] = 3 [1] = 14
        partes = valor.split(".") #separa el string en dos partes por el punto
        #VERIRFICAR SI EL VECTOR TIENE DOS POSICIONES, SI TIENE MAS SALIR CON FALSE
        return partes[0].isdigit() and partes[1].isdigit()
    return False

print("Pruebas es_float:")
print(es_float("3.14"))   # True
print(es_float(3.14))     # True
print(es_float("texto"))  # False
print(es_float("12"))     # False
print(es_float(12))       # False
print(es_float("pepe.4"))


# Función 2: Validar entero

def es_entero(valor):
    """
    Verifica si el valor es de tipo int o un string que representa un número entero.
    """
    if type(valor) == int: # SI LA VARIABLE ES UN ENTERO
        return True
    #ISDIGIT VERIFICA SI EL STRING SOLO TIENE DIGITOS (0,9)
    #"45", "3" , "168"
    if type(valor) == str and valor.isdigit():
        return True
    return False

# Función 3: Validar alfanumérico
def es_alfanumerico(valor):
    """
    Verifica si el valor es una cadena alfanumérica (solo letras y números).
    """
    if type(valor) == str and valor.isalnum():
        return True
    return False

# Pruebas


print("\nPruebas es_entero:")
print(es_entero("5"))     # True
print(es_entero(5))       # True
print(es_entero("5.0"))   # False
print(es_entero(5.0))     # False
print(es_entero("cinco")) # False
'''

print("\nPruebas es_alfanumerico:")
print(es_alfanumerico("Hola123"))     # True
print(es_alfanumerico("hola mundo"))  # False
print(es_alfanumerico("123"))         # True
print(es_alfanumerico("!!!"))         # False
print(es_alfanumerico(""))            # False
'''