import json
from configuraciones import *
from acertijos import *

def pantalla_mostrar_resultados_jugador(contador_jugador,contador_salas):
    PANTALLA_SUPERFICIE.fill(COLOR_BLANCO)
    definir_background_pantalla(background_blanco)

    rect_texto = pygame.Rect(PANTALLA_ANCHO,PANTALLA_ALTO,500,100)
    mostrar_texto_superficie(PANTALLA_SUPERFICIE,'RESULTADOS',COLOR_NEGRO,(PANTALLA_ANCHO/2 - rect_texto.width/2 + 100,margen_top),FUENTE_SIZE_MEDIUM)

    with open ('./jugadores.json','r') as registro:
        jugadores = json.load(registro)
        posicionY = 200

        for x in range(contador_salas):
            rect_texto_sala = pygame.Rect(0,0,100,0)
            mostrar_texto_superficie(PANTALLA_SUPERFICIE,f'SALA {x+1}',COLOR_NEGRO,
                                     (PANTALLA_ANCHO/2 - rect_texto_sala.width/2,posicionY),FUENTE_SIZE_SMALL)
            mostrar_texto_superficie(PANTALLA_SUPERFICIE,str(acertijos[x]['Puntos']),COLOR_NEGRO,
                                     (PANTALLA_ANCHO/2 - rect_texto_sala.width/2 + 100,posicionY),FUENTE_SIZE_SMALL)
            posicionY += 45

        mostrar_texto_superficie(PANTALLA_SUPERFICIE,str(jugadores[contador_jugador]['Puntos Totales']),COLOR_NEGRO,
                                 (PANTALLA_ANCHO/2,posicionY),FUENTE_SIZE_SMALL)

    boton_continuar = pygame.Rect(margen_right,margen_bottom,BOTON_ANCHO,BOTON_ALTO)
    mostrar_texto_superficie(PANTALLA_SUPERFICIE,'CONTINUAR',COLOR_NEGRO,(boton_continuar.x,boton_continuar.y),FUENTE_SIZE_SMALL)

    pygame.display.update()

    continuar = False
    while (not continuar):
        for evento in pygame.event.get():
            if (evento.type == pygame.QUIT):
                continuar = True
            
            elif (evento.type == pygame.MOUSEBUTTONDOWN):
                if (boton_continuar.collidepoint(evento.pos)):
                    continuar = True