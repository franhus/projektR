import sys
import os
import time
from glavno.staza_model import Staza
from glavno.auto_model import Auto

VIZUALNO = True

# dohvat podataka
putanja = os.path.join("staze", "nacrtana_staza.txt")
staza = Staza(putanja)
auto = Auto(staza.linija, staza.vanjske, staza.unutarnje)

if VIZUALNO:
    from vizualno.gui import pokreni_prikaz
    pokreni_prikaz(staza, auto)
else:
    print("Pokrecem simulaciju bez vizualnog dijela")
    t0 = time.time()

    while not auto.sudar and auto.indeks < len(staza.linija):
        auto.pomakni()
        
    tn = time.time()
    vrijeme = tn - t0

    if not auto.sudar:
        print("Auto je prosao stazu u ", vrijeme, " sekundi")
    else:
        print("Auto je izasao izvan granica staze na ", auto.pozicija())