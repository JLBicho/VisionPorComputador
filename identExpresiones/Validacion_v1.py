#Script para validar si una cara está feliz o no

#Incluimos pandas, para leer ficheros csv
import pandas
#Incluimos os para poder elegir como workin directory la carpeta que contiene nuestro csv
import os

os.chdir('D:\\UNIVERSIDAD\\2 MII-MAR\\Visión por computador\\Trabajo Reconocimiento Emociones\\Pruebas y validacion')
datos = pandas.read_csv("database_comas.txt")
#datos.iloc[1,2] #me devuelve el dato de la fila 2, columna 3 (empieza en 0)

def feliz_or_not(numero):
	if datos.iloc[numero,1] > 4:
		print("Esta feliz")
		feliz = 1
	else:
		print("No esta feliz")
		feliz = 0

feliz_or_not(2)
feliz_or_not(3)
feliz_or_not(4)