from configuraciones import *

def pantalla_menu_principal():
    PANTALLA_SUPERFICIE.fill(COLOR_NEGRO)
    definir_background_pantalla(background_negro)
    mostrar_texto_superficie(PANTALLA_SUPERFICIE,'PARCIAL 2 PROGRAMACION I',COLOR_BLANCO,(margen_left,margen_top),FUENTE_SIZE_MEDIUM)
    boton_jugar,boton_salir = pantalla_menu_principal_definir_botones()
    pantalla_menu_principal_dibujar_botones(boton_jugar,boton_salir)
    pygame.display.update()
    continuar = pantalla_menu_principal_interaccion(boton_jugar,boton_salir)
    return continuar

def pantalla_menu_principal_definir_botones():
    boton_jugar_left = margen_right
    boton_jugar_top = margen_bottom - BOTON_ALTO - 30

    boton_salir_left = margen_right
    boton_salir_top = margen_bottom

    boton_jugar = pygame.Rect(boton_jugar_left,boton_jugar_top,BOTON_ANCHO,BOTON_ALTO)
    boton_salir = pygame.Rect(boton_salir_left,boton_salir_top,BOTON_ANCHO,BOTON_ALTO)
    return boton_jugar,boton_salir

def pantalla_menu_principal_dibujar_botones(boton_jugar,boton_salir):
    mostrar_texto_superficie(PANTALLA_SUPERFICIE,'JUGAR',COLOR_BLANCO,
                             (boton_jugar.x + BOTON_ANCHO/2,boton_jugar.y),FUENTE_SIZE_SMALL)
    
    mostrar_texto_superficie(PANTALLA_SUPERFICIE,'SALIR',COLOR_BLANCO,
                             (boton_salir.x + BOTON_ANCHO/2,boton_salir.y),FUENTE_SIZE_SMALL)

def pantalla_menu_principal_interaccion(boton_jugar,boton_salir):
    continuar = False
    corriendo = True
    while (corriendo):

        for evento in pygame.event.get():
            if (evento.type == pygame.QUIT):
                corriendo = False
            
            elif (evento.type == pygame.MOUSEBUTTONDOWN):
                if (boton_jugar.collidepoint(evento.pos)):
                    PANTALLA_SUPERFICIE.fill((255,255,255))
                    continuar = True
                    corriendo = False
                elif (boton_salir.collidepoint(evento.pos)):
                    continuar = False
                    corriendo = False
    return continuar