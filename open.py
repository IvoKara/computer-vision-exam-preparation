import cv2 as cv
from defaults import img_matrix, kernel

eroded_img = cv.erode(img_matrix, kernel)
dilated_img = cv.dilate(eroded_img, kernel)
print(dilated_img)
