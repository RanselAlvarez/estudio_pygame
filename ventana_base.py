import pygame
from random import randint
import math

pygame.init()

ANCHO, ALTO = 1000, 800
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("GAME")


#==========================================================
# JUGADOR
#Posicion de la figura en la pantalla
jugador_x, jugador_y = ANCHO//2, ALTO//2

# Medidas de la figura
color_jugador = (255, 200, 0) # Color inicial
radio_jugador = 30
velocidad = 10

#==========================================================
# Circulo enemigo (estatico por el momento)
enemigo_x, enemigo_y = 300, 300
radio_enemigo = 50
color_enemigo = (255, 50, 50)  # Rojo


# Esto es para los FPS
reloj = pygame.time.Clock()



colision_time = 0
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
            
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                # Color aleatorio del circulo
                r = randint(0, 255)
                g = randint(0, 255)
                b = randint(0, 255)
                color_jugador = (r, g, b)
                jugador_x, jugador_y = ANCHO //2, ALTO // 2
        
        
        
        
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_LEFT]:
        jugador_x -= velocidad
    
    if teclas[pygame.K_RIGHT]:
        jugador_x += velocidad
    
    if teclas[pygame.K_UP]:
        jugador_y -= velocidad
        
    if teclas[pygame.K_DOWN]:
        jugador_y += velocidad

    # --- LÍMITES DE PANTALLA ---
    if jugador_x - radio_jugador < 0:
        jugador_x = radio_jugador
    if jugador_x + radio_jugador > ANCHO:
        jugador_x = ANCHO - radio_jugador
    if jugador_y - radio_jugador < 0:
        jugador_y = radio_jugador
    if jugador_y + radio_jugador > ALTO:
        jugador_y = ALTO - radio_jugador
    # -----------------------------------------
    
    #---DETECCION DE COLISION----#
    distancia = math.hypot(jugador_x - enemigo_x, jugador_y - enemigo_y)
    if distancia < (radio_jugador + radio_enemigo):
        colision_time = pygame.time.get_ticks()
        if pygame.time.get_ticks() - colision_time < 1000:
            color_jugador = (255, 255, 255)
            # Accion e colision(resetear la posicion del jugador)
            jugador_x, jugador_y = ANCHO // 2, ALTO //2
            
            
            
            
    pantalla.fill((255, 120, 255))
    # Dibujar el circulo del jugador
    pygame.draw.circle(pantalla, color_jugador, (jugador_x, jugador_y), radio_jugador)

    # Dibujar el circulo del enemigo
    pygame.draw.circle(pantalla, color_enemigo, (enemigo_x, enemigo_y), radio_enemigo)
    
    pygame.display.flip()
    reloj.tick(60)
    
    
pygame.quit()
