import numpy as np
import math


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
        self.__calcularPuntosNeutra()

# Crea vectores con los puntos característicos de la imágen neutra
    def __calcularPuntosNeutra(self):
        caras = self.detector.detectMultiScale(self.imagenNeutra)
        retval, puntos = self.marcador.fit(self.imagenNeutra, caras)
        self.puntosNeutra = puntos[0]
        self.puntosCabezaNeutra = self.puntosNeutra[0:1, 0:17, 0:2]
        self.puntosCejaDerNeutra = self.puntosNeutra[0:1, 17:22, 0:2]
        self.puntosCejaIzqNeutra = self.puntosNeutra[0:1, 22:27, 0:2]
        self.puntosTabiqueNeutra = self.puntosNeutra[0:1, 27:31, 0:2]
        self.puntosNarizNeutra = self.puntosNeutra[0:1, 31:36, 0:2]
        self.puntosOjoDerNeutra = self.puntosNeutra[0:1, 36:42, 0:2]
        self.puntosOjoIzqNeutra = self.puntosNeutra[0:1, 42:48, 0:2]
        self.puntosLabiosNeutra = self.puntosNeutra[0:1, 48:60, 0:2]
        self.puntosBocaNeutra = self.puntosNeutra[0:1, 60:68, 0:2]
        self.__puntosAUsNeutra()

# Crea vectores con los puntos característicos de la imágen analizable
    def __calcularPuntos(self):
        caras = self.detector.detectMultiScale(self.imagen)
        retval, puntos = self.marcador.fit(self.imagen, caras)
        self.puntos = puntos[0]
        self.puntosCabeza = self.puntos[0:1, 0:17, 0:2]
        self.puntosCejaDer = self.puntos[0:1, 17:22, 0:2]
        self.puntosCejaIzq = self.puntos[0:1, 22:27, 0:2]
        self.puntosTabique = self.puntos[0:1, 27:31, 0:2]
        self.puntosNariz = self.puntos[0:1, 31:36, 0:2]
        self.puntosOjoDer = self.puntos[0:1, 36:42, 0:2]
        self.puntosOjoIzq = self.puntos[0:1, 42:48, 0:2]
        self.puntosLabios = self.puntos[0:1, 48:60, 0:2]
        self.puntosBoca = self.puntos[0:1, 60:68, 0:2]
        self.__puntosAUs()

# TODO
# Crea vectores con los puntos de los action units definidos en
# el archivo de drive para la imagen que se analizará
    def __puntosAUs(self):
        # Calculadlos a partir de la variable self.puntos
        self.puntosBR = np.zeros((1, 3, 2), dtype='float32')
        self.puntosBR[0:1, 0, 0:2] = self.puntosCejaDer[0:1, 0, 0:2]
        self.puntosBR[0:1, 1, 0:2] = self.puntosCejaDer[0:1, 2, 0:2]
        self.puntosBR[0:1, 2, 0:2] = self.puntosCejaDer[0:1, 4, 0:2]
        self.puntosBL = np.zeros((1, 3, 2), dtype='float32')
        self.puntosBL[0:1, 0, 0:2] = self.puntosCejaIzq[0:1, 4, 0:2]
        self.puntosBL[0:1, 1, 0:2] = self.puntosCejaIzq[0:1, 2, 0:2]
        self.puntosBL[0:1, 2, 0:2] = self.puntosCejaIzq[0:1, 0, 0:2]
        self.puntosER = np.zeros((1, 4, 2), dtype='float32')
        self.puntosER[0:1, 0, 0:2] = self.puntosOjoDer[0:1, 3, 0:2]
        self.puntosER[0:1, 1, 0:2] = self.puntosOjoDer[0:1, 4, 0:2]
        self.puntosER[0:1, 2, 0:2] = self.puntosOjoDer[0:1, 2, 0:2]
        self.puntosER[0:1, 3, 0:2] = self.puntosOjoDer[0:1, 0, 0:2]
        self.puntosEL = np.zeros((1, 4, 2), dtype='float32')
        self.puntosEL[0:1, 0, 0:2] = self.puntosOjoIzq[0:1, 0, 0:2]
        self.puntosEL[0:1, 1, 0:2] = self.puntosOjoIzq[0:1, 5, 0:2]
        self.puntosEL[0:1, 2, 0:2] = self.puntosOjoIzq[0:1, 1, 0:2]
        self.puntosEL[0:1, 3, 0:2] = self.puntosOjoIzq[0:1, 3, 0:2]
        self.puntosMR = np.zeros((1, 3, 2), dtype='float32')
        self.puntosMR[0:1, 0, 0:2] = self.puntosLabios[0:1, 0, 0:2]
        self.puntosMR[0:1, 1, 0:2] = self.puntosLabios[0:1, 10, 0:2]
        self.puntosMR[0:1, 2, 0:2] = self.puntosLabios[0:1, 2, 0:2]
        self.puntosML = np.zeros((1, 3, 2), dtype='float32')
        self.puntosML[0:1, 0, 0:2] = self.puntosLabios[0:1, 6, 0:2]
        self.puntosML[0:1, 1, 0:2] = self.puntosLabios[0:1, 8, 0:2]
        self.puntosML[0:1, 2, 0:2] = self.puntosLabios[0:1, 4, 0:2]
        self.puntosMM = np.zeros((1, 2, 2), dtype='float32')
        self.puntosMM[0:1, 0, 0:2] = self.puntosBoca[0:1, 6, 0:2]
        self.puntosMM[0:1, 1, 0:2] = self.puntosBoca[0:1, 2, 0:2]
        self.__calcularDistancias()

