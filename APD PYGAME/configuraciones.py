import pygame

CANT_SALAS = 4
CANT_INTENTOS = 2

FUENTE = './fuente.otf'
FUENTE_SIZE_SMALL = 25
FUENTE_SIZE_MEDIUM = 50
FUENTE_SIZE_BIG = 80

PANTALLA_ANCHO = 1300
PANTALLA_ALTO = 700
PANTALLA_SUPERFICIE = pygame.display.set_mode((PANTALLA_ANCHO,PANTALLA_ALTO))

BOTON_ANCHO = 175
BOTON_ALTO = 25

MARGEN_HORIZONTAL = 0.025
MARGEN_VERTICAL = 0.10

margen_left = PANTALLA_ANCHO * MARGEN_HORIZONTAL
margen_right = (PANTALLA_ANCHO - BOTON_ANCHO - margen_left)
margen_top = PANTALLA_ALTO * MARGEN_VERTICAL
margen_bottom = PANTALLA_ALTO - BOTON_ALTO - margen_top

COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)

def mostrar_texto_superficie(superficie,texto,color,coord,fuente_size):
    fuente = pygame.font.Font(FUENTE,fuente_size)
    texto_renderizado = fuente.render(texto,True,color)
    superficie.blit(texto_renderizado,coord)

background_blanco = ('./background.jpg')
background_negro = ('./background2.jpg')

def definir_background_pantalla(ruta_imagen):
    background = pygame.image.load(ruta_imagen)
    background = pygame.transform.scale(background,(PANTALLA_ANCHO,PANTALLA_ALTO))
    PANTALLA_SUPERFICIE.blit(background,(0,0))