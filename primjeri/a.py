import pygame

# Obavezna inicijalizacija
pygame.init()

# Postavljanje dimenzija prozora
ekran = pygame.display.set_mode((800, 600))
pygame.display.set_caption("crtanje staze sa pygame")

# Definiranje boja (RGB format)
BIJELA = (255, 255, 255)
PLAVA = (0, 0, 255)
CRVENA = (255, 0, 0)

# Glavna petlja
radi = True
while radi:
    # 1. Obrada događaja (omogućava gašenje prozora na 'X')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            radi = False

    # 2. Čišćenje ekrana (ispunjavanje bojom pozadine)
    ekran.fill(BIJELA)

    # 3. Crtanje obične linije od točke A do točke B
    # Sintaksa: pygame.draw.line(površina, boja, početna_točka, završna_točka, debljina)
    pygame.draw.line(ekran, CRVENA, (100, 100), (700, 500), 5)

    # Napomena: Za tvoju stazu trebat će ti funkcija koja crta niz povezanih točaka:
    niz_tocaka = [(100, 300), (400, 300), (600, 100)]
    # Sintaksa: pygame.draw.lines(površina, boja, zatvori_liniju, lista_točaka, debljina)
    pygame.draw.lines(ekran, PLAVA, False, niz_tocaka, 3)

    # 4. Osvježavanje prikaza (iscrtava sve što smo definirali)
    pygame.display.flip()

# Gašenje modula nakon izlaska iz petlje
pygame.quit()