
def es_mayor(repros_a, repros_b):
    """Calcula que reproduccion es mayor."""
    return repros_a > repros_b


def calcula_diferencia(repros_a, repros_b):
    """Calcula la diferencia de visitas que tienen las canciones."""
    return abs(repros_a - repros_b)


# Round 1
CANCION_1_NOMBRE = "Here comes the sun / The Beatles"
CANCION_1_REPROS = 1919705952

CANCION_2_NOMBRE = "Californication / Red Hot Chili Peppers"
CANCION_2_REPROS = 2118332024

print("Round 1 FIGHT")
print("Canción 1:", CANCION_1_NOMBRE)
print("Reproducciones:", CANCION_1_REPROS, end="\n\n")

print("Canción 2:", CANCION_2_NOMBRE)
print("Reproducciones:", CANCION_2_REPROS, end="\n\n")


cancion_1_es_mayor = es_mayor(CANCION_1_REPROS, CANCION_2_REPROS)
cancion_2_es_mayor = es_mayor(CANCION_2_REPROS, CANCION_1_REPROS)

print("¿La Canción 1 tiene más reproducciones?:", cancion_1_es_mayor)
print("¿La Canción 2 tiene más reproducciones?:", cancion_2_es_mayor)

diferencia = calcula_diferencia(CANCION_1_REPROS, CANCION_2_REPROS)
print("diferencia de visitas:", diferencia)


# Round 2
CANCION_4_NOMBRE = "Bohemian Rhapsody/ Queen"
CANCION_4_REPROS = 3267193062

CANCION_3_NOMBRE = "Sweet child o mine / Guns and Roses"
CANCION_3_REPROS = 2875019844
print("Round 2 FIGHT")
print("Canción 4:", CANCION_4_NOMBRE)
print("Reproducciones:", CANCION_4_REPROS, end="\n\n")
print("Canción 3:", CANCION_3_NOMBRE)
print("Reproducciones:", CANCION_3_REPROS, end="\n\n")

cancion_4_es_mayor = es_mayor(CANCION_4_REPROS, CANCION_3_REPROS)
cancion_3_es_mayor = es_mayor(CANCION_3_REPROS, CANCION_4_REPROS)

print("¿La Canción 4 tiene más reproducciones?:", cancion_4_es_mayor)
print("¿La Canción 3 tiene más reproducciones?:", cancion_3_es_mayor)

diferencia = calcula_diferencia(CANCION_4_REPROS, CANCION_3_REPROS)
print("diferencia de visitas:", diferencia)

