
# def saludar(nombre):
#     print("Hola", nombre)

# saludar("Juan")

# def sumar(a, b):
#     print ("resultado:", a + b)

# sumar (5, 3)

# def mostrar(nombre, edad ):
#     print(nombre, "tiene ", edad, "años")

# mostrar("Juan", 25)


# def saludar(nombre = "invitado"):
#     print("Hola", nombre)

# saludar()
# saludar("Pedro")


# def sumar(a: int, b: int) -> int: #hace q reorne un entero 
#     return a + b 
# sumar(5, 3)

# resultado = sumar(2.5,3.0)  #pasa valores flotantes
# print(resultado)# imprime resultado flotante

# def dividir (a: int, b: int) -> float:
#     return int(a / b)
# dividir(36, 3)
# resultado = dividir(36, 5)
# print(resultado) #imprime resultado redondeado a entero


# #mutable
# lista1 = [1, 2, 3]
# lista2 = lista1
# lista2[0] = 99
# print("lista", lista1) 
# print("lista2", lista2)

#inmutable





# #pasaje por valor
# def modificar_numero(numero):
#     numero += 1
#     return numero

def por_valor(numero):
    numero = 20
    return numero

numero = 10

resultado = por_valor(numero)
print("Número modificado:", resultado)  # Imprime 20
print("Número original:", numero)  # Imprime 10


def funcion() :
    x = 5 # se guarda en el stack
    y = [1,2,3] # la referencia a la lista va al stack, la lsita vive en el heap
