import pyNaja
pyNaja.USE_GDAL = False  # nopep8

from bibASO.DoTheMagic import run


if __name__ == '__main__':
    run('file.tif')
