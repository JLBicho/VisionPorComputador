import numpy as np


class detectarExpresiones():

    def __init__(self, detector, marcador, imagenNeutra=None, imagen=None):
        self.detector = detector
        self.marcador = marcador
        self.imagenNeutra = imagenNeutra
        self.imagen = imagen
        if imagenNeutra is not None:
            self.__calcularPuntosNeutra()
        if imagen is not None:
            self.__calcularPuntos()

# Modifica la imagen analizable y recalcula los puntos característicos
    def setImagen(self, imagen):
        self.imagen = imagen
        self.__calcularPuntos()

# Modifica la imagen neutra y recalcula los puntos característicos
    def setImagenNeutra(self, imagen):
        self.imagenNeutra = imagen
        self.__calcularPuntos()

# Crea vectores con los puntos característicos de la imágen neutra
    def __calcularPuntosNeutra(self):
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
        self.__puntosAUsNeutra()

# Crea vectores con los puntos característicos de la imágen analizable
    def __calcularPuntos(self):
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
        self.__puntosAUs()

# TODO
# Crea vectores con los puntos de los action units definidos en
# el archivo de drive para la imagen que se analizará
    def __puntosAUs(self):
        # Calculadlos a partir de la variable self.puntos
        self.puntosBR = np.zeros((1, 3, 2), dtype='float32')
        self.puntosBL = np.zeros((1, 3, 2), dtype='float32')
        self.puntosER = np.zeros((1, 4, 2), dtype='float32')
        self.puntosEL = np.zeros((1, 4, 2), dtype='float32')
        self.puntosMR = np.zeros((1, 3, 2), dtype='float32')
        self.puntosML = np.zeros((1, 3, 2), dtype='float32')
        self.puntosMM = np.zeros((1, 2, 2), dtype='float32')
        self.__calcularDistancias()

# TODO
# Crea vectores con los puntos de los action units definidos en
# el archivo de drive para la imagen neutra
    def __puntosAUsNeutra(self):
        self.puntosNBR = np.zeros((1, 3, 2), dtype='float32')
        self.puntosNBL = np.zeros((1, 3, 2), dtype='float32')
        self.puntosNER = np.zeros((1, 4, 2), dtype='float32')
        self.puntosNEL = np.zeros((1, 4, 2), dtype='float32')
        self.puntosNMR = np.zeros((1, 3, 2), dtype='float32')
        self.puntosNML = np.zeros((1, 3, 2), dtype='float32')
        self.puntosNMM = np.zeros((1, 2, 2), dtype='float32')

# TODO: Para calcular distancia entre puntos usad librerías
# Calcula las distancias características de la imágen analizable
    def __calcularDistancias(self):
        # Completar con el resto de distancias necesarias
        # Para el resto de distancias seguid el mismo formato de nombre
        # dist + Izquierda_Derecha (parte derecha de la cara_parte izquierda)
        # si estan en el mismo lado arriba_abajo
        self.distER1_EL1 = None

# TODO
# Calcula las distancias características de la imágen neutra
    def __calcularDistanciasNeutra(self):
        self.distNER1_NEL1 = None

# TODO
# Escala la distancia entre ER1 y EL1 a 100 para ambas imagenes y el
# resto de distancias en la misma escala
    def __normalizarDist(self):
        pass

# TODO
# Genera el vector con los AUs que se cumplen con un valor de 0 a 1 en cada uno
    def __comprobarAUs(self):
        self.actionUnits = np.zeros(46)

# TODO: Definir funciones para cada action unit que devuelva un valor de 0 a 1
# en funcion del grado de cumplimiento de las condiciones impuestas
