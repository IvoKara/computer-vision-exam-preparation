import cv2 as cv
from defaults import img_matrix, kernel

dilated_img = cv.dilate(img_matrix, kernel)
eroded_img = cv.erode(dilated_img, kernel)
print(eroded_img)
