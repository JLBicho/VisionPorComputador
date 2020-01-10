print("Cargando datos...")
import identExpresiones as ie
import cv2
import numpy as np
import easygui as eg


def introducirImagenNeutra():
    path = eg.fileopenbox("Selecione un archivo")
    try:
        ima = cargarImagenPath(path)
        detecExp.setImagenNeutra(ima)
        print("\nImagen cargada correctamente\n")
    except:
        print("Archivo no reconocido")


def introducirImagen():
    path = eg.fileopenbox("Selecione un archivo")
    try:
        ima = cargarImagenPath(path)
        detecExp.setImagen(ima)
        print("\nImagen cargada correctamente\n")
    except:
        print("Archivo no reconocido")


def mostrarAUs():
    aus = detecExp.comprobarAUs()
    for i in [1, 2, 4, 6, 10, 12, 14]:
        print("AU" + str(i) + ": " + str(aus[i]))


def comprobarFelicidad():
    detecExp.comprobarAUs()
    feliz = detecExp.comprobarFelicidad()
    if feliz == 1:
        print("\nEl modelo determina que la imagen es FELIZ")
    else:
        print("\nEl modelo determina que la imagen es NO FELIZ")


def mostrarImagenes():
    imaNeutra = detecExp.imagenNeutra
    puntos = ie.marcarCara(imaNeutra, detectorCara, marcador)
    imaNeutra = ie.dibujarPuntos(imaNeutra, puntos)
    ima = detecExp.imagen
    puntos = ie.marcarCara(ima, detectorCara, marcador)
    ima = ie.dibujarPuntos(ima, puntos)
    ie.mostrarImagen(np.hstack((imaNeutra, ima)))


def cargarImagenPath(path):
    ima = cv2.imread(path)
    imaBW = cv2.cvtColor(ima, cv2.COLOR_BGR2GRAY)
    return imaBW


def menu(argumento):
    switcher = {
        '1': introducirImagenNeutra,
        '2': introducirImagen,
        '3': mostrarAUs,
        '4': comprobarFelicidad,
        '5': mostrarImagenes,
        '6': lambda: exit(0)
    }
    func = switcher.get(argumento, lambda: print("Argumento erroneo"))
    return func()


def textMenu():
    print("\nSeleccione una opción:\n")
    print("\t1) Introducir imagen neutra")
    print("\t2) Introducir imagen para comprobar")
    print("\t3) Mostrar valor de los action units")
    print("\t4) Comprobar felicidad")
    print("\t5) Mostrar puntos detectados en las imágenes")
    print("\t6) Salir")


if __name__ == "__main__":
    data = ie.cargarDatabase()
    imaNeutra = ie.cargarImagen(data.loc[1])
    imaFeliz = ie.cargarImagen(data.loc[4])
    # Contiene la información para detectar caras en una imagen
    detectorCara = cv2.CascadeClassifier(cv2.data.haarcascades
                                         + "haarcascade_"
                                         + "frontalface_default.xml")

    marcador = cv2.face.createFacemarkLBF()
    marcador.loadModel("Modelos/lbfmodel.yaml")
    detecExp = ie.detectarExpresiones(detectorCara, marcador, imaNeutra, imaFeliz)
    puntos = ie.marcarCara(imaFeliz, detectorCara, marcador)
    ima2 = ie.dibujarPuntos(imaFeliz, puntos)

    while(1):
        textMenu()
        opcion = input()
        menu(opcion)
