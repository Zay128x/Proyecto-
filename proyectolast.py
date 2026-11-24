def es_mayor(repros_a, repros_b):
    """Indica si el primer numero de reproducciones es mayor que el segundo."""
    return repros_a > repros_b


def calcula_diferencia(repros_a, repros_b):
    """Calcula la diferencia absoluta de reproducciones entre dos canciones."""
    return abs(repros_a - repros_b)


def separar_cancion_banda(etiqueta):
    """Separa una cadena 'Cancion / Banda' en titulo y banda sin espacios extra."""
    partes = str(etiqueta).split("/")
    cancion = partes[0].strip()
    banda = partes[1].strip() if len(partes) > 1 else "Desconocida"
    return cancion, banda


def leer_opcion_valida():
    """Pide 1 o 2 como texto limpio y devuelve el entero validado sin error."""
    entrada = input("Cual crees que tiene MAS reproducciones? (Elige 1 o 2): ").strip()
    while entrada != "1" and entrada != "2":
        print("Entrada no valida. Escribe 1 o 2.")
        entrada = input("Cual crees que tiene MAS reproducciones? (Elige 1 o 2): ").strip()
    return int(entrada)


def sumar_reproducciones(matriz_canciones):
    """Recorre la matriz 2D y acumula el total de reproducciones."""
    total = 0
    for fila in matriz_canciones:
        if len(fila) >= 2:
            total = total + fila[1]
    return total


def asegurar_y_leer_archivo(nombre_archivo):
    """Crea el archivo si no existe y devuelve su contenido previo."""
    with open(nombre_archivo, "a"):
        pass

    with open(nombre_archivo, "r") as archivo:
        return archivo.read().strip()


def guardar_puntaje(nombre_archivo, linea):
    """Guarda una linea con el resultado de la partida al final del archivo."""
    with open(nombre_archivo, "a") as archivo:
        archivo.write(linea + "\n")


def jugar_ronda(numero_ronda, cancion_a, cancion_b):
    """Muestra dos canciones intercalando orden, valida eleccion y regresa 1 o 0."""
    if numero_ronda % 2 == 0:
        primera = cancion_b
        segunda = cancion_a
    else:
        primera = cancion_a
        segunda = cancion_b

    titulo_1, banda_1 = separar_cancion_banda(primera[0])
    titulo_2, banda_2 = separar_cancion_banda(segunda[0])

    print()
    print("--- Ronda", numero_ronda, "de 33 ---")
    print("Opcion 1:", titulo_1.upper(), "-", banda_1)
    print("Opcion 2:", titulo_2.upper(), "-", banda_2)

    eleccion = leer_opcion_valida()
    primera_gana = es_mayor(primera[1], segunda[1])
    acierto = (eleccion == 1 and primera_gana) or (eleccion == 2 and not primera_gana)

    if acierto:
        print("Correcto! Acertaste.")
        punto = 1
    else:
        print("Incorrecto.")
        punto = 0

    diferencia = calcula_diferencia(primera[1], segunda[1])
    print("Diferencia de reproducciones:", diferencia)
    return punto


