import pygame
from vizualno.iscrtavanje_staze import nacrtaj_stazu

DIMENZIJA = 800
BIJELA = (255, 255, 255)
FPS = 60

def pokreni_prikaz(staza):
    pygame.init()
    ekran = pygame.display.set_mode((DIMENZIJA, DIMENZIJA))
    pygame.display.set_caption("Simulacija")
    
    clock = pygame.time.Clock()
    radi = True

    while radi:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                radi = False

        ekran.fill(BIJELA)
        
        # Iscrtavanje elemenata
        nacrtaj_stazu(ekran, staza)
        # nacrtaj_autic(ekran, autic)  <-- ovdje dodajemo autić u sljedećem koraku
        
        # Osvježavanje prikaza
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()