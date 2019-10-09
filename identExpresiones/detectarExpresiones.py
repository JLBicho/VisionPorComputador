class detectarExpresiones():
    def __init__(self, detector, marcador, imagenNeutra=None, imagen=None):
        self.detector = detector
        self.marcador = marcador
        self.imagenNeutra = imagenNeutra
        self.imagen = imagen

    def calcularPuntosNeutra(self):
        caras = self.detector.detectMultiScale(self.imagenNeutra)
        retval, puntos = self.marcador.fit(self.imagenNeutra, caras)
        self.puntosNeutra = puntos[0]
        self.puntosCabezaNeutra = self.puntosNeutra[0:1, 0:17, 0:2]
        self.puntosCejaIzqNeutra = self.puntosNeutra[0:1, 17:22, 0:2]
        self.puntosCejaDerNeutra = self.puntosNeutra[0:1, 22:27, 0:2]
        self.puntosTabiqueNeutra = self.puntosNeutra[0:1, 27:31, 0:2]
        self.puntosNarizNeutra = self.puntosNeutra[0:1, 31:36, 0:2]
        self.puntosOjoIzqNeutra = self.puntosNeutra[0:1, 36:42, 0:2]
        self.puntosOjoDerNeutra = self.puntosNeutra[0:1, 42:48, 0:2]
        self.puntosLabiosNeutra = self.puntosNeutra[0:1, 48:60, 0:2]
        self.puntosBocaNeutra = self.puntosNeutra[0:1, 60:68, 0:2]

    def calcularPuntos(self):
        caras = self.detector.detectMultiScale(self.imagen)
        retval, puntos = self.marcador.fit(self.imagen, caras)
        self.puntos = puntos[0]
        self.puntosCabeza = self.puntos[0:1, 0:17, 0:2]
        self.puntosCejaIzq = self.puntos[0:1, 17:22, 0:2]
        self.puntosCejaDer = self.puntos[0:1, 22:27, 0:2]
        self.puntosTabique = self.puntos[0:1, 27:31, 0:2]
        self.puntosNariz = self.puntos[0:1, 31:36, 0:2]
        self.puntosOjoIzq = self.puntos[0:1, 36:42, 0:2]
        self.puntosOjoDer = self.puntos[0:1, 42:48, 0:2]
        self.puntosLabios = self.puntos[0:1, 48:60, 0:2]
        self.puntosBoca = self.puntos[0:1, 60:68, 0:2]
