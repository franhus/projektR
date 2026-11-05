import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev
from shapely import LineString
import os
import json

# prostor za crtanje
plt.figure(figsize=(6, 6))
plt.title("Nacrtaj stazu")
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.grid(True)

# crtanje
ulaz = plt.ginput(n=-1, timeout=0) 
plt.close()

# bar 3 tocke
if len(ulaz) < 3:
    print("potrebno bar 3 tocke")
    exit()

# zatvaranje kruga
ulaz.append(ulaz[0])

# x i y koordinate
ulaz = np.array(ulaz)
x = ulaz[:, 0]
y = ulaz[:, 1]

# gladenje
tck, u = splprep([x, y], s=0, per=True)

puno_tocaka = np.linspace(0, 1, 500)        # broj tocaka za izgladivanje
x_linija, y_linija = splev(puno_tocaka, tck)    # x i y koordinate sredisnje linije staze

# pretvorba u matricu (300, 2)
linija = np.column_stack((x_linija, y_linija))
linija = LineString(linija)                 # sredisnja linija staze

# stvaranje rubova od sredisnje linije
staza = linija.buffer(3.0, quad_segs=16, resolution=16, join_style=1)
x_vanjski, y_vanjski = staza.exterior.xy    # x i y koordinate vanjske granice staze
x_unutarnji, y_unutarnji = staza.interiors[0].xy    # # x i y koordinate unutarnje granice staze

# crtanje staze
plt.figure(figsize=(6, 6))
# spline
plt.plot(x_linija, y_linija, "r--", linewidth=2, label='sredina')
# staza
plt.plot(x_vanjski, y_vanjski, 'b-', linewidth=2, label='vanjski rub')
plt.plot(x_unutarnji, y_unutarnji, 'b-', linewidth=2, label='unutarnji rub')
# tocke povezane crtama
plt.plot(x, y, 'go--', label='tocke povezane crtama')
plt.title("spline") 
plt.grid(True)
plt.axis('equal')
plt.show()


# za slanje u pygame
vanjske_tocke = staza.exterior.coords       # tocke vanjske granice
unutarnje_tocke = staza.interiors[0].coords  # # tocke unutarnje granice

# povećavanje i invertiranje y osi
def skaliraj(tocke):
    # 8 = 800 / 100, 8 i 800 se mijenjaju zajedno ako se mijenjaju
    return [(x * 8, 800 - (y * 8)) for x, y in tocke]

vanjske_tocke = skaliraj(list(staza.exterior.coords))
unutarnje_tocke = skaliraj(list(staza.interiors[0].coords))
tocke_sredine = skaliraj(list(zip(x_linija, y_linija)))     # spaja x i y koordinate
podaci = {
    "linija": tocke_sredine,
    "vanjske": vanjske_tocke,
    "unutarnje": unutarnje_tocke
}
# spremanje u .txt
os.makedirs("staze", exist_ok=True)
putanja = os.path.join("staze", "nacrtana_staza.txt")
with open(putanja, "w") as f:
    json.dump(podaci, f, indent=4)
