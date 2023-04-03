import pyNaja

if pyNaja.USE_GDAL:
    print('import gdal')
else:
    print('import pil')


def readImageGdal(filename):
    print(f'gdal.readImage({filename})')


def readImagePil(filename):
    print(f'pil.readImage({filename})')


readImage = readImageGdal if pyNaja.USE_GDAL else readImagePil