# TODO
# Crea vectores con los puntos de los action units definidos en
# el archivo de drive para la imagen neutra
    def __puntosAUsNeutra(self):
        self.puntosNBR = np.zeros((1, 3, 2), dtype='float32')
        self.puntosNBR[0:1, 0, 0:2] = self.puntosCejaDerNeutra[0:1, 0, 0:2]
        self.puntosNBR[0:1, 1, 0:2] = self.puntosCejaDerNeutra[0:1, 2, 0:2]
        self.puntosNBR[0:1, 2, 0:2] = self.puntosCejaDerNeutra[0:1, 4, 0:2]
        self.puntosNBL = np.zeros((1, 3, 2), dtype='float32')
        self.puntosNBL[0:1, 0, 0:2] = self.puntosCejaIzqNeutra[0:1, 4, 0:2]
        self.puntosNBL[0:1, 1, 0:2] = self.puntosCejaIzqNeutra[0:1, 2, 0:2]
        self.puntosNBL[0:1, 2, 0:2] = self.puntosCejaIzqNeutra[0:1, 0, 0:2]
        self.puntosNER = np.zeros((1, 4, 2), dtype='float32')
        self.puntosNER[0:1, 0, 0:2] = self.puntosOjoDerNeutra[0:1, 3, 0:2]
        self.puntosNER[0:1, 1, 0:2] = self.puntosOjoDerNeutra[0:1, 4, 0:2]
        self.puntosNER[0:1, 2, 0:2] = self.puntosOjoDerNeutra[0:1, 2, 0:2]
        self.puntosNER[0:1, 3, 0:2] = self.puntosOjoDerNeutra[0:1, 0, 0:2]
        self.puntosNEL = np.zeros((1, 4, 2), dtype='float32')
        self.puntosNEL[0:1, 0, 0:2] = self.puntosOjoIzqNeutra[0:1, 0, 0:2]
        self.puntosNEL[0:1, 1, 0:2] = self.puntosOjoIzqNeutra[0:1, 5, 0:2]
        self.puntosNEL[0:1, 2, 0:2] = self.puntosOjoIzqNeutra[0:1, 1, 0:2]
        self.puntosNEL[0:1, 3, 0:2] = self.puntosOjoIzqNeutra[0:1, 3, 0:2]
        self.puntosNMR = np.zeros((1, 3, 2), dtype='float32')
        self.puntosNMR[0:1, 0, 0:2] = self.puntosLabiosNeutra[0:1, 0, 0:2]
        self.puntosNMR[0:1, 1, 0:2] = self.puntosLabiosNeutra[0:1, 10, 0:2]
        self.puntosNMR[0:1, 2, 0:2] = self.puntosLabiosNeutra[0:1, 2, 0:2]
        self.puntosNML = np.zeros((1, 3, 2), dtype='float32')
        self.puntosNML[0:1, 0, 0:2] = self.puntosLabiosNeutra[0:1, 6, 0:2]
        self.puntosNML[0:1, 1, 0:2] = self.puntosLabiosNeutra[0:1, 8, 0:2]
        self.puntosNML[0:1, 2, 0:2] = self.puntosLabiosNeutra[0:1, 4, 0:2]
        self.puntosNMM = np.zeros((1, 2, 2), dtype='float32')
        self.puntosNMM[0:1, 0, 0:2] = self.puntosBocaNeutra[0:1, 6, 0:2]
        self.puntosNMM[0:1, 1, 0:2] = self.puntosBocaNeutra[0:1, 2, 0:2]
        self.__calcularDistanciasNeutra()

