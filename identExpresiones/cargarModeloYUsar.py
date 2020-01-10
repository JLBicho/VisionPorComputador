"""
 Este script sirve para cargar un modelo previamente entrenado
 y comprobar sus resultados con otras imagenes

"""

from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn import ensemble
from sklearn import neighbors
import numpy as np
import pandas as pd
import pickle
import cv2

# Devuelve la imágen a partir del dataframe
def cargarImagen(datos):
    ima = cv2.imread(datos)
    imaBW = cv2.cvtColor(ima, cv2.COLOR_BGR2GRAY)
    return imaBW

def marcarCara(imagen, detector, marcador):
    caras = detector.detectMultiScale(imagen)
    retval, puntos = marcador.fit(imagen, caras)
    return puntos[0]

if __name__ == "__main__":
    filename = 'ModelosFelicidad(80-20)/' + 'pasivoAgresivoClassifier [0.927].sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    datos = pd.read_csv('Database_nosotros/dataBaseAUs.csv')
    X = datos.iloc[:, 1:]
    y = datos.Feliz

    test = np.array(X.iloc[:,:])
    
    test.reshape(-1,1)
    result = loaded_model.predict(test)
    good = 0;
    bad = 0;
    total = 0;
    for i in range(0,len(result)):
        if result[i] == y[i]:
            good = good + 1
        else:
            bad = bad + 1

        total = total + 1 

    print("good = "+ str(good) + ", bad = "+str(bad) + ", total = " + str(total))
    print("good(%) = "+ str(round(good/total*100,1)) + ", bad(%) = " + str(round(bad/total*100,1)))