import pygame
from pygame import *
import constantes
from paletas import paleta
from paletas import Pelota

# Inicializar Pygame y crear las paletas y la pelota
pygame.init()
jugador_1 = paleta(10, 245)
jugador_2 = paleta(635, 245)
pelota = Pelota(constantes.ANCHO // 2, constantes.ALTO // 2)

ventana = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))
fuente = pygame.font.Font(None, 74)
texto_jugar = fuente.render('Jugar', True, (255, 255, 255))
texto_salir = fuente.render('Salir', True, (255, 255, 255))

boton_jugar = texto_jugar.get_rect(center=(constantes.ANCHO // 2, constantes.ALTO // 2 - 50))
boton_salir = texto_salir.get_rect(center=(constantes.ANCHO // 2, constantes.ALTO // 2 + 50))

pygame.display.set_caption("Pong")

# Definir las variables de movimiento de las paletas
mover_arriba = False
mover_abajo = False
mover_arriba2 = False
mover_abajo2 = False

#Variables de puntuacion
puntos = 0
puntos_2 = 0

# Función para mostrar los puntos
def show_puntos(screen, puntos):
    text = fuente.render(f"Jugador 1: {puntos}", True, (255, 255, 255))
    screen.blit(text, (5, 5))

def show_puntos_2(screen, puntos_2):
    text = fuente.render(f"Jugador 2: {puntos_2}", True, (255, 255, 255))
    screen.blit(text, (350, 5))

mostrar_menu = True
run = True

# Controlar el frame rate
reloj = pygame.time.Clock()

while run:
    reloj.tick(constantes.FPS)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False
        if mostrar_menu:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(evento.pos):
                    mostrar_menu = False
                if boton_salir.collidepoint(evento.pos):
                    run = False
        else:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_w:
                    mover_arriba = True
                if evento.key == pygame.K_s:
                    mover_abajo = True
                if evento.key == pygame.K_UP:
                    mover_arriba2 = True
                if evento.key == pygame.K_DOWN:
                    mover_abajo2 = True
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_w:
                    mover_arriba = False
                if evento.key == pygame.K_s:
                    mover_abajo = False
                if evento.key == pygame.K_UP:
                    mover_arriba2 = False
                if evento.key == pygame.K_DOWN:
                    mover_abajo2 = False

    if mostrar_menu:
        ventana.fill((0, 0, 0))
        #para obtener la posicion de donde esa el cursor
        posicion_cursor=pygame.mouse.get_pos()
        #si el cursor se encuentra encima de la opcion cambia de color
        if boton_jugar.collidepoint(posicion_cursor):
            color_jugar = (0, 255, 0)
        else:
            color_jugar = (255, 255, 255)
        
        if boton_salir.collidepoint(posicion_cursor):
            color_salir = (0, 255, 0)
        else:
            color_salir = (255, 255, 255)

        texto_jugar = fuente.render('Jugar', True, color_jugar)
        texto_salir = fuente.render('Salir', True, color_salir)

        ventana.blit(texto_jugar, boton_jugar)
        ventana.blit(texto_salir, boton_salir)
    else:
        # Para calcular el movimiento
        delta_x = 0
        delta_y = 0
        delta_x2 = 0
        delta_y2 = 0

        if mover_arriba:
            delta_y = -8
        if mover_abajo:
            delta_y = 8
        if mover_arriba2:
            delta_y2 = -8
        if mover_abajo2:
            delta_y2 = 8

        # Mover paletas
        jugador_1.mover_paletas(delta_x, delta_y)
        jugador_2.mover_paletas(delta_x2, delta_y2)

        # Mover la pelota
        pelota.mover(jugador_1, jugador_2)

        # Borrar la pantalla
        ventana.fill((52, 76, 91))

        # Verificar si la pelota sale de la pantalla para sumar puntos
        if pelota.rect.x < 0:  # Jugador 2 marca un punto
            puntos_2 += 1
            pelota.reset()  
        elif pelota.rect.x > constantes.ANCHO:  # Jugador 1 marca un punto
            puntos += 1
            pelota.reset()  

        # Mostrar las paletas de los jugadores
        jugador_1.dibujar_paletas(ventana)
        jugador_2.dibujar_paletas(ventana)
        # Mostrar la pelota
        pelota.dibujar_pelota(ventana)

        # Mostrar los puntos
        show_puntos(ventana, puntos)
        show_puntos_2(ventana, puntos_2)

    pygame.display.flip()

pygame.quit()
