import sys
import os
from glavno.staza_model import Staza

VIZUALNO = True

# Dohvat podataka
putanja = os.path.join("staze", "nacrtana_staza.txt")
staza = Staza(putanja)

if VIZUALNO:
    from vizualno.gui import pokreni_prikaz
    pokreni_prikaz(staza)
else:
    print("Pokrecem simulaciju bez vizualnog dijela")