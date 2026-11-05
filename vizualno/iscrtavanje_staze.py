import pygame

PLAVA = (0, 0, 255)
CRVENA = (255, 0, 0)

def nacrtaj_stazu(ekran, staza):
    pygame.draw.aalines(ekran, PLAVA, False, staza.vanjske)
    pygame.draw.aalines(ekran, CRVENA, False, staza.unutarnje)
    print("aa")
