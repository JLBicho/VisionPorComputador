import pandas as pd
## Me da colision con ROS
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
##

import cv2
import numpy as np
import os
from zipfile import ZipFile
import SeleccionarPuntos as sp
from detectarExpresiones import detectarExpresiones
# import warnings
# warnings.filterwarnings('always')


# Extraer imágenes de la Database si no se ha hecho antes
def extraerImagenes():
    if not os.path.exists('Images'):
        with ZipFile('Database/jaffedbase.zip', 'r') as zip:
            zip.extractall('Images')

def generarCsv():
    df=[]
    index = 1
    path = 'Database_nosotros/caretos'
    # Store the image file names in a list as long as they are jpgs
    images = [f for f in os.listdir(path) if os.path.splitext(f)[-1] == '.jpg']
    for i in images: 
        #for j, caracter in enumerate(i):
            #df.append(caracter)
        df.append([i[0], i[1], i])
        index = index + 1
    df = np.asarray(df)    
    df = pd.DataFrame(df,columns=['per','emo','arc'])
    df.to_csv(r'Database_nosotros/basedatos.csv')

#Lee los modelos de las distintas carpetas y los mete en una lista   
def leerModelos():
    lista = []
    path = 'ModelosFelicidad(40-60)'
    modelos = [f for f in os.listdir(path) if os.path.splitext(f)[-1] == '.sav']
    lista.append(modelos)
    path = 'ModelosFelicidad(60-40)'
    modelos = [f for f in os.listdir(path) if os.path.splitext(f)[-1] == '.sav']
    lista.append(modelos)
    path = 'ModelosFelicidad(80-20)'
    modelos = [f for f in os.listdir(path) if os.path.splitext(f)[-1] == '.sav']
    lista.append(modelos)
    return lista
    
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
        data.loc[indice, 'PATH'] = ('Images/' + str(indice) + '.'
                                    + (data.loc[indice, 'PIC']).
                                    replace('-', '.') + '.tiff')
    return data

# Cargar Database del directorio database_validacion
def cargarDatabase_faces():
    data = pd.read_csv('Database_validacion/basedatos.csv', index_col=False)
    
    data['PATH'] = 0
    # Añadir columna con el path
    for indice in data.index:
        data.loc[indice, 'PATH'] = ('Database_validacion/faces/'
                                    + (data.loc[indice, 'arc']))

    return data

# Cargar Database del directorio database_nosotros
def cargarDatabase_caretos():
    data = pd.read_csv('Database_nosotros/basedatos.csv', index_col=False)

    data['PATH'] = 0
    # Añadir columna con el path
    for indice in data.index:
        data.loc[indice, 'PATH'] = ('Database_nosotros/caretos/' + (data.loc[indice, 'arc']))
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
    #MAIN DE PRUEBA
    
    #cargarDatabase_faces()
    
    #MAIN DE DANI
    """
    data = cargarDatabase()
    imaNeutra = cargarImagen(data.loc[1])
    imaFeliz = cargarImagen(data.loc[4])
    # Contiene la información para detectar caras en una imagen
    detectorCara = cv2.CascadeClassifier(cv2.data.haarcascades
                                         + "haarcascade_"
                                         + "frontalface_default.xml")

    marcador = cv2.face.createFacemarkLBF()
    marcador.loadModel("Modelos/lbfmodel.yaml")
    """
    """
    puntos = marcarCara(imaNeutra, detectorCara, marcador)
    ima2 = dibujarPuntos(imaNeutra, puntos)
    mostrarImagen(ima2)
    mostrarImagen(dibujarPuntos(imaNeutra, sp.selPuntosBoca((puntos))))
    mostrarImagen(dibujarPuntos(imaNeutra, sp.selPuntosLabios((puntos))))
    """
    """
    prueba = detectarExpresiones(detectorCara, marcador, imaNeutra, imaFeliz)
    aus = prueba.comprobarAUs()
    for i in [1, 2, 4, 6, 10, 12, 14]:
        print("AU" + str(i) + ": " + str(aus[i]))

    print("Felicidad total: " + str(prueba.comprobarFelicidad()))
    puntos = marcarCara(imaFeliz, detectorCara, marcador)
    ima2 = dibujarPuntos(imaFeliz, puntos)
    #mostrarImagen(ima2)
    
    """
    """
    prueba.puntosBocaNeutra
    prueba.puntosLabiosNeutra
    print(prueba.puntosBocaNeutra)
    print(prueba.puntosLabiosNeutra)

    mostrarImagen(ima)
    clasifOjos = cv2.CascadeClassifier(cv2.data.haarcascades
                                       + "haarcascade_eye.xml")
    ojos = clasifOjos.detectMultiScale(ima)
    for ojo in ojos:
        ima2 = cv2.rectangle(ima, (ojo[0], ojo[1]),
                             (ojo[0] + ojo[2], ojo[1] + ojo[3]), 0)
    """
