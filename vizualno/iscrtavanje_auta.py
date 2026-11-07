import pygame

PLAVA = (0, 0, 255)

def nacrtaj_auto(ekran, auto):
    x, y = auto.pozicija()
    velicina = auto.velicina
    
    # pozicije i dimenzija auta
    kvadrat = pygame.Rect(x - (velicina / 2), y - (velicina / 2), velicina, velicina)

    pygame.draw.rect(ekran, PLAVA, kvadrat)