import cv2
import numpy as np
import pyautogui
import urllib.request

cap = cv2.VideoCapture(1)
lower_range = np.array([0,0,251])
upper_range = np.array([0,0,255])
width , height = 1920,1080

p = np.load('points.npy')
p = p[0],p[len(p)-1]
print(p)

class Filtration:
    def __init__(self,image,width,height):
        #self.frame = cv2.resize(image , (width,height))
        self.image = image
        hsv_image = cv2.cvtColor(self.image,cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_image,lower_range,upper_range)
        self.contours, _ = cv2.findContours(mask.copy() , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
        self.centre = int(height/2),int(width/2)
    def returns(self):
        return self.image,self.contours,self.centre

points = []
class Main:
    def __init__():
        pass
    def run():
        while True:
            x,y,w,h = p[0][0],p[0][1],p[1][0],p[1][1]
            ret , frame = cap.read()
            #frame = cv2.flip(frame , 1)
            frame = cv2.resize(frame,(width,height))
            
            frame2 = frame[y:y+h,x:x+w]
            
            Filtered = Filtration(frame2 , width, height)
            frame2,contours,centre = Filtered.returns()
            #frame2 = cv2.resize(frame,(w,h))
            if len(contours)>0.99:
                c = max(contours , key = cv2.contourArea)
                (x,y),radius = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                try:
                    centre = (int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
                    if radius>12 and radius<50:
                        cv2.drawContours(frame2 , contours , -1 , (0,255,0) , 3)
                        cv2.circle(frame2 , (centre[0],centre[1]) , int(radius) , (255,0,0) ,3)
                        pyautogui.moveTo(x,y)
                except Exception as e:
                    pass

            hsv_image = cv2.cvtColor(frame2,cv2.COLOR_BGR2HSV)
            lr = np.array([121,0,81])
            ur = np.array([179,255,255])
            mask_ = cv2.inRange(hsv_image,lr,ur)
            contours_, _ = cv2.findContours(mask_.copy() , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
            if len(contours_)>40:
                c = max(contours_ , key = cv2.contourArea)
                pyautogui.click(clicks=2)
                print('Clicked')
                
            cv2.imshow('main-frame' , frame)
            cv2.imshow('Calibrated-frame' , frame2)
            cv2.imshow('mask-frame' , mask_)
            if cv2.waitKey(1) & 0xFF==ord('q'):
                cv2.destroyAllWindows()
                break
            
        cap.release()
Main.run()

