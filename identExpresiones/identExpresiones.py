import pandas as pd
import cv2
import numpy as np
import os
from zipfile import ZipFile


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


if __name__ == "__main__":
    data = cargarDatabase()
    ima = cargarImagen(data.loc[1])
    cv2.imshow('preview', ima)
    cv2.waitKey(0)
