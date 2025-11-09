import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread("/workspaces/WASD/2D_Machine_Vision/farb_img.jpg")
img_grau =cv.imread("/workspaces/WASD/2D_Machine_Vision/farb_img.jpg", cv.IMREAD_GRAYSCALE)

cv.imwrite('/workspaces/WASD/2D_Machine_Vision/farb_grau.png',img_grau)

img_farb_1=cv.cvtColor(img_grau,cv.COLOR_GRAY2BGR)
cv.imwrite("ergebnis.png",img_farb_1)

b, g, r = cv.split(img)

fig, axes = plt.subplots(1, 4, figsize=(16, 4))

axes[0].imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
axes[0].set_title("Original")
axes[0].axis('off')

axes[1].imshow(b, cmap='gray')
axes[1].set_title("Blau-Kanal")
axes[1].axis('off')

axes[2].imshow(g, cmap='gray')
axes[2].set_title("Grün-Kanal")
axes[2].axis('off')

axes[3].imshow(r, cmap='gray')
axes[3].set_title("Rot-Kanal")
axes[3].axis('off')

plt.tight_layout()
plt.savefig("kanaele_anzeige.png")
plt.show()