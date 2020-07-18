import numpy as np 
import os
import cv2
import time
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("Sub.mp4",fourcc,20.0,(640,480))
time.sleep(2)
background = 0
c  = 0
for i in range(30):
    re, background = cap.read()
    if (re == False ):
        continue
    background = np.flip(background,axis = 1)
    
        
while(cap.isOpened()) :
    re , img = cap.read()
    if not re :
        break
    c = c+1
    img = np.flip(img , axis = 1)
    hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv,lower_red,upper_red)
    lower_red =  np.array([170,120,70])
    upper_red =  np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)
    mask1 = mask1 + mask2
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations =2)
    mask1 = cv2.dilate(mask1 , np.ones((3,3),np.uint8),iterations = 1)
    mask2 = cv2.bitwise_not(mask1)
    res1 = cv2.bitwise_and(background,background,mask = mask1)
    res2 = cv2.bitwise_and(img,img,mask= mask2)
    f_o = cv2.addWeighted(res1,1,res2,1,0)  
    cv2.imshow("INVISIBLE MAN",f_o)
    if (re== True):
        out.write(f_o)
   
    k= cv2.waitKey(10)
    if k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
