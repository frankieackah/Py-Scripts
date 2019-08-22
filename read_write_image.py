import numpy as np
import cv2

image_reader = cv2.imread('img1.png', 0)
cv2.imshow('image', image_reader)
cv2.waitKey(0)
cv2.destroyAllWindows()
