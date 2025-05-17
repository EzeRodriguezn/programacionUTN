import random

# Generar una nota aleatoria entre 1 y 10
nota = random.randint(1, 10)

# Determinar el mensaje según el valor de la nota
if nota >= 6:
    mensaje = f"Promoción directa, la nota es {nota}."
elif nota >= 4:
    mensaje = f"Aprobado, la nota es {nota}."
else:
    mensaje = f"Desaprobado, la nota es {nota}."

# Mostrar el mensaje
print(mensaje)