numpy as np:
    np.array()

scipy:
    // sluzi za spremanje podataka umjesto matrice kad je puno nula
    from scipy.sparse import csr_array:
        csr_array((vrijednost, koordinate), oblik_matrice)

    // sluzi za nalazenje vrijednosti na krivulji izmedu dvije tocke
    from scipy.interpolation import CubicSpline
        interpolate = CubicSpline(x, y) // x, y su liste
        interpolate(xn) // = yn

matplotlib:

shapely:

cma: