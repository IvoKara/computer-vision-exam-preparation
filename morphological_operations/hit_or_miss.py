import cv2 as cv
from defaults import img_matrix, kernel

out_img = cv.morphologyEx(img_matrix, cv.MORPH_HITMISS, kernel)
print(out_img)
