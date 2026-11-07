import pygame
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

    while radi:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                radi = False

        auto.pomakni()
        ekran.fill(BIJELA)
        
        # iscrtavanje elemenata
        nacrtaj_stazu(ekran, staza)
        nacrtaj_auto(ekran, auto)
        
        # refresh
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()