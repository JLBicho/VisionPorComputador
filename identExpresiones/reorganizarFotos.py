import os

for filename in os.listdir("C:/Users/Daniel/Desktop/jaffedbase"):
    longitud = len(filename)
    posPunto1 = filename.find('.', 3)
    posPunto2 = filename.rfind('.')
    numeracion = filename[posPunto1 + 1:posPunto2]
    dst = numeracion + '.' + filename[0:6] + '.tiff'
    src = "C:/Users/Daniel/Desktop/jaffedbase" + '/' + filename
    dst = "C:/Users/Daniel/Desktop/jaffedbase" + '/' + dst
    os.rename(src, dst)