# Para calcular las distancias entre dos puntos
    def __dist(self, x1, x2):
        distancia = math.sqrt((x2[0:1, 0] - x1[0:1, 0])**2
                              + (x2[0:1, 1] - x1[0:1, 1])**2)
        return distancia

# Para calcular las distancias VERTICALES entre dos puntos.
# x1 (arriba) - x2 (abajo)
    def __distVertical(self, x1, x2):
        distancia = x1[0:1, 1] - x2[0:1, 1]
        return distancia

# Para calcular las distancias HORIZONTALES entre dos puntos.
# x1 (izquierda) - x2 (derecha)
    def __distHorizontal(self, x1, x2):
        distancia = x1[0:1, 0] - x2[0:1, 0]
        return distancia        

# TODO: Para calcular distancia entre puntos usad librerías
# Calcula las distancias características de la imágen analizable
    def __calcularDistancias(self):
        # Completar con el resto de distancias necesarias
        # Para el resto de distancias seguid el mismo formato de nombre
        # dist + Izquierda_Derecha (parte derecha de la cara_parte izquierda)
        # si estan en el mismo lado arriba_abajo

        self.distER1_EL1 = self.__dist(self.puntosER[0:1, 0, 0:2],
                                       self.puntosEL[0:1, 0, 0:2])

        # AU1 (estan en AU4)
        self.distvBR3_ER1 = self.__distVertical(self.puntosBR[0:1, 2, 0:2],
                                                self.puntosER[0:1, 0, 0:2])
        self.distvBL3_EL1 = self.__distVertical(self.puntosBL[0:1, 2, 0:2],
                                                self.puntosEL[0:1, 0, 0:2])
        # AU2
        self.distvBR1_ER4 = self.__distVertical(self.puntosBR[0:1, 0, 0:2],
                                                self.puntosER[0:1, 3, 0:2])
        self.distvBL1_EL4 = self.__distVertical(self.puntosBL[0:1, 0, 0:2],
                                                self.puntosEL[0:1, 3, 0:2])
        self.distvBR2_ER2 = self.__distVertical(self.puntosBR[0:1, 1, 0:2],
                                                self.puntosER[0:1, 1, 0:2])
        self.distvBL2_EL2 = self.__distVertical(self.puntosBL[0:1, 1, 0:2],
                                                self.puntosEL[0:1, 1, 0:2])

        # AU4
        self.distvBR1_ER1 = self.__distVertical(self.puntosBR[0:1, 0, 0:2],
                                                self.puntosER[0:1, 0, 0:2])
        self.distvBL1_EL1 = self.__distVertical(self.puntosBL[0:1, 0, 0:2],
                                                self.puntosEL[0:1, 0, 0:2])
        self.distBR2_ER1 = self.__dist(self.puntosBR[0:1, 1, 0:2],
                                       self.puntosER[0:1, 0, 0:2])
        self.distBL2_EL1 = self.__dist(self.puntosBL[0:1, 1, 0:2],
                                       self.puntosEL[0:1, 0, 0:2])
        self.distBR3_ER1 = self.__dist(self.puntosBR[0:1, 2, 0:2],
                                       self.puntosER[0:1, 0, 0:2])
        self.distBL3_EL1 = self.__dist(self.puntosBL[0:1, 2, 0:2],
                                       self.puntosEL[0:1, 0, 0:2])

        # AU6
        self.distER2_ER3 = self.__dist(self.puntosER[0:1, 1, 0:2],
                                       self.puntosER[0:1, 2, 0:2])
        self.distEL2_EL3 = self.__dist(self.puntosEL[0:1, 1, 0:2],
                                       self.puntosEL[0:1, 2, 0:2])
        self.distvER1_ER3 = self.__distVertical(self.puntosER[0:1, 0, 0:2],
                                                self.puntosER[0:1, 2, 0:2])
        self.distvEL1_EL3 = self.__distVertical(self.puntosEL[0:1, 0, 0:2],
                                                self.puntosEL[0:1, 2, 0:2])

        # AU10
        self.distMR2_ER1 = self.__dist(self.puntosMR[0:1, 3, 0:2],
                                      self.puntosER[0:1, 0, 0:2])
        self.distML2_EL1 = self.__dist(self.puntosML[0:1, 3, 0:2],
                                      self.puntosEL[0:1, 0, 0:2])
        # AU12
        self.distMR1_ER1 = self.__dist(self.puntosMR[0:1, 0, 0:2],
                                      self.puntosER[0:1, 0, 0:2])
        self.distML1_EL1 = self.__dist(self.puntosML[0:1, 0, 0:2],
                                      self.puntosEL[0:1, 0, 0:2])
        # AU12 AU14
        self.distMM1_MM2 = self.__dist(self.puntosMM[0:1, 0, 0:2],
                                      self.puntoMM[0:1, 1, 0:2])
        # AU14
        self.disthMR1_ER1 = self.__distHorizontal(self.puntosMR[0:1, 0, 0:2],
                                                  self.puntosER[0:1, 0, 0:2])
        self.disthML1_EL1 = self.__distHorizontal(self.puntosML[0:1, 0, 0:2],
                                                  self.puntosEL[0:1, 0, 0:2])
