import pygame
import math

CRVENA = (255, 0, 0)
ZELENA = (0, 255, 0)
CRNA = (0, 0, 0)
LJUBICASTA = (139, 0, 139)

def nacrtaj_stazu(ekran, staza):
    # segmenti
    prikaz_segmenata = True
    if prikaz_segmenata:
        for segment in staza.segmenti:
            pygame.draw.lines(ekran, LJUBICASTA, True, segment, 1)

    # granice
    pygame.draw.aalines(ekran, CRVENA, False, staza.vanjske)
    pygame.draw.aalines(ekran, CRVENA, False, staza.unutarnje)

    # start/cilj
    pocetak = staza.linija[0]
    tocke_sortirano = sorted(staza.segmenti[0], key=lambda t: math.hypot(t[0] - pocetak[0], t[1] - pocetak[1]))
    pygame.draw.line(ekran, CRNA, tocke_sortirano[0], tocke_sortirano[1], 2)

    # linija
    prikaz_linije = True
    if prikaz_linije:
        pygame.draw.aalines(ekran, ZELENA, False, staza.linija)

    