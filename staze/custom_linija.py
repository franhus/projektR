import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev
import os
import json

BROJ_TOCAKA = 500

# dohvat granica staze
putanja = os.path.join("staze", "nacrtana_staza.txt")
with open(putanja, "r") as f:
    podaci = json.load(f)
vanjske = np.array(podaci["vanjske"])
unutarnje = np.array(podaci["unutarnje"])
start = ((vanjske[0][0] + unutarnje[0][0]) /2, (vanjske[0][1] + unutarnje[0][1]) / 2)

# crtanje staze
plt.figure(figsize=(8, 8))
plt.title("Nacrtaj liniju")
plt.plot(vanjske[:, 0], vanjske[:, 1], 'b-', linewidth=2, label='vanjski rub')
plt.plot(unutarnje[:, 0], unutarnje[:, 1], 'b-', linewidth=2, label='unutarnji rub')
# crtanje startne linije (CRNA CRTA)
plt.plot([vanjske[0][0], unutarnje[0][0]], [vanjske[0][1], unutarnje[0][1]], 'k-', linewidth=3, label='start/cilj')
# crtanje prve tocke na sredini (start)
plt.plot(start[0], start[1], 'go', markersize=8, label='automatski start')

# invertiranje osi matplotlib->pygame
plt.gca().invert_yaxis()
plt.axis('equal')
plt.grid(True)

# crtanje (ceka klikove dok korisnik ne pritisne Enter ili srednju tipku)
ulaz = plt.ginput(n=-1, timeout=0) 
plt.close()
# dodavanje startne tocke
ulaz = [start] + ulaz

# bar 3 tocke
if len(ulaz) < 3:
    print("potrebno bar 3 tocke")
    exit()

# zatvaranje kruga putanje
ulaz.append(ulaz[0])

# x i y koordinate tvog novog unosa
ulaz = np.array(ulaz)
x = ulaz[:, 0]
y = ulaz[:, 1]

# gladenje tocaka
tck, u = splprep([x, y], s=0, per=True)

puno_tocaka = np.linspace(0, 1, BROJ_TOCAKA) # broj tocaka za izgladivanje
x_linija, y_linija = splev(puno_tocaka, tck) # x i y koordinate nove linije

# crtanje staze sa custom linijom
plt.figure(figsize=(8, 8))
# staza
plt.plot(vanjske[:, 0], vanjske[:, 1], 'b-', linewidth=2, label='vanjski rub')
plt.plot(unutarnje[:, 0], unutarnje[:, 1], 'b-', linewidth=2, label='unutarnji rub')
plt.plot([vanjske[0][0], unutarnje[0][0]], [vanjske[0][1], unutarnje[0][1]], 'k-', linewidth=3, label='start/cilj')
plt.plot(start[0], start[1], 'go', markersize=8, label='start')
# linija
plt.plot(x_linija, y_linija, "r--", linewidth=2, label='linija')
# tocke linije
plt.plot(x, y, 'go--', label='kliknute tocke')

plt.title("Custom putanja") 
plt.gca().invert_yaxis()
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()

# spremanje
nova_linija = np.column_stack((x_linija, y_linija)).tolist()
podaci["linija"] = nova_linija
with open(putanja, "w") as f:
    json.dump(podaci, f, indent=4)