# TODO
# Calcula las distancias características de la imágen neutra
    def __calcularDistanciasNeutra(self):
        self.distNER1_NEL1 = self.__dist(self.puntosNER[0:1, 0, 0:2],
                                         self.puntosNEL[0:1, 0, 0:2])

        # AU1
        self.distvNBR3_NER1 = self.__distVertical(self.puntosNBR[0:1, 2, 0:2],
                                                  self.puntosNER[0:1, 0, 0:2])
        self.distvNBL3_NEL1 = self.__distVertical(self.puntosNBL[0:1, 2, 0:2],
                                                  self.puntosNEL[0:1, 0, 0:2])

        # AU2
        self.distvNBR1_NER4 = self.__distVertical(self.puntosNBR[0:1, 0, 0:2],
                                                  self.puntosNER[0:1, 3, 0:2])
        self.distvNBL1_NEL4 = self.__distVertical(self.puntosNBL[0:1, 0, 0:2],
                                                  self.puntosNEL[0:1, 3, 0:2])
        self.distvNBR2_NER2 = self.__distVertical(self.puntosNBR[0:1, 1, 0:2],
                                                  self.puntosNER[0:1, 1, 0:2])
        self.distvNBL2_NEL2 = self.__distVertical(self.puntosNBL[0:1, 1, 0:2],
                                                  self.puntosNEL[0:1, 1, 0:2])

        # AU4
        self.distvNBR1_NER1 = self.__distVertical(self.puntosNBR[0:1, 0, 0:2],
                                                  self.puntosNER[0:1, 0, 0:2])
        self.distvNBL1_NEL1 = self.__distVertical(self.puntosNBL[0:1, 0, 0:2],
                                                  self.puntosNEL[0:1, 0, 0:2])
        self.distNBR2_NER1 = self.__dist(self.puntosNBR[0:1, 1, 0:2],
                                         self.puntosNER[0:1, 0, 0:2])
        self.distNBL2_NEL1 = self.__dist(self.puntosNBL[0:1, 1, 0:2],
                                         self.puntosNEL[0:1, 0, 0:2])
        self.distNBR3_NER1 = self.__dist(self.puntosNBR[0:1, 2, 0:2],
                                         self.puntosNER[0:1, 0, 0:2])
        self.distNBL3_NEL1 = self.__dist(self.puntosNBL[0:1, 2, 0:2],
                                         self.puntosNEL[0:1, 0, 0:2])

        # AU6
        self.distNER2_NER3 = self.__dist(self.puntosNER[0:1, 1, 0:2],
                                         self.puntosNER[0:1, 2, 0:2])
        self.distNEL2_NEL3 = self.__dist(self.puntosNEL[0:1, 1, 0:2],
                                         self.puntosNEL[0:1, 2, 0:2])
        self.distvNER1_NER3 = self.__distVertical(self.puntosNER[0:1, 0, 0:2],
                                                  self.puntosNER[0:1, 2, 0:2])
        self.distvNEL1_NEL3 = self.__distVertical(self.puntosNEL[0:1, 0, 0:2],
                                                  self.puntosNEL[0:1, 2, 0:2])

        # AU10
        self.distNMR2_NER1 = self.__dist(self.puntosNMR[0:1, 3, 0:2],
                                      self.puntosNER[0:1, 0, 0:2])
        self.distNML2_NEL1 = self.__dist(self.puntosNML[0:1, 3, 0:2],
                                      self.puntosNEL[0:1, 0, 0:2])
        # AU12
        self.distNMR1_NER1 = self.__dist(self.puntosNMR[0:1, 0, 0:2],
                                      self.puntosNER[0:1, 0, 0:2])
        self.distNML1_NEL1 = self.__dist(self.puntosNML[0:1, 0, 0:2],
                                      self.puntosNEL[0:1, 0, 0:2])
        # AU12 AU14
        self.distNMM1_NMM2 = self.__dist(self.puntosNMM[0:1, 0, 0:2],
                                      self.puntoNMM[0:1, 1, 0:2])
        # AU14
        self.disthNMR1_NER1 = self.__distHorizontal(self.puntosNMR[0:1, 0, 0:2],
                                                  self.puntosNER[0:1, 0, 0:2])
        self.disthNML1_NEL1 = self.__distHorizontal(self.puntosNML[0:1, 0, 0:2],
                                                  self.puntosNEL[0:1, 0, 0:2])

