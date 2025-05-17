"""
Una tienda online quiere mejorar su sistema de recomendaciones analizando el comportamiento de sus clientes. Para ello, dispone del historial de compras de dos usuarios distintos, almacenado en listas de productos.
📌 Objetivo: Escribir un programa en Python que permita analizar estos historiales de compra y responder las siguientes preguntas:
 1️⃣ Productos en común: ¿Qué productos han comprado ambos usuarios?
 2️⃣ Productos exclusivos: ¿Qué productos ha comprado cada usuario que el otro no ha adquirido?
 3️⃣ Catálogo total: ¿Cuál sería el conjunto total de productos comprados entre los dos usuarios?
 4️⃣ Recomendaciones: ¿Cómo podrías utilizar esta información para sugerir productos a cada usuario?
🎯 Requisitos:
 ✔️ El programa debe recibir como entrada dos listas de productos (pueden ser ingresadas manualmente o predefinidas).
 ✔️ Debe procesar y mostrar los resultados de forma clara.
 ✔️ Se valorará el uso de funciones para estructurar el código de manera organizada.
🔹 Extras opcionales:
Permitir que los usuarios ingresen sus listas manualmente.
Ampliar el programa para comparar más de dos usuarios.
"""

lista_usuario1 = ["campera", "remera", "zapatillas", "bufanda"]

lista_usuario2 = ["pantalon", "gorra", "campera", "buzo", "bufanda"]


productos_en_comun = []

#queremos llenar productos_en_comun con los productos que se repiten en ambas listas,
for i in range(len(lista_usuario1)):
    productos_en_comun = lista_usuario1[i]
    print(f"producto: {productos_en_comun}")


    for j in range(len(lista_usuario2)):
        if lista_usuario1[i] == lista_usuario2[j]:
            productos_en_comun = lista_usuario1 + [lista_usuario2[j]]
            print(f"productoPrueba: {productos_en_comun}")

            