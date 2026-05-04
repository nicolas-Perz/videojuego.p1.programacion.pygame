import json
from constantes import *
from funciones import *
from pantallas.pantalla_por_sala import pantalla_por_sala

def pantalla_por_jugador():
    # Cargo el archivo con los jugadores
    with open('./jugadores.json', 'r', encoding='utf-8') as archivo_json:
        jugadores = json.load(archivo_json)
        
    # Printeo el nombre
    contador_jugador = 0
    for jugador in jugadores:
        nombre = jugador['Nombre']
        mostrar_texto_superficie(PANTALLA_SUPERFICIE,f'¡BIENVENIDO {nombre}!',(255,255,255),
                                 (PANTALLA_ANCHO/2 - 200,MARGEN_TOP),FUENTE_SIZE_MEDIUM)
        pygame.display.update()
        pantalla_por_sala(contador_jugador)
        contador_jugador += 1