def es_mayor(repros_a, repros_b):
    """Calcula que reproduccion es mayor."""
    return repros_a > repros_b


def calcula_diferencia(repros_a, repros_b):
    """Calcula la diferencia de visitas que tienen las canciones."""
    return abs(repros_a - repros_b)

puntos = 0

canciones_nombres = [
    "Here comes the sun / The Beatles",
    "Californication / Red Hot Chili Peppers",
    "Bohemian Rhapsody/ Queen",
    "Sweet child o mine / Guns and Roses"
]

canciones_repros = [
    1919705952,
    2118332024,
    3267193062,
    2875019844
]

print("Round 1 FIGHT")
print("Opción 1:", canciones_nombres[0])
print("Opción 2:", canciones_nombres[1], end="\n\n")

eleccion_1 = int(input("¿Cuál canción crees que tiene MÁS reproducciones? (Elige 1 o 2): "))

while eleccion_1 != 1 and eleccion_1 != 2:
    print("opcion no valida, Debiste de  elegir entre 1 o 2")
    eleccion_1 = int(input("¿Cuál canción crees que tiene MÁS reproducciones? (Elige 1 o 2): "))

cancion_1_es_mayor = es_mayor(canciones_repros[0], canciones_repros[1])

if (eleccion_1 == 1 and cancion_1_es_mayor) or (eleccion_1 == 2 and not cancion_1_es_mayor):
    print("¡Correcto! Has acertado esta ronda")
    puntos = puntos + 1
else:
    print("Incorrecto. No era la opción con más reproducciones.")

diferencia = calcula_diferencia(canciones_repros[0], canciones_repros[1])
print("diferencia de visitas:", diferencia)

print("Round 2 FIGHT")
print("Canción 1:", canciones_nombres[2])
print("Canción 2:", canciones_nombres[3], end="\n\n")

eleccion_2 = int(input("¿Cuál canción crees que tiene MÁS reproducciones? (Elige 1 o 2): "))

while eleccion_2 != 1 and eleccion_2 != 2:
    print("opcion no valida, Debiste de  elegir entre 1 o 2")
    eleccion_2 = int(input("¿Cuál canción crees que tiene MÁS reproducciones? (Elige 1 o 2): "))

cancion_4_es_mayor = es_mayor(canciones_repros[2], canciones_repros[3])

if (eleccion_2 == 1 and cancion_4_es_mayor) or (eleccion_2 == 2 and not cancion_4_es_mayor):   
    print("¡Correcto! Has acertado esta ronda")
    puntos = puntos + 1
else:
    print("Incorrecto. No era la opción con más reproducciones.")

diferencia = calcula_diferencia(canciones_repros[2], canciones_repros[3])
print("diferencia de visitas:", diferencia)

print("resultado final")
print("El puntaje obtenido es", puntos, "de 2 ")
if puntos == 2:
    print("¡Excelente! Puntuación perfecta.")
elif puntos == 1:
    print("Buen intento, acertaste la mitad.")
else:
    print("Suerte para la próxima.")