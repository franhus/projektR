import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev
from shapely import LineString
import pygame
import os

# dohvat podataka
fajl = "nacrtana_staza.npz"
podaci = np.load(os.path.join("staze", fajl))
tocke_linije = podaci["linija"].tolist()
vanjske_tocke = podaci["vanjske"].tolist()
unutarnje_tocke = podaci["unutarnje"].tolist()

# 

#PyGame iscrtavanje
pygame.init()
ekran = pygame.display.set_mode((800, 800))

BIJELA = (255, 255, 255)
PLAVA = (0, 0, 255)
CRVENA = (255, 0, 0)
radi = True
while radi:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            radi = False

    ekran.fill(BIJELA)

    pygame.draw.aalines(ekran, PLAVA, False, vanjske_tocke, 2)
    pygame.draw.aalines(ekran, CRVENA, False, unutarnje_tocke, 2)

    pygame.display.flip()
pygame.quit()