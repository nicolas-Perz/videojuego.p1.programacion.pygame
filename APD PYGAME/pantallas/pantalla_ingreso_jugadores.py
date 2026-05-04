import json
from configuraciones import *

def pantalla_ingreso_jugadores():

    PANTALLA_SUPERFICIE.fill(COLOR_BLANCO)
    definir_background_pantalla(background_blanco)

    rect_texto = pygame.Rect(PANTALLA_ANCHO/2,margen_top,PANTALLA_ANCHO/2,0)
    mostrar_texto_superficie(PANTALLA_SUPERFICIE,'INGRESE JUGADORES',COLOR_NEGRO,(PANTALLA_ANCHO/2 - rect_texto.width/2,rect_texto.y + 25),FUENTE_SIZE_MEDIUM)

    boton_confirmar = pantalla_ingreso_jugadores_definir_botones()
    pantalla_ingreso_jugadores_dibujar_botones(boton_confirmar)

    rect_input = pantalla_ingreso_jugadores_definir_input()
    pygame.draw.rect(PANTALLA_SUPERFICIE,COLOR_NEGRO,rect_input)

    pygame.display.update()
    ingresar_jugadores(rect_input,boton_confirmar)

def pantalla_ingreso_jugadores_definir_botones():
    boton_confirmar_left = margen_right
    boton_confirmar_top = margen_bottom

    boton_confirmar = pygame.Rect(boton_confirmar_left,boton_confirmar_top,BOTON_ANCHO,BOTON_ALTO)
    return boton_confirmar

def pantalla_ingreso_jugadores_dibujar_botones(boton_confirmar):
    mostrar_texto_superficie(PANTALLA_SUPERFICIE,'CONFIRMAR',COLOR_NEGRO,
                             (boton_confirmar.x,boton_confirmar.y),FUENTE_SIZE_SMALL)

def pantalla_ingreso_jugadores_definir_input():
    rect_input_ancho = 300
    rect_input_alto = 50
    rect_input_left = (PANTALLA_ANCHO/2) - rect_input_ancho/2
    rect_input_top = margen_bottom
    
    rect_input = pygame.Rect(rect_input_left,rect_input_top,rect_input_ancho,rect_input_alto)
    return rect_input

def ingresar_jugadores(rect_input,confirmar):
    jugadores_nombres = []
    superficie_input = pygame.Surface((rect_input.width,rect_input.height))
    
    ingresando = True
    while (ingresando):
        for evento in pygame.event.get():
            
            if (evento.type == pygame.MOUSEBUTTONDOWN):
                if (rect_input.collidepoint(evento.pos)):
                    letra_escrita = capturar_texto(superficie_input,(rect_input.x,rect_input.y))
                    jugadores_nombres.append(letra_escrita)
                    jugadores_guardar(jugadores_nombres)
                    jugadores_nombres_mostrar(jugadores_nombres)
                    pygame.display.update()
                elif (confirmar.collidepoint(evento.pos)):
                    if len(jugadores_nombres) >= 1:
                        PANTALLA_SUPERFICIE.fill(COLOR_NEGRO)
                        ingresando = False

def capturar_texto(superficie,coord):
    texto_ingresado = ''
    color_superficie = superficie.get_at((0,0))

    escribiendo = True
    while (escribiendo):
        for evento in pygame.event.get():
            if (evento.type == pygame.KEYDOWN):
                if (evento.key == pygame.K_RETURN):
                    if (texto_ingresado.strip() == ''):
                        texto_ingresado = ''
                        escribiendo = True
                    else:
                        escribiendo = False
                elif (evento.key == pygame.K_BACKSPACE):
                    texto_ingresado = texto_ingresado[:-1]
                else:
                    texto_ingresado += evento.unicode
                    texto_ingresado = texto_ingresado.upper()
        superficie.fill(color_superficie)
        mostrar_texto_superficie(superficie,texto_ingresado,COLOR_BLANCO,(0,0),FUENTE_SIZE_SMALL)

        PANTALLA_SUPERFICIE.blit(superficie,coord)
        pygame.display.update()

    texto_ingresado = texto_ingresado.strip()

    return texto_ingresado

def jugadores_guardar(jugadores):
    lista_jugadores = []
    for jugador in jugadores:
        lista_jugadores.append({
            'Nombre': jugador,
            'Puntos Totales': 0,
        })
    with open ('./jugadores.json','w') as archivo_json:
        json.dump(lista_jugadores,archivo_json,indent=4)

def jugadores_nombres_mostrar(jugadores):
    posicionY = 200
    for jugador in jugadores:
        rect_nombre = pygame.Rect(PANTALLA_ANCHO,margen_top,100,0)
        mostrar_texto_superficie(PANTALLA_SUPERFICIE,jugador,COLOR_NEGRO,
                                 (PANTALLA_ANCHO/2 - rect_nombre.width/2 , posicionY),FUENTE_SIZE_SMALL)
        posicionY += 40