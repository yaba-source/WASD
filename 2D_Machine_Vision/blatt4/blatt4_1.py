from PIL import Image
import numpy as np

img = Image.open("/workspaces/WASD/2D_Machine_Vision/blatt4/robot.png")
pixels=np.array(img)


grau= np.zeros((pixels.shape [0],pixels.shape [1]))
for i in range (pixels.shape[0]):
    for j in range (pixels.shape[1]):
        r,g,b= pixels[i,j,0],pixels[i, j, 1], pixels[i, j, 2]
        grau[i, j] = 0.299 * r + 0.587 * g + 0.114 * b # oder (r+g+b)/3
grau_img= Image.fromarray(grau.astype(np.uint8))
grau_img.save('/workspaces/WASD/2D_Machine_Vision/robot_gray_grau.png')