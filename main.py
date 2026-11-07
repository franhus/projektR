import sys
import os
from glavno.staza_model import Staza
from glavno.auto_model import Auto

VIZUALNO = True

# dohvat podataka
putanja = os.path.join("staze", "nacrtana_staza.txt")
staza = Staza(putanja)
auto = Auto(staza.linija)

if VIZUALNO:
    from vizualno.gui import pokreni_prikaz
    pokreni_prikaz(staza, auto)
else:
    print("Pokrecem simulaciju bez vizualnog dijela")