import pandas as pd
import identExpresiones as ie
import detectarExpresiones as de
import cv2
import numpy as np


# Entra la base de datos en data, el número del action unit que se desea
# comprobar en au y un objeto detectaeExpresiones con detector de cara y
# marcador de puntos en detectExp.
# Devuelve la media y la desviación típica de los resultados obtenidos para el
# AU al recorrer la base de datos cuando se aplica a caras felices y cuando se
# aplica a caras no felices
def pruebasAU(data, au, detectExp):
    persona = None
    personaAnterior = None
    totalAUfeliz = []
    totalAUnoFeliz = []
    for i, row in data.iterrows():
        persona = row.PIC[0:2]
        if persona != personaAnterior:
            detectExp.setImagenNeutra(ie.cargarImagen(row))
        else:
            detectExp.setImagen(ie.cargarImagen(row))
            aus = detectExp.comprobarAUs()
            if row.HAP > 4:
                totalAUfeliz.append(aus[au])
                print("Imagen: " + str(i))
                print("AUs:" + str(aus[au]))
            else:
                totalAUnoFeliz.append(aus[au])

        personaAnterior = persona
    totalAUfeliz = np.asarray(totalAUfeliz)
    totalAUnoFeliz = np.asarray(totalAUnoFeliz)
    return [(totalAUfeliz.mean(), totalAUfeliz.std()),
            (totalAUnoFeliz.mean(), totalAUnoFeliz.std())]


if __name__ == '__main__':
    detectorCara = cv2.CascadeClassifier(cv2.data.haarcascades
                                         + "haarcascade_"
                                         + "frontalface_default.xml")

    marcador = cv2.face.createFacemarkLBF()
    marcador.loadModel("Modelos/lbfmodel.yaml")
    prueba = de.detectarExpresiones(detectorCara, marcador)
    data = ie.cargarDatabase()
    print(pruebasAU(data, 1, prueba))
    
