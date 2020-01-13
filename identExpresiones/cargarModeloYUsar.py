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
import os

if __name__ == "__main__":
    # Cargamos el modelo y el clasificador
    path = 'ModelosFelicidad(40-60)/'
    classifiers = os.listdir(path)
    # Para cada clasificador encontrado en el directorio
    for classifier in classifiers:
        filename = path + classifier
        loaded_model = pickle.load(open(filename, 'rb'))

        # Carga los datos de las AU
        datos = pd.read_csv('Database/dataBaseAUs.csv')
        X = datos.iloc[:, 1:]
        y = datos.Feliz
        # Guarda en un array los datos de los AU
        test = np.array(X.iloc[:,:])
        test.reshape(-1,1)
        # Realiza una prediccion
        result = loaded_model.predict(test)
        good = 0;
        bad = 0;
        total = 0;
        # Compara el resultado con la realidad
        for i in range(0,len(result)):
            if result[i] == y[i]:
                good = good + 1
            else:
                bad = bad + 1

            total = total + 1 

        print(classifier)
        print("good(%) = "+ str(round(good/total*100,1)) + ", bad(%) = " + str(round(bad/total*100,1)))