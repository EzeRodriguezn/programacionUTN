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
def numero_entero():
    numero = input("ingrese un numero entero: ")
    if numero.isdigit():
        print("el nunero es entero")
    else:
        print("error,no es un numero entero")
    return numero
numero_entero()

#------------------------------------------

2#
def numero_flotante():
    numero = input("ingrerse un numero flotante: ")
    if not numero.isdigit() and not numero.isalpha():
        print ("el numero es un flotante")
    else:
        print ("error, no es u numero flotante ")
    return numero 
numero_flotante()

#------------------------------------------

# 3#
def ingreso_cadena():
    cadena = input("ingrese una cadena: ")
    if cadena.isalpha():
        print("es una cadena ")
    else:
        print ("no es una cadena")
    return cadena
ingreso_cadena()

#------------------------------------------

4#
def area_rectangulo():
    base = input("ingrese la base del rectangulo: ")
    altura = input("ingrese la altura del triangulo: ")
    if not base.isdigit() and not altura.isdigit():
        print("la base y la altura no son un digito valido")
    else:
        base = int(base)
        altura = int(altura)
        area = base * altura
        print (f"el area del rectangulo es {area}")
    return area
area_rectangulo()

#------------------------------------------

# 5#
def area_circulo(numero):
    
    if isinstance(numero, int):#porque dice el parametro
        area = 3.14 * numero**2
        print (f"el area del circulo es: {area}")
    else:
        input("error, no es un digito")
    return area
area_circulo(8)

#------------------------------------------

6# Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
def numero_par_impar():
    numero_ingresado = input("ingrese un numero: ")
    if numero_ingresado.isdigit():
        numero_ingresado = float(numero_ingresado)
        if numero_ingresado % 2 ==0:
            return print (f"el numero ingresado {numero_ingresado} es par")   
        else:
            return print(f"el numero ingresado {numero_ingresado} es inpar")   
    else:
        print("error, ingrese un numero")
    return numero_ingresado
numero_par_impar()

    
#------------------------------------------

7# Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.
def numero_par_impar():
    numero_ingresado = input("ingrese un numero: ")
    if numero_ingresado.isdigit():
        numero_ingresado = float(numero_ingresado)
        if numero_ingresado % 2 ==0:
            return True
        else:
            return False
    else:
        print("error, ingrese un numero")
    return numero_ingresado
numero_par_impar()

#------------------------------------------

8# Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
#sin argumento

def numero_max():
    a = input("ingrese un numero: ")
    b = input("ingrese un segundo numero: ")
    c = input("ingrese un tercer numero: ")
    if a.isdigit() and b.isdigit() and c.isdigit():
        a = int(a)
        b = int (b) 
        c = int(c)
        if a > b and a > c:
            return a
        elif b > a and b > c:
            return b
        else:
            return c
    else:
        print("error, no es un digito valido")
print(numero_max())

#8
#con argumento
def numero_max(a,b,c):
     if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        if a > b and a > c:
            return a
        elif b > a and b > c:
            return b
        else:
            return c
     else:
        print("error, no es un digito valido")
resultado = numero_max(1,2,3)
print(resultado)

#-------------------------------------------

#9 Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.
def potencia_numero(base,exponente):
    if isinstance(base,(int)) and isinstance(exponente,(int)):
        return base ** exponente
    else:
       print("error, digitos invalidos")
resultado = potencia_numero(2,2)
print (resultado)


#10 Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.
def numero_primo():
    numero_ingresado = input("inserta un numero: ")
    if numero_ingresado.isdigit():
        numero_ingresado = int(numero_ingresado)
        if numero_ingresado < 2:
             return False
        for i in range(2, numero_ingresado):
            if numero_ingresado % i == 0:
                return False
        else:
            return True
    else:
        print("error, numero no valido")
print (numero_primo())
    


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

