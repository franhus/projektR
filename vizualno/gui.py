import pygame
import time
from vizualno.iscrtavanje_staze import nacrtaj_stazu
from vizualno.iscrtavanje_auta import nacrtaj_auto

DIMENZIJA = 800
BIJELA = (255, 255, 255)
FPS = 60

def pokreni_prikaz(staza, auto):
    pygame.init()
    ekran = pygame.display.set_mode((DIMENZIJA, DIMENZIJA))
    pygame.display.set_caption("Simulacija")
    
    clock = pygame.time.Clock()
    radi = True

    t0 = time.time()
    tn = None

    while radi:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                radi = False

        if not auto.sudar and auto.indeks < len(staza.linija):
            auto.pomakni()
            if auto.indeks >= len(staza.linija):
                tn = time.time()
            
        ekran.fill(BIJELA)
        
        # iscrtavanje elemenata
        nacrtaj_stazu(ekran, staza)
        nacrtaj_auto(ekran, auto)
        
        # refresh
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

    return tn - t0