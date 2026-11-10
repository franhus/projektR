import math
from shapely.geometry import Point, Polygon

BRZINA = 3.0
VELICINA = 14

class Auto:
    def __init__(self, linija_staze, vanjske_tocke, unutarnje_tocke):
        self.linija = linija_staze # lista tocaka linije
        self.indeks = 1 # indeks sljedece tocke u listi
        self.brzina = BRZINA
        self.velicina = VELICINA
        self.x = float(self.linija[0][0])
        self.y = float(self.linija[0][1])
        self.sudar = False # True ako izade izvan staze (sudari se sa nekom od granica)
        self.granice = Polygon(vanjske_tocke, holes=[unutarnje_tocke])

    def pozicija(self):
        return (self.x, self.y)

    def unutar_staze(self):
        # materijalna tocka, inace makni #
        auto_hitbox = Point(self.x, self.y)#.buffer(self.velicina / 4)
        return self.granice.contains(auto_hitbox)
    
    def pomakni(self):
        # broj px za prijelaz u frameu
        preostalo = self.brzina

        while preostalo > 0:
            # koordinate sljedece tocke
            sljedeca_x = self.linija[self.indeks][0]
            sljedeca_y = self.linija[self.indeks][1]

            # udaljenost do sljedece tocke
            dx = sljedeca_x - self.x
            dy = sljedeca_y - self.y
            udaljenost = math.hypot(dx, dy)

            if udaljenost <= preostalo:
                self.x = float(sljedeca_x)
                self.y = float(sljedeca_y)
                preostalo -= udaljenost
                
                self.indeks += 1
                if self.indeks >= len(self.linija):
                    preostalo = 0
            else:
                # normalizacija vektora
                self.x += (dx / udaljenost) * preostalo
                self.y += (dy / udaljenost) * preostalo
                preostalo = 0
            
            if not self.unutar_staze():
                self.sudar = True
                break