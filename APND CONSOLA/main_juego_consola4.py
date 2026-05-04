import json
from funciones import *
from acertijos import *

# Defino CONSTANTES
CANTIDAD_SALAS = 4
CANTIDAD_INTENTOS = 2

def main():
    # Captura de datos
    print('Ingrese la cantidad de jugadores deseada: ')
    jugadores_cantidad = get_int_rango(1,10)
    jugadores_nombres = get_str_array(jugadores_cantidad)
    jugadores_puntos_salas_matriz = get_matriz(jugadores_cantidad,CANTIDAD_SALAS)

    # Empieza el juego
    correr_salas(jugadores_nombres,jugadores_puntos_salas_matriz)
    torneo_print_resultados(jugadores_nombres,jugadores_puntos_salas_matriz)
    guardar_resultados(jugadores_nombres,jugadores_puntos_salas_matriz)


def correr_salas(jugadores_nombres,matriz_jugadores_pts):
    for x in range(len(jugadores_nombres)): # x funciona como contador_jugador
        print_division()
        print(f'Hola {jugadores_nombres[x]}!')

        contador_sala = 0
        perdio = False
        while (contador_sala < CANTIDAD_SALAS) and (not perdio):
            sala_respuesta_correcta = acertijos[contador_sala]['Respuesta Correcta']
            sala_puntos = acertijos[contador_sala]['Puntos']
            presentacion_acertijos(acertijos,contador_sala)

            intento_aprobado = correr_intentos(sala_respuesta_correcta,contador_sala)

            if (intento_aprobado):
                matriz_jugadores_pts[x][contador_sala] = sala_puntos
                input('Pasas de sala!')
                contador_sala += 1
            else:
                input('Perdiste el juego!')
                for y in range(contador_sala,CANTIDAD_SALAS):
                    matriz_jugadores_pts[x][y] = 0
                perdio = True

        jugador_print_resultados(x,matriz_jugadores_pts)

def correr_intentos(respuesta_correcta,contador_sala):
    intentos_restantes = 0
    intento_aprobado = False

    while (intentos_restantes < CANTIDAD_INTENTOS) and (not intento_aprobado):
        respuesta_jugador = get_respuesta(contador_sala)

        if (get_respuesta_aprobada(respuesta_jugador,respuesta_correcta)):
            print('Adivinaste!')
            intento_aprobado = True
        else:
            intentos_restantes += 1
            input('Respuesta equivocada!')
    
    return intento_aprobado

def get_respuesta(contador_sala):
    respuestas_disponibles = acertijos[contador_sala]['Respuestas']
    respuesta_jugador = int(input('Ingrese su respuesta: \n'))

    while (respuesta_jugador not in respuestas_disponibles):
        print('La respuesta no está disponible.')
        print(f'Respuestas posibles: {respuestas_disponibles}')
        respuesta_jugador = int(input('Ingrese una respuesta válida: '))

    return respuesta_jugador

def get_respuesta_aprobada(respuesta_ingresada,respuesta_correcta):
    respuesta_aprobada = False
    if respuesta_ingresada == respuesta_correcta:
        respuesta_aprobada = True
    return respuesta_aprobada

def jugador_print_resultados(contador_jugador,matriz_jugadores_pts):
    print_division()
    input('VER RESULTADOS')
    puntos_totales = 0
    for x in range(CANTIDAD_SALAS):
        print(f'Sala {x+1:<20} Puntos: {matriz_jugadores_pts[contador_jugador][x]}')
        puntos_totales += matriz_jugadores_pts[contador_jugador][x]
    print(f'Puntos Totales: {puntos_totales}')

def torneo_print_resultados(jugadores_nombres,matriz_jugadores_puntos):
    jugadores_cantidad = len(jugadores_nombres)
    jugadores_puntos_totales = [[]] * jugadores_cantidad
    print_division()
    input('RESULTADOS DEL TORNEO')
    print_division()

    puntaje_mayor = 0
    for x in range(jugadores_cantidad):
        jugador_actual_puntos = 0
        for y in range(CANTIDAD_SALAS):
            jugador_actual_puntos += matriz_jugadores_puntos[x][y]
            jugadores_puntos_totales[x] = jugador_actual_puntos

    puntaje_mayor = max(jugadores_puntos_totales)

    for x in range(jugadores_cantidad):
        if (jugadores_puntos_totales[x] == puntaje_mayor):
            print(f'Jugador/es Ganador/es: {jugadores_nombres[x]}')
    
    for x in range(jugadores_cantidad):
        contador_salas_superadas = 0
        for y in range(CANTIDAD_SALAS):
            if (matriz_jugadores_puntos[x][y] > 1):
                contador_salas_superadas += 1
        print(f'El jugador {jugadores_nombres[x]} superó {contador_salas_superadas} salas!')

def guardar_resultados(jugadores,matriz_puntos):
    lista_jugadores = []
    puntos = [[]] * len(jugadores)

    for x in range(len(jugadores)):
        puntos[x] = 0
        
        for y in range(CANTIDAD_SALAS):
            puntos[x] += matriz_puntos[x][y]

        lista_jugadores.append({
            'Nombre': jugadores[x],
            'Puntos Totales': puntos[x]
        })
    with open('./resultados.json','w') as resultados_json:
        json.dump(lista_jugadores,resultados_json,indent=4)

main()