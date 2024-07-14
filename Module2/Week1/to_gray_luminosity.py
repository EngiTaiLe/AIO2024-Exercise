import matplotlib.pyplot as plt 
import numpy as np
import cv2 

img = cv2.imread('Module2/Week1/dog.jpeg',1)
gray_img = (img[:,:,0]*0.07)+(img[:,:,1]*0.72)+(img[:,:,2]*0.21)
plt.imshow(gray_img,cmap='gray')
plt.show()
print(gray_img[0,0])