# TODO
# Escala la distancia entre ER1 y EL1 a 100 para ambas imagenes y el
# resto de distancias en la misma escala
# Añadir aqui todas las demas distancias para normalizarlas
# Por ultimo, le damos a ER1_EL1 su nuevo valor de 100
    def __normalizarDist(self):
        # Imagen

        # # ejemplo:
        self.distER2_ER1 = self.distER2_ER1 * 100 / self.distER1_EL1

        # AU1
        self.distvBR3_ER1 = self.distvBR3_ER1 * 100 / self.distER1_EL1
        self.distvBL3_EL1 = self.distvBL3_EL1 * 100 / self.distER1_EL1

        # AU2
        self.distvBR1_ER4 = self.distvBR1_ER4 * 100 / self.distER1_EL1
        self.distvBL1_EL4 = self.distvBL1_EL4 * 100 / self.distER1_EL1
        self.distvBR2_ER2 = self.distvBR2_ER2 * 100 / self.distER1_EL1
        self.distvBL2_EL2 = self.distvBL2_EL2 * 100 / self.distER1_EL1

        # AU4
        self.distvBR1_ER1 = self.distvBR1_ER1 * 100 / self.distER1_EL1
        self.distvBL1_EL1 = self.distvBL1_EL1 * 100 / self.distER1_EL1
        self.distBR2_ER1 = self.distBR2_ER1 * 100 / self.distER1_EL1
        self.distBL2_EL1 = self.distBL2_EL1 * 100 / self.distER1_EL1
        self.distBR3_ER1 = self.distBR3_ER1 * 100 / self.distER1_EL1
        self.distBL3_EL1 = self.distBL3_EL1 * 100 / self.distER1_EL1

        # AU6
        self.distER2_ER3 = self.distER2_ER3 * 100 / self.distER1_EL1
        self.distEL2_EL3 = self.distEL2_EL3 * 100 / self.distER1_EL1
        self.distvER1_ER3 = self.distvER1_ER3 * 100 / self.distER1_EL1
        self.distvEL1_EL3 = self.distvEL1_EL3 * 100 / self.distER1_EL1

        self.distER1_EL1 = 100

        # AU10
        self.distMR2_ER1 = self.distMR2_ER1 * 100 / self.distNER1_NEL1
        self.distML2_EL1 = self.distML2_EL1 * 100 / self.distNER1_NEL1

        # AU12
        self.distMR1_ER1 = self.distMR1_ER1 * 100 / self.distNER1_NEL1
        self.distML1_EL1 = self.distML1_EL1 * 100 / self.distNER1_NEL1

        # AU12 AU14
        self.distMM1_MM2 = self.distMM1_MM2 * 100 / self.distNER1_NEL1

        # AU14
        self.disthMR1_ER1 = self.disthMR1_ER1 * 100 / self.distNER1_NEL1
        self.disthML1_EL1 = self.disthML1_EL1 * 100 / self.distNER1_NEL1

        # Imagen Neutra

        # # ejemplo:
        self.distNER2_NER1 = self.distNER2_NER1 * 100 / self.distNER1_NEL1

        # AU1
        self.distvNBR3_NER1 = self.distvNBR3_NER1 * 100 / self.distNER1_NEL1
        self.distvNBL3_NEL1 = self.distvNBL3_NEL1 * 100 / self.distNER1_NEL1

        # AU2
        self.distvNBR1_NER4 = self.distvNBR1_NER4 * 100 / self.distNER1_NEL1
        self.distvNsBL1_NEL4 = self.distvNBL1_NEL4 * 100 / self.distNER1_NEL1
        self.distvNBR2_NER2 = self.distvNBR2_NER2 * 100 / self.distNER1_NEL1
        self.distvNBL2_NEL2 = self.distvNBL2_NEL2 * 100 / self.distNER1_NEL1

        # AU4 + AU1
        self.distvNBR1_NER1 = self.distvNBR1_NER1 * 100 / self.distNER1_NEL1
        self.distvNBL1_NEL1 = self.distvNBL1_NEL1 * 100 / self.distNER1_NEL1
        self.distNBR2_NER1 = self.distNBR2_NER1 * 100 / self.distNER1_NEL1
        self.distNBL2_NEL1 = self.distNBL2_NEL1 * 100 / self.distNER1_NEL1
        self.distNBR3_NER1 = self.distNBR3_NER1 * 100 / self.distNER1_NEL1
        self.distNBL3_NEL1 = self.distNBL3_NEL1 * 100 / self.distNER1_NEL1

        # AU6
        self.distNER2_NER3 = self.distNER2_NER3 * 100 / self.distNER1_NEL1
        self.distNEL2_NEL3 = self.distNEL2_NEL3 * 100 / self.distNER1_NEL1
        self.distvNER1_NER3 = self.distvNER1_NER3 * 100 / self.distNER1_NEL1
        self.distvNEL1_NEL3 = self.distvNEL1_NEL3 * 100 / self.distNER1_NEL1

        self.distNER1_NEL1 = 100

        # AU10
        self.distNMR2_NER1 = self.distNMR2_NER1 * 100 / self.distNER1_NEL1
        self.distNML2_NEL1 = self.distNML2_NEL1 * 100 / self.distNER1_NEL1
        
        # AU12
        self.distNMR1_NER1 = self.distNMR1_NER1 * 100 / self.distNER1_NEL1
        self.distNML1_NEL1 = self.distNML1_NEL1 * 100 / self.distNER1_NEL1
        
        # AU14
        self.disthNMR1_NER1 = self.disthNMR1_NER1 * 100 / self.distNER1_NEL1
        self.disthNML1_NEL1 = self.disthNML1_NEL1 * 100 / self.distNER1_NEL1

