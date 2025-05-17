# 1 Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
# 2 Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
# 3 Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 
# 4 Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 
# 5 Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
# 6 Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
# 7 Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.
# 8 Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
# 9 Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.
# 10 Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.
# 11 Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.
# 12 Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.
# 13 Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.

#1

# def numero_entero(): 
#    numero = int(input("Ingrese un número entero: "))
#    if numero.isdigit():
#        numero = f"el numero es: {numero}"
#    else:
#        numero = "error,no es un numero entero"
#    return numero

# resultado = numero_entero()
# print("Número entero ingresado:", resultado)

# 2#
# def numero_flotante(): 
#     numero = float(input("Ingrese un número flotante: "))
#     if not numero.isdigit() and not numero.isalpha():
#        numero = f"el numero es: {numero}"  
#     else:
#        numero = "error,no es un numero flotante"

#     return numero
# resultado = numero_flotante()
# print("Número flotante ingresado:", resultado)

# 3#
# def cadena():  #mejorar
#    cadena = input("Ingrese una cadena: ")
#    return cadena.isalnum()       
# resultado = cadena()
# print("Cadena ingresada:", resultado)   


# 4#
# def area_rectangulo(base:float, altura:float) -> float:
#     #validar_float con una funcion pasando la base 
#     #lo mismo con la altura
#     area = base * altura
#     return area
# resultado = area_rectangulo(5, 10)
# print("El área del rectángulo es:", resultado)

# 5#
# def area_circulo(radio:float):
#     #validar aca tamien
#     area = 3.14 * radio ** 2
#     return area
# resultado = area_circulo(5)
# print("El área del círculo es:", resultado)



6# Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
# def par_o_impar(numero):
#     if isinstance(numero, int): #isinstance verifica si el valor es un entero
#         if numero % 2 == 0:
#             return(f"{numero} es par")
#         else:
#             return(f"{numero} es impar")
#     else:
#         return "Error: El valor ingresado no es un número entero."

# resultado = par_o_impar(11)
# print(resultado)    

7# Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.
# def par_o_impar(numero:int):
#     if numero % 2 == 0:
#         return True
#     else:
#         return False
    
# resultado = par_o_impar(10)
# print(resultado)  

8# Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
# def maximo_de_tres(a, b, c):
#         return max(a, b, c)

# resultado = maximo_de_tres(50, 4, 12)
# print("El número más grande es:", resultado)

9# Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.
# def potencia_numero(base, exponente):
#     return base ** exponente
# resultado = potencia_numero(10, 4)
# print("La potencia es:", resultado)

10# Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.
# def numero_primo(numero):
    




# #11 usar modulo para esto
# def cuenta_regresiva(n):
#     if n == 0:
#         print("¡Despegue!")
#     else:
#         print(n)
#         cuenta_regresiva(n - 1)


        

# def pedir_y_calcular_factorial():
#     numero = input("Ingrese un número entero positivo: ")
#     if numero.isnumeric():
#         numero = int(numero)
#         if numero >= 0:
#             print("El factorial de", numero, "es:", factorial(numero))
#         else:
#             print("Debe ingresar un número mayor o igual a cero.")
#     else:
#         print("Error: debe ingresar solo números.")

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# pedir_y_calcular_factorial(n)

