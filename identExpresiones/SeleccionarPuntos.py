
def selPuntosCabeza(puntos):
    return puntos[0:1, 0:17, 0:2]


def selPuntosCejaIzq(puntos):
    return puntos[0:1, 17:22, 0:2]


def selPuntosCejaDer(puntos):
    return puntos[0:1, 22:27, 0:2]


def selPuntosTabique(puntos):
    return puntos[0:1, 27:31, 0:2]


def selPuntosNariz(puntos):
    return puntos[0:1, 31:36, 0:2]


def selPuntosOjoIzq(puntos):
    return puntos[0:1, 36:42, 0:2]


def selPuntosOjoDer(puntos):
    return puntos[0:1, 42:48, 0:2]


def selPuntosLabios(puntos):
    return puntos[0:1, 48:60, 0:2]


def selPuntosBoca(puntos):
    return puntos[0:1, 60:68, 0:2]
