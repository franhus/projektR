import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev

# 1. Priprema prozora za crtanje
plt.figure(figsize=(6, 6))
plt.title("Klikni mišem po ekranu da nacrtaš stazu!\n(Pritisni ENTER kad si gotov)")
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.grid(True)

# 2. Crtanje mišem
ulaz = plt.ginput(n=-1, timeout=0) 
plt.close()

# Sigurnosna provjera: moraš kliknuti barem 3 točke da bi Spline radio
if len(ulaz) < 3:
    print("Moraš kliknuti barem 3 točke!")
    exit()

# 3. Zatvaramo krug (dodajemo prvu točku na kraj liste)
ulaz.append(ulaz[0])

# 4. Pretvaramo u NumPy polje i odvajamo X i Y koordinate
ulaz = np.array(ulaz)
x = ulaz[:, 0]
y = ulaz[:, 1]

# 5. GLAĐENJE POMOĆU SPLINE-A
# splprep računa krivulju, a per=True mu kaže da je to zatvoreni krug
tck, u = splprep([x, y], s=0, per=True)

# Generiramo 300 sitnih, savršeno glatkih točaka duž te putanje
puno_tocaka = np.linspace(0, 1, 300)
x_novi, y_novi = splev(puno_tocaka, tck)

# Konačna glatka staza posložena u matricu oblika (300, 2)
linija = np.column_stack((x_novi, y_novi))

# 6. Prikaz rezultata
plt.figure(figsize=(6, 6))
# Crtamo glatku plavu liniju staze
plt.plot(x_novi, y_novi, 'b-', linewidth=3, label='Glatka staza (Spline)')
# Crtamo tvoje originalne klikove da vidiš razliku
plt.plot(x, y, 'ro--', label='Grubi klikovi')
plt.title("Glatka staza")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()