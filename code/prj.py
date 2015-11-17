import cv2
import numpy as np



src=cv2.imread("h1.jpg")
src=cv2.resize(src,(500,500))
cv2.imshow("STEP 1-source",src)
hsv=cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
cv2.imshow("STEP 2-HSV",hsv)
hsvSplit=cv2.split(hsv)
cv2.imshow("STEP 3-HSV Split",hsvSplit[1])
#Bluring the imgage to enhance the hand
hsvSplit[1]=cv2.GaussianBlur(hsvSplit[1],(9,9),0)
cv2.imshow("STEP 4-HSV-Blur",hsvSplit[1])
ret,hsvSplit[1] = cv2.threshold(hsvSplit[1], 25, 255, cv2.THRESH_BINARY)
cv2.imshow("STEP 5-HSV-Threshold",hsvSplit[1])
t1, contours, hierarchy=cv2.findContours(hsvSplit[1],cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
hand=np.zeros(src.shape)

hand=np.zeros(src.shape,src.dtype)

##initilizing variables for finding max contours
max=0
pt=-1
## Finding largest contour
for i in range(0,len(contours),1):
    area=cv2.contourArea(contours[i])
    if area>max:
        max=area
        pt=i

cv2.pc


cv2.drawContours(hand, contours, pt, (255,255,255), cv2.FILLED)
cv2.imshow("STEP 6-Largest Contour",hand)

edge=cv2.Canny(hand,50,180,)
cv2.imshow("STEP 7-HandEdge",edge)


cv2.waitKey(0)