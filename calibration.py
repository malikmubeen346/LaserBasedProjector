import cv2,os
import numpy as np
import pyautogui
import urllib.request
import time

print('''
    [Calibration - Info] - Depending upon camera and processing power This Screen will appear after 5 seconds
    Point the laser from top-left corner to bottom-right corner
    frame count is 500
    ------------------------
    |X                      |
    |  -                    |
    |     -                 |
    |        -              |
    |            -          |
    |                 x     |
    ------------------------
    ''')
#time.sleep()
cap = cv2.VideoCapture(1)
lower_range = np.array([0,0,251])
upper_range = np.array([0,0,255])
width , height = 1920,1080


class Filtration:
    def __init__(self,image,width,height):
        self.frame = cv2.resize(image , (width,height))
        #self.frame = cv2.flip(self.frame , 1)
        hsv_image = cv2.cvtColor(self.frame,cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_image,lower_range,upper_range)
        self.contours, _ = cv2.findContours(mask.copy() , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
        self.centre = int(height/2),int(width/2)
    def returns(self):
        return self.frame,self.contours,self.centre

points = []

class Main:
    def __init__():
        pass
    def run():
        cc = 0
        while cc<200:
            ret , frame = cap.read()
            frame = cv2.resize(frame,(height,width))
            Filtered = Filtration(frame , width, height)
            frame,contours,centre = Filtered.returns()
            if len(contours)>0:
                c = max(contours , key = cv2.contourArea)
                (x,y),radius = cv2.minEnclosingCircle(c)
                points.append([int(x),int(y)])
                M = cv2.moments(c)
                try:
                    centre = (int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
                    if radius>10:
                        cv2.drawContours(frame , contours , -1 , (0,255,0) , 1)
                        cv2.circle(frame , (centre[0],centre[1]) , int(radius) , (255,0,0) ,3)
                        pyautogui.moveTo(x,y)
                except Exception as e:
                    pass
            cv2.imshow('project' , frame)

            if cv2.waitKey(1) & 0xFF==ord('q'):
                cv2.destroyAllWindows()
                break
            cc+=1
        cap.release()
Main.run()

np.save('points',points,allow_pickle = True)
os.system('python project_file_.py')
