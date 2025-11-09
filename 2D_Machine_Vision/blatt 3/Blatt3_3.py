import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("/workspaces/WASD/2D_Machine_Vision/robot_gray.png")

hoehe, breite, kanaele = img.shape
print(f"Höhe: {hoehe}, Breite: {breite}, Kanäle: {kanaele}")

# Bei Graustufenbildern (nur 2D)
grau = cv.imread('/workspaces/WASD/2D_Machine_Vision/robot_gray.png', cv.IMREAD_GRAYSCALE)
hoehe, breite = grau.shape

# Gesamtanzahl der Pixel
anzahl_pixel = img.size
print(f"Gesamte Pixel: {anzahl_pixel}")

#Datentyp
datentyp= img.dtype
print(f"Datentyp :{datentyp}")

#minimal und max Wert der Pixel
min_wert=img.min()
max_wert= img.max()
print(f"Min: {min_wert}, Max: {max_wert}")

bild_float=img.astype(np.float32)

cv.imwrite('/workspaces/WASD/2D_Machine_Vision/robot_gray_grau.png',grau)

