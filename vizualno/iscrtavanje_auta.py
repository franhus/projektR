import pygame

PLAVA = (0, 0, 255)
CRVENA = (255, 0, 0)

def nacrtaj_auto(ekran, auto):
    x, y = auto.pozicija()
    velicina = auto.velicina
    
    # pozicije i dimenzija auta
    kvadrat = pygame.Rect(x - (velicina / 2), y - (velicina / 2), velicina, velicina)
    boja = CRVENA if auto.sudar else PLAVA
    pygame.draw.rect(ekran, boja, kvadrat)