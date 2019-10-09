import pandas as pd
import cv2
# import numpy as np
import os
from zipfile import ZipFile
import SeleccionarPuntos as sp
from detectarExpresiones import detectarExpresiones


# Extraer imágenes de la Database si no se ha hecho antes
def extraerImagenes():
    if not os.path.exists('Images'):
        with ZipFile('Database/jaffedbase.zip', 'r') as zip:
            zip.extractall('Images')


# Cargar Database del directorio database
def cargarDatabase():
    data = pd.read_csv('Database/database.csv', sep=';', index_col=0)
    im_faltantes = [8, 12, 21, 76, 108, 183]
    for im in im_faltantes:
        data = data.drop(index=im, axis=1)
    # Se extraen las imagenes si no se ha realizado antes
    extraerImagenes()
    data['PATH'] = 0
    # Añadir columna con el path
    for indice in data.index:
        data.PATH.loc[indice] = ('Images/' + str(indice) + '.'
                                 + (data.PIC.loc[indice]).replace('-', '.')
                                 + '.tiff')
    return data


# Devuelve la imágen a partir del dataframe
def cargarImagen(datos):
    ima = cv2.imread(datos.PATH)
    imaBW = cv2.cvtColor(ima, cv2.COLOR_BGR2GRAY)
    return imaBW


def mostrarImagen(ima, titulo='Imagen'):
    cv2.imshow(titulo, ima)
    cv2.waitKey(0)


# Devuelve el primer elemento de una lista de arrays con los puntos que
# caracterizan cada cara en la imagen. Debe entrar la imagen frontalde
# la cara, un detector en boundig box de la cara y el marcador del archivo
# "lbfmodel.yaml"
def marcarCara(imagen, detector, marcador):
    caras = detector.detectMultiScale(imagen)
    retval, puntos = marcador.fit(imagen, caras)
    return puntos[0]


# Devuelve una copia la imagen pasada con los puntos descritos en el
# primer canal en de la variable puntos
def dibujarPuntos(imagen, puntos):
    ima = imagen.copy()
    cv2.face.drawFacemarks(ima, puntos, 255)
    return ima


if __name__ == "__main__":
    data = cargarDatabase()
    ima = cargarImagen(data.loc[20])

    # Contiene la información para detectar caras en una imagen
    detectorCara = cv2.CascadeClassifier(cv2.data.haarcascades
                                         + "haarcascade_"
                                         + "frontalface_default.xml")

    marcador = cv2.face.createFacemarkLBF()
    marcador.loadModel("Modelos/lbfmodel.yaml")

    puntos = marcarCara(ima, detectorCara, marcador)
    ima2 = dibujarPuntos(ima, puntos)
    mostrarImagen(ima2)
    mostrarImagen(dibujarPuntos(ima, sp.selPuntosLabios((puntos))))
    prueba = detectarExpresiones(detectorCara, marcador, ima)
    prueba.calcularPuntosNeutra()

    """
    mostrarImagen(ima)
    clasifOjos = cv2.CascadeClassifier(cv2.data.haarcascades
                                       + "haarcascade_eye.xml")
    ojos = clasifOjos.detectMultiScale(ima)
    for ojo in ojos:
        ima2 = cv2.rectangle(ima, (ojo[0], ojo[1]),
                             (ojo[0] + ojo[2], ojo[1] + ojo[3]), 0)
    """
