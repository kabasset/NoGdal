# NoGdal

## Purpose

This is an example project to demonstrate a mechanism to enable or disable a package-internal import (e.g. GDAL in `pyNaja`) from outside the package.

## TL;DR

There are two scripts, `main_default.py` and `main_no_gdal.py`, which call the same function, `readImage()`, with or without GDAL.
For more representativeness, the function is not called directly, though, but via an intermediate package, `bibASO`.
The only difference between both scripts is that the no-GDAL script starts by setting `pyNaja.USE_GDAL = False`.

## Explanation

`USE_GDAL` is implemented as a package variable of `pyNaja`, i.e. in `pyNaja/__init__.py`.
If it is `True`, then `readImage()` will use GDAL; otherwise it falls back on PIL.

This works because packages are singletons, so that importing `pyNaja.ImageIO` will set `USE_GDAL` only if `pyNaja` was not imported first.
Note that this mechanism only works when `USE_GDAL` is set before `pyNaja.ImageIO` is imported.
The most natural place to do so, as demonstrated here, is at the beginning of the main.
