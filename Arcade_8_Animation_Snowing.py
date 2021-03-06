import pygame  #importando pygame
import random
#Definiendo colores
NEGRO = (0, 0 , 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

PI = 3.141592653  #estableciendo pi

pygame.init()  #initializating

#Haciendo la cochina ventana
dimensiones = (700, 700)
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Está Nevando") #poniendole titulo
copos = 50
lista_nieve = [] * copos

for i in range(copos):
    x = random.randrange(0, 700)
    y = random.randrange(0, 700)
    lista_nieve.append([x, y])

hecho = False #Hasta que el usuario cierre la aplicacion.

reloj = pygame.time.Clock() #gestionar cuan rapido se actualiza la pantalla

#-----Bucle principal del programa------
while not hecho:

    for evento in pygame.event.get():   # El usuario hizo algo
        if evento.type == pygame.QUIT:  # si el usuario pincha sobre cerrar
            hecho = True                # Acabamos y salimos del bucle

    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERIAN IR ENCIMA DE ESTE COMENTARIO

    # TODA LA LOGICA DEL JUEGO DEBERIA IR DEBAJO DE ESTE COMENTARIO
    # TODA LA LOGICA DEL JUEGO DEBERIA IR ENCIMA DE ESTE COMENTARIO

    # EL CODIGO DE DIBUJO DEBERIA IR DEBAJO DE ESTE COMENTARIO
    # EL CODIGO DE DIBUJO DEBERIA IR ENCIMA DE ESTE COMENTARIO

    pantalla.fill(NEGRO) # Primero, limpia la pantalla con negro.

    for i in range(len(lista_nieve)):
        # Dibuja el copo de nieve
        pygame.draw.circle(pantalla, BLANCO, lista_nieve[i], 2)
        # Mueve el copo un pixel hacia abajo
        lista_nieve[i][1] += 1

        if lista_nieve[i][1] > 700:  # Si el copo ya se salió de la pantalla
            y = random.randrange(-50, -10)
            lista_nieve[i][1] = y
            x = random.randrange(0, 700)
            lista_nieve[i][0] = x

    pygame.display.flip() # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.

    reloj.tick(60) # Limita a 60 fotogramas por segundo (frames per second)
pygame.quit()
