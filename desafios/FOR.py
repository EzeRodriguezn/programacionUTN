
# 1 Mostrar los números ascendentes desde el 1 al 10
# 2 Mostrar los números descendentes desde el 10 al 1
# 3 Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.
# 4 Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:

# 	5 x 0 = 0
# 	5 x 1  = 5
# 	5 x 2 = 10
# 	5 x 3  = 15 …

# 5 Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.
# 6 Imprimir los números múltiplos de 3 entre el 1 y el 10.
# 7 Mostrar los números pares que hay desde la unidad hasta el número 50.
# 8 Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:


# 9 Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.
# 10 Ingresar un número. Determinar si el número es primo o no.
# 11 Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.


numero = int(input("Ingresa un número: "))
if numero <= 1:
    print(f"El número {numero} no es primo.")
else:
    # Usamos un bucle for para verificar si el número es divisible por algún otro número que no sea él mismo ni 1
    es_primo = True  # Suponemos que el número es primo
    for i in range(2, numero):  # Comenzamos desde 2 hasta el número-1
        if numero % i == 0:  # Si el número es divisible por i, entonces no es primo
            es_primo = False
            break  # No es necesario seguir verificando, ya sabemos que no es primo

    # Imprimimos el resultado
    if es_primo:
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")