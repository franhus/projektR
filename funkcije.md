numpy as np:
    np.array()
    
    np.linespace(start, end, num) -> num tocaka izmedu start i end 
    
    np.sin i np.cos
    
    np.column_stack ili np.vstack
    
    np.interp(x, xp, yp) -> vraca koordinate tocke x u odnosu na tocke s xp (lista x koordinata) i yp (lista y koordinata)


scipy:
    // sluzi za spremanje podataka umjesto matrice kad je puno nula
    from scipy.sparse import csr_array:
        csr_array((vrijednost, koordinate), oblik_matrice)

    // sluzi za nalazenje vrijednosti na krivulji izmedu dvije tocke
    from scipy.interpolation import CubicSpline
        interpolate = CubicSpline(x, y) // x, y su liste
        interpolate(xn) // = yn

    tck, u = splprep([x, y], s=0, per=True) -> x, y je lista koordinata staze, vraca tck koji proslijedim u splev

    x, y = splev(tocke, tck) vraca nove koordinate (puno njih u glatkoj liniji) na temelju tck, tocke je koliko su tocke guste (linespace)

matplotlib:
    plot(x, y, "tip") -> printa liste tocaka sa [x,y] u obliku tipa
        "o" je kruzic, inace linija
        "-" nakon tip je za krivulju, inace pravac
    fill between(x, y1, y2) -> za tocke u x (x koordinate) popunjuje 
    
    prostor izmedu y1 i y2 tocaka
    
    plt.figure(figsize=(a,b)) -> kanvas velicine a x b
    
    plt. ginput(n=-1, timeout=0) -> crtanje staze

    plt.axis("equal") -> osi X:Y = 1:1

shapely:

cma: