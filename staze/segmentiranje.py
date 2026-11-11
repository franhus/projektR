import os
import json
import numpy as np
from shapely.geometry import LineString, Polygon, MultiLineString
from shapely.ops import split

SEGMENTI = 40
SIRINA_STAZE = 50.0


putanja = os.path.join("staze", "nacrtana_staza.txt")
with open(putanja, "r") as f:
    podaci = json.load(f)

vanjske = podaci.get("vanjske", [])
unutarnje = podaci.get("unutarnje", [])
linija = podaci.get("linija", []) # sredisnja linija

staza = Polygon(vanjske, holes=[unutarnje])
linija = LineString(linija)

granice_segmenata = []
duljina_linije = linija.length

# za svaki segment stvara granice
for i in range(SEGMENTI):
    udaljenost = (i / SEGMENTI) * duljina_linije
    tocka = linija.interpolate(udaljenost)
    tocka_ispred = linija.interpolate(min(udaljenost + 1.0, duljina_linije))
    
    dx = tocka_ispred.x - tocka.x
    dy = tocka_ispred.y - tocka.y
    duljina_vektora = np.hypot(dx, dy)
    okomica_dx = -(dy / duljina_vektora)
    okomica_dy = (dx / duljina_vektora)

    # stvara granicu dva segmenta (presjek sa granicama staze)
    granica = LineString([
        (tocka.x - okomica_dx * SIRINA_STAZE, tocka.y - okomica_dy * SIRINA_STAZE),
        (tocka.x + okomica_dx * SIRINA_STAZE, tocka.y + okomica_dy * SIRINA_STAZE)
    ])
    granice_segmenata.append(granica)

# podijela staza na segmente i sortiranje
granice_segmenata = MultiLineString(granice_segmenata)
segmenti_neporedani = split(staza, granice_segmenata)

segmenti = [segment for segment in segmenti_neporedani.geoms if segment.geom_type == 'Polygon']
segmenti.sort(key=lambda z: linija.project(z.centroid))

# koordinate svakog segmenta
koordinate_segmenata = []
for segment in segmenti:
    koordinate = list(segment.exterior.coords) # rubne tocka poligona segmenta
    koordinate_segmenata.append(koordinate)

# spremanje
podaci["segmenti"] = koordinate_segmenata
with open(putanja, "w") as f:
    json.dump(podaci, f, indent=4)

print(f"Broj izrezanih segmenata: {len(segmenti)}")