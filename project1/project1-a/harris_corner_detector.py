import os, cv2
import numpy as numpy

img = cv2.imread("original_img/geo_wave.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
corners = cv2.cornerHarris(gray, 3,3,0.04)
img[corners>0.01*corners.max()]=[0,0,255]
"""
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
os.mkdir("result_img")
cv2.imwrite("result_img/geo_wave_result.jpg", img)

