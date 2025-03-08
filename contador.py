import pygame
import sys


pygame.init()


screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Contador de puntos")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


font = pygame.font.Font(None, 74)


puntos = 0
puntos_2 = 0


def show_puntos(screen, puntos):
    text = font.render(f"Jugador 1: {puntos}", True, BLACK)
    screen.blit(text, (5, 5))


def show_puntos_2(screen, puntos_2):
    text = font.render(f"Jugador 2: {puntos_2}", True, BLACK)
    screen.blit(text, (5, 50))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                puntos += 1
            if event.key == pygame.K_w:
                puntos_2 += 1

    screen.fill(WHITE)

    show_puntos(screen, puntos)
    show_puntos_2(screen, puntos_2)
    pygame.display.flip()


pygame.quit()
sys.exit()
