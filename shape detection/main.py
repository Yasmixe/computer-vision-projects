import cv2
import numpy as np
def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #trouver les contours
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgco, cnt, -1, (255, 0, 0), 2)
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objcor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            if objcor == 3: objtype = "triangle"
            elif objcor == 4:
                asp = w/float(h)
                if asp >0.95 and asp <1.05: objtype="square"
                else: objtype = "rectangle"
            if objcor ==5:
                objtype = "pentagon"
            if objcor ==6:
                objtype = "hexagon"
            if objcor ==7:
                objtype = "heptagon"
            if objcor ==8:
                objtype = "octagon"
            if objcor ==9:
                objtype = "nonagon"

            cv2.rectangle(imgco,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgco, objtype, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)



img = cv2.imread("shape.png")
imgco = img.copy() #copie de notre image pour ne pas dessiner sur the original one
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #rendre notre photo grise
imgblur = cv2.GaussianBlur(imgGray,(7,7),1) #add blur
imgcanny = cv2.Canny(imgblur,50,50) #detect edges
getContours(imgcanny) #les contours

cv2.imshow("image",img)
cv2.imshow("imageGRAY",imgGray)
cv2.imshow("imageBlur",imgblur)
cv2.imshow("imagecanny",imgcanny)
cv2.imshow("contouring",imgco)

cv2.waitKey(0)
