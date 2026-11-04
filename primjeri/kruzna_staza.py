import numpy as np
import os
import json

# Generiranje 500 točaka u krug (od 0 do 360 stupnjeva)
kutovi = np.linspace(0, 2 * np.pi, 500)
centar = 400

# Izračun koordinata matematikom
x_sredina = centar + 280 * np.cos(kutovi)
y_sredina = centar + 280 * np.sin(kutovi)

x_vanjski = centar + 312 * np.cos(kutovi)
y_vanjski = centar + 312 * np.sin(kutovi)

x_unutarnji = centar + 248 * np.cos(kutovi)
y_unutarnji = centar + 248 * np.sin(kutovi)

# Spajanje u Pygame (X, Y) format parova
tocke_sredine = list(zip(x_sredina, y_sredina))
vanjske_tocke = list(zip(x_vanjski, y_vanjski))
unutarnje_tocke = list(zip(x_unutarnji, y_unutarnji))

# Spremanje u binarnu datoteku
podaci = {
    "linija": tocke_sredine,
    "vanjske": vanjske_tocke,
    "unutarnje": unutarnje_tocke
}
# spremanje u .txt
os.makedirs("staze", exist_ok=True)
putanja = os.path.join("staze", "kruzna_staza.txt")
with open(putanja, "w") as f:
    json.dump(podaci, f, indent=4)