def main():
    """Ejecuta las rondas del juego, consulta archivo y guarda el resultado."""
    nombre_archivo = "historial_rondas.txt"
    historial = asegurar_y_leer_archivo(nombre_archivo)
    if historial != "":
        print("Historial previo:")
        print(historial)
        print("-" * 35)

    canciones = [
        ["Have You Ever Seen The Rain / Creedence Clearwater Revival", 2648186229],
        ["Fortunate Son / Creedence Clearwater Revival", 2033180197],
        ["Paranoid / Black Sabbath", 1782929153],
        ["Iron Man / Black Sabbath", 777792867],
        ["Should I Stay or Should I Go / The Clash", 1385400000],
        ["Rock the Casbah / The Clash", 685200000],
        ["Uptown Girl / Billy Joel", 1531578010],
        ["Piano Man / Billy Joel", 1490134433],
        ["You Make My Dreams (Come True) / Daryl Hall & John Oates", 1488611631],
        ["Maneater / Daryl Hall & John Oates", 1261620566],
        ["Here Comes The Sun / The Beatles", 1915000000],
        ["Let It Be / The Beatles", 1120000000],
        ["Dream On / Aerosmith", 1734597688],
        ["I Don't Want To Miss A Thing / Aerosmith", 1477771640],
        ["Wind Of Change / Scorpions", 1212534639],
        ["Rock You Like a Hurricane / Scorpions", 564434032],
        ["Chop Suey! / System Of A Down", 2150000000],
        ["Toxicity / System Of A Down", 1480000000],
        ["Island In The Sun / Weezer", 1180000000],
        ["Buddy Holly / Weezer", 790000000],
        ["Creep / Radiohead", 3269178199],
        ["No Surprises / Radiohead", 1508658477],
        ["Wonderwall / Oasis", 3209513663],
        ["Don't Look Back in Anger / Oasis", 1519993420],
        ["Basket Case / Green Day", 1685314257],
        ["American Idiot / Green Day", 1516688536],
        ["Evil / Interpol", 211180773],
        ["Obstacle 1 / Interpol", 137749455],
        ["Interstate Love Song / Stone Temple Pilots", 628746887],
        ["Plush / Stone Temple Pilots", 481351251],
        ["Freak On a Leash / Korn", 881611712],
        ["Coming Undone / Korn", 607552864],
        ["Crazy Train / Ozzy Osbourne", 1063136176],
        ["No More Tears / Ozzy Osbourne", 462425130],
        ["Bohemian Rhapsody / Queen", 3342073470],
        ["Don't Stop Me Now / Queen", 2831383606],
        ["With Or Without You / U2", 1485000000],
        ["I Still Haven't Found What I'm Looking For / U2", 1180000000],
        ["Light My Fire / The Doors", 580000000],
        ["Riders on the Storm / The Doors", 575000000],
        ["Cold Heart (PNAU Remix) / Elton John", 2862847739],
        ["Rocket Man (I Think It's Going To Be A Long, Long Time) / Elton John", 1650000000],
        ["In the Air Tonight / Phil Collins", 1136721096],
        ["You'll Be in My Heart / Phil Collins", 587214047],
        ["Boys Don't Cry / The Cure", 1050000000],
        ["Friday I'm in Love / The Cure", 1015000000],
        ["There Is a Light That Never Goes Out / The Smiths", 1020000000],
        ["This Charming Man / The Smiths", 740000000],
        ["Don't Stop Believin' / Journey", 3072317969],
        ["Any Way You Want It / Journey", 606616867],
        ["Paint It, Black / The Rolling Stones", 1740000000],
        ["Start Me Up / The Rolling Stones", 1150000000],
        ["Every Breath You Take / The Police", 2850000000],
        ["Roxanne / The Police", 1090000000],
        ["Take Me Out / Franz Ferdinand", 1478801493],
        ["No You Girls / Franz Ferdinand", 131310219],
        ["Ruby / Kaiser Chiefs", 366311422],
        ["I Predict A Riot / Kaiser Chiefs", 199823728],
        ["I Wanna Be Yours / Arctic Monkeys", 4128829477],
        ["Do I Wanna Know? / Arctic Monkeys", 3232856770],
        ["Californication / Red Hot Chili Peppers", 2118332024],
        ["Can't Stop / Red Hot Chili Peppers", 2390000000],
        ["Everlong / Foo Fighters", 2480000000],
        ["The Pretender / Foo Fighters", 1420000000],
        ["Sweet Child o' Mine / Guns N' Roses", 2875019844],
        ["November Rain / Guns N' Roses", 2380000000]
    ]

    total_rondas = len(canciones) // 2
    total_repros = sumar_reproducciones(canciones)
    print("Total de reproducciones en las", len(canciones), "canciones:", total_repros)

    puntos = 0
    for ronda in range(1, total_rondas + 1):
        indice_a = (ronda - 1) * 2
        indice_b = indice_a + 1
        puntos = puntos + jugar_ronda(ronda, canciones[indice_a], canciones[indice_b])

    print()
    print("--- Resultado final ---")
    print("Puntaje:", puntos, "de", total_rondas)
    guardar_puntaje(nombre_archivo, "Puntaje obtenido: " + str(puntos) + "/" + str(total_rondas))


main()