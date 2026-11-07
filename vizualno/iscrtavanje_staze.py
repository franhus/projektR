import pygame

CRVENA = (255, 0, 0)
ZELENA = (0, 255, 0)
CRNA = (0, 0, 0)

def nacrtaj_stazu(ekran, staza):
    # granice
    pygame.draw.aalines(ekran, CRVENA, False, staza.vanjske)
    pygame.draw.aalines(ekran, CRVENA, False, staza.unutarnje)

    # start/cilj
    cilj_vanjski = staza.vanjske[0]
    cilj_unutarnji = staza.unutarnje[0]
    pygame.draw.line(ekran, CRNA, cilj_vanjski, cilj_unutarnji, 2)

    # linija
    prikaz_linije = True
    if prikaz_linije:
        pygame.draw.aalines(ekran, ZELENA, False, staza.linija)

