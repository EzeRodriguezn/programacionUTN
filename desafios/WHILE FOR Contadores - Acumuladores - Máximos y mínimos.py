# 1 Mostrar 10 repeticiones de números ascendentes desde el 1 al 10. (for)
# 2 Mostrar 10 repeticiones de números descendentes desde el 10 al 1. (for)
# 3 Mostrar la suma de los números desde el 1 hasta el 10. (for , acumulador)
# 4 Mostrar la suma de los números pares desde el 1 hasta el 10. (for, acumulador, 2)
# 5 Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.(for, acumulador y contador(opcional), promedio)
# 6 Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.(while, acumulador y contador, promedio)
# 7 Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.(while, acumulador += acumulador *=)
# 8 Ingresar 10 números enteros. Determinar el máximo y el mínimo.(for, max , mix )



# 1
# for i in range(1, 11):  
#      print(i)  


#2
# for i in range (10,0,-1): 
#         print(i)

# 3
# suma = 0  #acumulador
# for i in range (1,11):
#     suma += i
#     print(suma)

#4
# suma_pares = 0
# for i in range(0, 11,2):
#     suma_pares += i
#     print (suma_pares)

5
# suma = 0  # Acumulador
# contador = 0  # Contador
# for i in range(1,6): #si pones 5 el contador solo toma 4 numeros porque va del 0 al 4
#     numero = int(input("Ingrese un número: "))  
#     suma += numero 
#     contador += 1 
# promedio = suma / contador
# print(i)
# print("La suma es:", suma)
# print("El promedio es:", promedio)

# suma = acumulador 
# promedio = contador 

# # 6
# numero_ingreasdo = 0
# acumulador = 0
# contador = 0
# continuar = "s" 
# while continuar.lower() == "s":
#     numero_ingreasdo = int(input("Ingrese un número: "))
#     acumulador += numero_ingreasdo 
#     contador += 1
#     continuar = input("¿Desea ingresar otro número? (s/n): ")

# promedio = acumulador / contador 

# print("La suma es:", acumulador)
# print("El promedio es:", promedio)

#7
# acumulador_positivo = 0
# acumulador_negativo = 1  #inicializo en 1 porque si lo pongo en 0 no acumulo
# continuar = "s"
# while continuar.lower() == "s":
#     numero_ingresado =int(input("Ingrese un número: "))
#     if numero_ingresado > 0:
#         acumulador_positivo += numero_ingresado
#     else:
#         acumulador_negativo *= numero_ingresado 
#     continuar = input("¿Desea ingresar otro número? (s/n): ")
# print("La suma de los números positivos es:", acumulador_positivo) 
# print("El producto de los números negativos es:", acumulador_negativo)


#8
# maximo = float('-inf')  # Inicializo en el menor número posible
# minimo = float('inf')  # Inicializo en el mayor número posible
# for i in range(1,11):
#     numero_ingresado = int(input("Ingrese un número: "))
#     if numero_ingresado  > maximo:
#         maximo = numero_ingresado
#     if numero_ingresado < minimo:
#         minimo = numero_ingresado
# print("El número máximo es:", maximo)       
# print("El número mínimo es:", minimo)




 