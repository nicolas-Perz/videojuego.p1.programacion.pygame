import json
from configuraciones import *
from acertijos import *

def pantalla_resultados_torneo():
    PANTALLA_SUPERFICIE.fill(COLOR_NEGRO)
    definir_background_pantalla(background_negro)

    rect_texto = pygame.Rect(PANTALLA_ANCHO/2,margen_top,500,0)
    mostrar_texto_superficie(PANTALLA_SUPERFICIE,'RESULTADOS TORNEO',COLOR_BLANCO,
                             (PANTALLA_ANCHO/2 - rect_texto.width/2,rect_texto.y),FUENTE_SIZE_MEDIUM)
    
    with open ('./jugadores.json','r') as jugadores_json:
        jugadores = json.load(jugadores_json)
        jugadores = sorted(jugadores, key=lambda x: int(x['Puntos Totales']), reverse=True)

        posicionY = rect_texto.y + 150
        for jugador in jugadores:
            rect_jugador = pygame.Rect(PANTALLA_ANCHO/2,0,200,0)
            mostrar_texto_superficie(PANTALLA_SUPERFICIE,jugador['Nombre'],COLOR_BLANCO,
                                     (PANTALLA_ANCHO/2 - rect_jugador.width/2,posicionY),FUENTE_SIZE_SMALL)
            mostrar_texto_superficie(PANTALLA_SUPERFICIE,str(jugador['Puntos Totales']),COLOR_BLANCO,
                                     (PANTALLA_ANCHO/2 - rect_jugador.width/2 + 200,posicionY),FUENTE_SIZE_SMALL)
            posicionY += 40

    boton_salir = pygame.Rect(margen_right + 100,margen_bottom,BOTON_ANCHO - 100,BOTON_ALTO)
    mostrar_texto_superficie(PANTALLA_SUPERFICIE,'SALIR',COLOR_BLANCO,(boton_salir.x,boton_salir.y),FUENTE_SIZE_SMALL)

    boton_regresar = pygame.Rect(margen_right - 50,margen_bottom - boton_salir.height - 30,BOTON_ANCHO + 35,BOTON_ALTO)
    mostrar_texto_superficie(PANTALLA_SUPERFICIE,'MENU PRINCIPAL',COLOR_BLANCO,(boton_regresar.x,boton_regresar.y),FUENTE_SIZE_SMALL)

    pygame.display.update()

    salir = False
    regresar = False
    while (not salir) and (not regresar):
        for evento in pygame.event.get():
            if (evento.type == pygame.QUIT):
                salir = True
            elif (evento.type == pygame.MOUSEBUTTONDOWN):
                if (boton_salir.collidepoint(evento.pos)):
                    salir = True
                elif (boton_regresar.collidepoint(evento.pos)):
                    regresar = True
    
    return regresar