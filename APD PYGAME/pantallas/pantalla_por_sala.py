import json
from configuraciones import *
from acertijos import *
from pantallas.pantalla_mostrar_resultados_jugador import pantalla_mostrar_resultados_jugador

def pantalla_por_sala():

    with open('./jugadores.json','r') as jugadores_json:
        jugadores = json.load(jugadores_json)
    
    contador_jugador = 0
    for jugador in jugadores:
        PANTALLA_SUPERFICIE.fill(COLOR_NEGRO)
        definir_background_pantalla(background_negro)
        jugador_nombre = jugador['Nombre']
        lista_botones = pantalla_por_sala_definir_botones()
        contador_salas = pantalla_por_sala_correr(lista_botones,contador_jugador,jugador_nombre)
        pantalla_mostrar_resultados_jugador(contador_jugador,contador_salas)
        contador_jugador += 1

def pantalla_por_sala_definir_botones():
    boton_ancho_op = PANTALLA_ANCHO/2  - 50
    boton_alto_op = PANTALLA_ALTO/4
    lista_botones = []

    for x in range(2): # (x == 0) -> boton a la izquierda
        for y in range(2): # (y == 0) -> boton arriba
            if (x == 0):
                boton_X = margen_left
            else:
                boton_X = PANTALLA_ANCHO/2
            
            if (y == 0):
                boton_Y = PANTALLA_ALTO/2 - 50
            else:
                boton_Y = margen_bottom - 100

            boton_op = pygame.Rect(boton_X,boton_Y,boton_ancho_op,boton_alto_op)
            lista_botones.append(boton_op)

    return lista_botones

def pantalla_por_sala_correr(botones,contador_jugador,jugador_nombre):
    contador_sala = 0
    jugador_intentos = 0

    respondiendo = True
    while (respondiendo) and (contador_sala < CANT_SALAS) and (jugador_intentos < CANT_INTENTOS):
        sala_acertijo = acertijos[contador_sala]['Acertijo']
        sala_respuestas = acertijos[contador_sala]['Respuestas']
        sala_respuesta_correcta = acertijos[contador_sala]['Respuesta Correcta']

        rect_nombre = pygame.Rect(PANTALLA_ANCHO/2,margen_top,300,100)
        mostrar_texto_superficie(PANTALLA_SUPERFICIE,jugador_nombre,COLOR_BLANCO,(PANTALLA_ANCHO/2 - rect_nombre.width/2,rect_nombre.y),FUENTE_SIZE_MEDIUM)

        rect_acertijo = pygame.Rect(PANTALLA_ANCHO/2,rect_nombre.y + 50,300,100)
        mostrar_texto_superficie(PANTALLA_SUPERFICIE,sala_acertijo.upper(),COLOR_BLANCO,(PANTALLA_ANCHO/2 - rect_acertijo.width/2,rect_acertijo.y),FUENTE_SIZE_MEDIUM)

        opcion_correcta_rect,lista_opciones_incorrectas = ubicar_respuestas_botones(botones,sala_respuestas,sala_respuesta_correcta)

        for evento in pygame.event.get():
            if (evento.type == pygame.QUIT):
                respondiendo = False
            
            elif (evento.type == pygame.MOUSEBUTTONDOWN):
                if (opcion_correcta_rect.collidepoint(evento.pos)):
                    print('Adivinaste!')
                    sumar_puntos_jugador(contador_jugador,contador_sala)
                    jugador_intentos = 0
                    contador_sala += 1
                    PANTALLA_SUPERFICIE.fill(COLOR_NEGRO)
                    definir_background_pantalla(background_negro)
                else:
                    for opcion_incorrecta in lista_opciones_incorrectas:
                        if (opcion_incorrecta.collidepoint(evento.pos)):
                            print('¡Mal!')
                            jugador_intentos += 1
        pygame.display.update()
    return contador_sala

def ubicar_respuestas_botones(lista_botones,respuestas,respuesta_correcta):
    lista_respuestas_incorrectas = []
    for x in range(len(lista_botones)):
        pygame.draw.rect(PANTALLA_SUPERFICIE,COLOR_BLANCO,lista_botones[x])

        if (str(respuestas[x]) == str(respuesta_correcta)):
            respuesta_correcta_rect = pygame.Rect(lista_botones[x].x,lista_botones[x].y,lista_botones[x].width,lista_botones[x].height)
            mostrar_texto_superficie(PANTALLA_SUPERFICIE,str(respuesta_correcta),COLOR_NEGRO,
                                     (respuesta_correcta_rect.x + 40,respuesta_correcta_rect.y + 40),FUENTE_SIZE_BIG)
        else:
            respuesta_incorrecta_rect = pygame.Rect(lista_botones[x].x,lista_botones[x].y,lista_botones[x].width,lista_botones[x].height)
            lista_respuestas_incorrectas.append(respuesta_incorrecta_rect)
            mostrar_texto_superficie(PANTALLA_SUPERFICIE,str(respuestas[x]),COLOR_NEGRO,
                                     (respuesta_incorrecta_rect.x + 40,respuesta_incorrecta_rect.y + 40),FUENTE_SIZE_BIG)
    return respuesta_correcta_rect,lista_respuestas_incorrectas

def sumar_puntos_jugador(contador_jugador,contador_sala):
    jugador_puntos = acertijos[contador_sala]['Puntos']

    with open ('./jugadores.json','r') as archivo_json:
        jugadores_datos = json.load(archivo_json)
    
    jugadores_datos[contador_jugador]['Puntos Totales'] += jugador_puntos

    with open ('./jugadores.json','w') as archivo_json:
        json.dump(jugadores_datos,archivo_json,indent=4)