# Genera el vector con los AUs que se cumplen con un valor de 0 a 1 para cada
# AU calculado y -1 en los AU no calculados
    def __comprobarAUs(self):
        self.actionUnits = np.zeros(46) - 1
        self.actionUnits[1] = self.__AU1()
        self.actionUnits[2] = self.__AU2()
        self.actionUnits[4] = self.__AU4()
        self.actionUnits[6] = self.__AU6()
        self.actionUnits[10] = self.__AU10()
        self.actionUnits[12] = self.__AU12()
        self.actionUnits[14] = self.__AU14()

# TODO: Completar funciones para cada action unit que devuelva un valor de
#       0 a 1 en funcion del grado de cumplimiento de las condiciones impuestas
    def __AU1(self):
        # Inner eyebrows raised
        compliance = None

        # Threshold = % del maximo para considerarse activo
        thr = 0.2

        # Max dist = dist entre puntos max para esa AU
        maxdist_B3 = 100

        # # Ceja derecha
        if self.distvBR3_ER1 - self.distvNBR3_NER1 > thr * maxdist_B3:
            compBR = (self.distvBR3_ER1 - self.distvNBR3_NER1)/maxdist_B3
        else:
            compBR = 0
        if compBR > 1:
            compBR = 1
        # # Ceja izquierda
        if self.distvBL3_EL1 - self.distvNBL3_NEL1 > thr * maxdist_B3:
            comBL = (self.distvBL3_EL1 - self.distvNBL3_NEL1)/maxdist_B3
        else:
            compBL = 0
        if compBL > 1:
            compBL = 1
        # # Resultado
        compliance = 0.5 * compBR + 0.5 * compBL
        return compliance

    def __AU2(self):
        # Outer eyebrows raised
        compliance = None

        # Threshold = % del maximo para considerarse activo
        thr = 0.2

        # Max dist = dist entre puntos max para esa AU
        maxdist_B1 = 100  # Punto mas exterior de la ceja
        maxdist_B2 = 100  # Punto central de la ceja

        # # Ceja derecha
        if self.distvBR1_ER4 - self.distvNBR1_NER4 > thr * maxdist_B1:
            compBR1 = (self.distvBR1_ER4 - self.distvNBR1_NER4)/maxdist_B1
        else:
            compBR1 = 0
        if compBR1 > 1:
            compBR1 = 1

        if self.distvBR2_ER2 - self.distvNBR2_NER2 > thr * maxdist_B2:
            compBR2 = (self.distvBR2_ER2 - self.distvNBR2_NER2)/maxdist_B2
        else:
            compBR2 = 0
        if compBR2 > 1:
            compBR2 = 1

        compBR = 0.5 * compBR1 + 0.5 * compBR2

        # # Ceja izquierda
        if self.distvBL1_EL4 - self.distvNBL1_NEL4 > thr * maxdist_B1:
            compBL1 = (self.distvBL1_EL4 - self.distvNBL1_NEL4)/maxdist_B1
        else:
            compBL1 = 0
        if compBL1 > 1:
            compBL1 = 1

        if self.distvBL2_EL2 - self.distvNBL2_NEL2 > thr * maxdist_B2:
            compBL2 = (self.distvBL2_EL2 - self.distvNBL2_NEL2)/maxdist_B2
        else:
            compBL2 = 0
        if compBL2 > 1:
            compBL2 = 1

        compBL = 0.5 * compBL1 + 0.5 * compBL2
        # # Resultado
        compliance = 0.5 * compBR + 0.5 * compBL
        return compliance

    def __AU4(self):
        compliance = None
        thr_B1 = None
        thr_B2 = None
        thr_B3 = None
        # Right
        if self.distvBR1_ER1 - self.distvNBR1_NER1 > 0.2 * thr_B1:
            compBR1 = (self.distvBR1_ER1 - self.distvNBR1_NER1) / thr_B1
        if self.distBR2_ER1 - self.distNBR2_NER1 > 0.2 * thr_B2:
            compBR2 = (self.distBR2_ER1 - self.distNBR2_NER1) / thr_B2
        if self.distBR3_ER1 - self.distNBR3_NER1 > 0.2 * thr_B3:
            compBR3 = (self.distBR3_ER1 - self.distNBR3_NER1) / thr_B3
        complianceR = 0.4 * compBR1 + 0.3 * compBR2 + 0.3 * compBR3
        # Left
        if self.distvBL1_EL1 - self.distvNBL1_NEL1 > 0.2 * thr_B1:
            compBR1 = (self.distvBL1_EL1 - self.distvNBL1_NEL1) / thr_B1
        if self.distBL2_EL1 - self.distNBL2_NEL1 > 0.2 * thr_B2:
            compBR2 = (self.distBL2_EL1 - self.distNBL2_NEL1) / thr_B2
        if self.distBL3_EL1 - self.distNBL3_NEL1 > 0.2 * thr_B3:
            compBR3 = (self.distBL3_EL1 - self.distNBL3_NEL1) / thr_B3
        complianceL = 0.4 * compBL1 + 0.3 * compBL2 + 0.3 * compBL3
        compliance = 0.5 * complianceR + 0.5 * complianceL
        return compliance

    def __AU6(self):
        compliance = None
        thr_E3 = None
        thr_E2_E3 = None
        # Right
        if self.distNER2_NER3 - self.distER2_ER3 > 0.2 * thr_E2_E3:
            compER2_ER3 = (self.distNER2_NER3 - self.distER2_ER3) / thr_E2_E3
        if self.distvNER1_NER3 - self.distvER1_ER3 > 0.2 * thr_E3:
            compER1_ER3 = (self.distvNER1_NER3 - self.distvER1_ER3) / thr_E3
        complianceR = 0.7 * compER2_ER3 + 0.3 * compER1_ER3
        # Left
        if self.distNEL2_NEL3 - self.distEL2_EL3 > 0.2 * thr_E2_E3:
            compEL2_EL3 = (self.distNEL2_NEL3 - self.distEL2_EL3) / thr_E2_E3
        if self.distvNEL1_NEL3 - self.distvEL1_EL3 > 0.2 * thr_E3:
            compEL1_EL3 = (self.distvNEL1_NEL3 - self.distvEL1_EL3) / thr_E3
        complianceL = 0.7 * compEL2_EL3 + 0.3 * compEL1_EL3
        compliance = 0.5 * complianceR + 0.5 * complianceL
        return compliance

    def __AU10(self):
        # mr2 up + bit out
        # ml2 up + bit out
        compliance = None
        AU10thres = None # tiene que ser negativo
        compMR2 = None
        compML2 = None

        # Right lip
        if self.distMR2_ER1 - self.distNMR2_NER1 < AU10thres:
            compMR2 = (self.distMR2_ER1 - self.distNMR2_ER1) / AU10thres
        # Left lip
        if self.distML2_EL1 - self.distNML2_NEL1 < AU10thres:
            compML2 = (self.distML2_EL1 - self.distNML2_NEL1) / AU10thres

        compliance = 0.5 * compML2 + 0.5 * compMR2
        if compliance > 1:
            compliance = 1
        return compliance

    def __AU12(self):
        # mr1 up + bit out
        # ml1 up + bit out
        # mouth closed

        compliance = None
        AU12thres = None
        MMthres = None
        compMR1 = None
        compML1 = None
        compMM = None

        # Right lip
        if self.distMR1_ER1 - self.distNMR1_NER1 < AU12thres:
           compMR1 =  (self.distMR1_ER1 - self.distNMR1_NER1) / AU12thres
        # Left lip
        if self.distML1_EL1 - self.distNML1_NEL1 < AU12thres:
           compML1 = (self.distML1_EL1 - self.distNML1_NEL1) / AU12thres
        # Mouth closed: the more closed, the more compliance
        if self.distMM1_MM2 < MMthres:
            compMM = 1 - self.distMM1_MM2
        
        compliance = 0.5 * (0.5 * compML1 + 0.5 * compMR1) + 0.5 * compMM
        
        return compliance

    def __AU14(self):
        # mr1: out
        # ml1: out
        # mouth closed

        compliance = None
        AU14thres = None
        MMthres = None
        compMR1 = None
        compML1 = None
        compMM = None

        # Right lip
        if self.disthMR1_ER1 - self.disthNMR1_NER1 > AU14thres:
           compMR1 =  (self.disthMR1_ER1 - self.disthNMR1_NER1) / AU14thres
        # Left lip
        if self.disthML1_EL1 - self.disthNML1_NEL1 > AU14thres:
           compML1 = (self.disthML1_EL1 - self.disthNML1_NEL1) / AU14thres
        # Mouth closed: the more closed, the more compliance
        if self.distMM1_MM2 < MMthres:
            compMM = 1 - self.distMM1_MM2

        compliance = 0.5 * (0.5 * compML1 + 0.5 * compMR1) + 0.5 * compMM
        
        return compliance

# TODO: Introducir parámetros en la ponderación modificables para ajustar
#       el modelo posteriormente.
# Devuelve el valor de felicidad de 0 a 1 ponderado (mediante
# paramFelicidad a partir del vector actionUnits
    def comprobarFelicidad(self):
        self.paramFelicidad = np.zeros(46) - 1
        self.paramFelicidad[1] = 0
        self.paramFelicidad[2] = 0
        self.paramFelicidad[4] = 0
        self.paramFelicidad[6] = 0
        self.paramFelicidad[10] = 0
        self.paramFelicidad[12] = 0
        self.paramFelicidad[14] = 0
        self.felicidad = np.dot(self.actionUnits, self.paramFelicidad)
        return self.felicidad
