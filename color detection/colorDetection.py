import cv2
import numpy as np
def empty(a):
    pass
cv2.namedWindow("trackbars")
cv2.resizeWindow("trackbars",640,240)
cv2.createTrackbar("hue min","trackbars",75,179,empty)
cv2.createTrackbar("hue max","trackbars",114,179,empty)
cv2.createTrackbar("sat min","trackbars",200,255,empty)
cv2.createTrackbar("sat max","trackbars",255,255,empty)
cv2.createTrackbar("val min","trackbars",144,179,empty)
cv2.createTrackbar("val max","trackbars",216,255,empty)

while True:
 logo = cv2.imread("logo.png")
 img = cv2.resize(logo,(350,350))
 imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
 h_min = cv2.getTrackbarPos("hue min","trackbars")
 h_max = cv2.getTrackbarPos("hue max","trackbars")
 s_min = cv2.getTrackbarPos("sat min","trackbars")
 s_max = cv2.getTrackbarPos("sat max","trackbars")
 v_min = cv2.getTrackbarPos("val min","trackbars")
 v_max = cv2.getTrackbarPos("val max","trackbars")
 print(h_min)
 print(h_max)
 print(s_min)
 print(s_max)
 print(v_min)
 print(v_max)
 lower = np.array([h_min,s_min,v_min])
 upper = np.array([h_max,s_max,v_max])
 mask = cv2.inRange(imgHSV,lower,upper)
 imgresult = cv2.bitwise_and(img,img,mask=mask)
 cv2.imshow("image",imgHSV)
 cv2.imshow("mask",mask)
 cv2.imshow("result",imgresult)


 cv2.waitKey(1)