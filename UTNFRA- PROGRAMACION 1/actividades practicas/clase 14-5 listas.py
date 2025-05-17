# calificacion = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# suma = 0


# for i in range(len(calificacion)):
#     suma += calificacion[i]

#     promedio = suma / len(calificacion)
# print("El promedio es: ", promedio)


# a = [1, 2, 3]
# b = a
# b[0] = 100
# print(a)

datos = [None, None, None]
nombre = input("Ingrese su nombre: ")    
edad = int(input("Ingrese su edad: "))
dni = int(input("Ingrese su dni: "))
a = [nombre, edad, dni]
datos [0] = nombre
datos [1] = edad
datos [2] = dni
# datos [2] = dni
datos_copias = datos.copy()
print(datos)