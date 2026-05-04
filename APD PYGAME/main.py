from configuraciones import *
from pantallas.pantalla_menu_principal import pantalla_menu_principal
from pantallas.pantalla_ingreso_jugadores import pantalla_ingreso_jugadores
from pantallas.pantalla_por_sala import pantalla_por_sala
from pantallas.pantalla_mostrar_resultados_torneo import pantalla_resultados_torneo

def main():
    pygame.init()
    pygame.mixer.init()

    jugando = True
    while (jugando):
        pygame.mixer.music.load('Alone-Takanaka.ogg')
        pygame.mixer.music.play(-1)
        continuar = pantalla_menu_principal()
        if (continuar):
            pantalla_ingreso_jugadores()
            pantalla_por_sala() # llamo a pantalla_mostrar_resultados_jugadores dentro de pantalla_por_sala
            regresar = pantalla_resultados_torneo()
            if (regresar):
                main()
        jugando = False
main()