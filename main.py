
def es_mayor(repros_a, repros_b):
    """Calcula que reproduccion es mayor."""
    return repros_a > repros_b


def calcula_diferencia(repros_a, repros_b):
    """Calcula la diferencia de visitas que tienen las canciones."""
    return abs(repros_a - repros_b)

puntos=0
# Round 1

CANCION_1_NOMBRE = "Here comes the sun / The Beatles"
CANCION_1_REPROS = 1919705952

CANCION_2_NOMBRE = "Californication / Red Hot Chili Peppers"
CANCION_2_REPROS = 2118332024

print("Round 1 FIGHT")
print("Opción 1:", CANCION_1_NOMBRE)
print("Opción 2:", CANCION_2_NOMBRE, end="\n\n")

eleccion_1 = int(input("¿Cuál canción crees que tiene MÁS reproducciones? (Elige 1 o 2): "))

cancion_1_es_mayor = es_mayor(CANCION_1_REPROS, CANCION_2_REPROS)

if eleccion_1 != 1 and eleccion_1 != 2:
    print("opcion no valida, Debiste de  elegir entre 1 o 2")
elif (eleccion_1 == 1 and cancion_1_es_mayor) or (eleccion_1 == 2 and not cancion_1_es_mayor):
    print("¡Correcto! Has acertado esta ronda")
    puntos = puntos + 1
else:
    print("Incorrecto. No era la opción con más reproducciones.")



diferencia = calcula_diferencia(CANCION_1_REPROS, CANCION_2_REPROS)
print("diferencia de visitas:", diferencia)


# Round 2
CANCION_4_NOMBRE = "Bohemian Rhapsody/ Queen"
CANCION_4_REPROS = 3267193062

CANCION_3_NOMBRE = "Sweet child o mine / Guns and Roses"
CANCION_3_REPROS = 2875019844

print("Round 2 FIGHT")
print("Canción 4:", CANCION_4_NOMBRE)
print("Canción 3:", CANCION_3_NOMBRE, end="\n\n")

eleccion_2 = int(input("¿Cuál canción crees que tiene MÁS reproducciones? (Elige 3 o 4): "))

cancion_4_es_mayor = es_mayor(CANCION_4_REPROS, CANCION_3_REPROS)

if eleccion_2 != 3 and eleccion_2 !=4:
    print("opcion no valida, Debiste de  elegir entre 3 o 4")
elif (eleccion_2 == 4 and cancion_4_es_mayor) or (eleccion_2 == 3 and not cancion_4_es_mayor):   
    print("¡Correcto! Has acertado esta ronda")
    puntos = puntos + 1
else:
    print("Incorrecto. No era la opción con más reproducciones.")

diferencia = calcula_diferencia(CANCION_4_REPROS, CANCION_3_REPROS)
print("diferencia de visitas:", diferencia)

print("resultado final")
print("El puntaje obtenido es", puntos, "de 2 ")
if puntos == 2:
    print("¡Excelente! Puntuación perfecta.")
elif puntos == 1:
    print("Buen intento, acertaste la mitad.")
else:
    print("Suerte para la próxima, obtuviste 0 puntos.")

