import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev
from shapely import LineString

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

puno_tocaka = np.linspace(0, 1, 300)
x_novi, y_novi = splev(puno_tocaka, tck)

# pretvorba u matricu (300, 2)
linija = np.column_stack((x_novi, y_novi))
linija = LineString(linija)

# stvaranje rubova od sredisnje linije
staza = linija.buffer(3.0, quad_segs=16, resolution=16, join_style=1)
x_vanjski, y_vanjski = staza.exterior.xy
x_unutarnji, y_unutarnji = staza.interiors[0].xy


plt.figure(figsize=(6, 6))
# spline
plt.plot(x_novi, y_novi, "r--", linewidth=2, label='sredina')
# staza
plt.plot(x_vanjski, y_vanjski, 'b-', linewidth=2, label='vanjski rub')
plt.plot(x_unutarnji, y_unutarnji, 'b-', linewidth=2, label='unutarnji rub')
# tocke povezane crtama
plt.plot(x, y, 'go--', label='tocke povezane crtama')
plt.title("spline") 
plt.grid(True)
plt.axis('equal')
plt.show()