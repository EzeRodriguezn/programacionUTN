# Programa para determinar la posición de un jugador de baloncesto según su altura

# Solicitar la altura del jugador en centímetros
altura = int(input("Ingrese la altura del jugador en centímetros: "))

# Determinar la posición del jugador según su altura
if altura < 160:
    posicion = "Base"
elif 160 <= altura <= 179:
    posicion = "Escolta"
elif 180 <= altura <= 199:
    posicion = "Alero"
else:
    posicion = "Ala-Pívot o Pívot"

# Mostrar la posición del jugador
print(f"La posición del jugador es: {posicion}")