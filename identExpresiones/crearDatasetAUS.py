import pandas as pd
import identExpresiones as ie
import detectarExpresiones as de
import cv2
import numpy as np


def dataFrameAUs(data, au, detectExp):
    persona = None
    personaAnterior = None
    datos = []
    indiceAUS = np.array([1, 2, 4, 6, 10, 12, 14])
    for i, row in data.iterrows():
        persona = row.PIC[0:2]
        if persona != personaAnterior:
            detectExp.setImagenNeutra(ie.cargarImagen(row))
        else:
            detectExp.setImagen(ie.cargarImagen(row))
            aus = detectExp.comprobarAUs()[indiceAUS]
            if row.HAP > 4:
                feliz = 1
            else:
                feliz = 0
            dataAUS = np.append(feliz, aus)
            datos.append(dataAUS)
        personaAnterior = persona
    datos = np.asarray(datos)
    datos = pd.DataFrame(datos, columns=['Feliz', 'au1', 'au2', 'au4', 'au6',
                                         'au10', 'au12', 'au14'])
    return datos


if __name__ == '__main__':
    detectorCara = cv2.CascadeClassifier(cv2.data.haarcascades
                                         + "haarcascade_"
                                         + "frontalface_default.xml")

    marcador = cv2.face.createFacemarkLBF()
    marcador.loadModel("Modelos/lbfmodel.yaml")
    prueba = de.detectarExpresiones(detectorCara, marcador)
    data = ie.cargarDatabase()

    datos = dataFrameAUs(data, 1, prueba)
    datos.to_csv("Database/dataBaseAUs.csv", index=False)
