# paletas.py

import pygame
from pygame import *
import constantes


class paleta:
    def __init__(self, x, y):
        # Tamaño de la paleta
        self.ancho = 10
        self.alto = 60
        self.x = x
        self.y = y
        
        # Crear la superficie de la paleta y su rectángulo (rect)
        self.image = pygame.Surface((self.ancho, self.alto))
        self.image.fill((255, 255, 255))  # Color de la paleta
        self.rect = self.image.get_rect(topleft=(self.x, self.y))  

    def mover_paletas(self, delta_x, delta_y):
        self.rect.x += delta_x
        self.rect.y += delta_y

        # Restringir la paleta dentro de los límites de la pantalla, considerando el marcador
        if self.rect.top < 50:  
            self.rect.top = 50
        if self.rect.bottom > constantes.ALTO: 
            self.rect.bottom = constantes.ALTO

    def dibujar_paletas(self, pantalla):
        pantalla.blit(self.image, self.rect)



class Pelota:
    def __init__(self, x, y):
        self.radio = 10  
        self.color = (255, 255, 0)  # Color de la pelota (amarillo)
        self.velocidad_x = 5
        self.velocidad_y = 5
        
        # Crear la superficie para la pelota (circular)
        self.image = pygame.Surface((2 * self.radio, 2 * self.radio), pygame.SRCALPHA)  
        pygame.draw.circle(self.image, self.color, (self.radio, self.radio), self.radio)  
        self.rect = self.image.get_rect(center=(x, y))  
    def mover(self, jugador_1, jugador_2):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Rebotar en los bordes superior e inferior, evitando que se mueva por encima del marcador
        if self.rect.top < 50:  
            self.velocidad_y = -self.velocidad_y
            self.rect.top = 50  

        if self.rect.bottom > constantes.ALTO:  # Borde inferior de la pantalla
            self.velocidad_y = -self.velocidad_y
            self.rect.bottom = constantes.ALTO

        # Rebotar en las paletas
        if self.rect.colliderect(jugador_1.rect) or self.rect.colliderect(jugador_2.rect):
            self.velocidad_x = -self.velocidad_x

    def dibujar_pelota(self, ventana):
        ventana.blit(self.image, self.rect)

    # Método reset para reposicionar la pelota en el centro
    def reset(self):
        self.rect.center = (constantes.ANCHO // 2, constantes.ALTO // 2)
        self.velocidad_x = -self.velocidad_x  
        self.velocidad_y = 5  



