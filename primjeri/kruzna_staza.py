import numpy as np
import os

# Generiranje 300 točaka u krug (od 0 do 360 stupnjeva)
kutovi = np.linspace(0, 2 * np.pi, 300)
centar = 400

# Izračun koordinata čistom matematikom
x_sredina = centar + 280 * np.cos(kutovi)
y_sredina = centar + 280 * np.sin(kutovi)

x_vanjski = centar + 312 * np.cos(kutovi)
y_vanjski = centar + 312 * np.sin(kutovi)

x_unutarnji = centar + 248 * np.cos(kutovi)
y_unutarnji = centar + 248 * np.sin(kutovi)

# Spajanje u Pygame (X, Y) format parova
sredina_tocke = list(zip(x_sredina, y_sredina))
vanjske_tocke = list(zip(x_vanjski, y_vanjski))
unutarnje_tocke = list(zip(x_unutarnji, y_unutarnji))

# Spremanje u binarnu datoteku
os.makedirs("moje_staze", exist_ok=True)
np.savez(
    os.path.join("moje_staze", "podaci_staze.npz"), 
    sredina=np.array(sredina_tocke), 
    vanjske=np.array(vanjske_tocke), 
    unutarnje=np.array(unutarnje_tocke)
)

print("Gotovo! Binarna datoteka podaci_staze.npz je uspješno stvorena.")