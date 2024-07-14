import matplotlib.pyplot as plt
import numpy as np
import cv2 

img = cv2.imread('Module2/Week1/dog.jpeg',1)
gray_img = np.add(img.max(axis=2),img.min(axis=2))/2
plt.imshow(gray_img,cmap='gray')
plt.show()
print(gray_img[0,0])