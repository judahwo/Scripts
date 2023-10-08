import cv2
from picamera2 import Picamera2
import time

piCam = Picamera2()
dispW=1280
dispH=720
piCam.preview_configuration.main.size = (dispW,dispH)
piCam.preview_configuration.main.format="RGB888"
piCam.preview_configuration.controls.FrameRate=30
piCam.preview_configuration.align()
piCam.configure("preview")
piCam.start()
fps=0
pos=(30,60)
font=cv2.FONT_HERSHEY_SIMPLEX
height=1.5
color=(0,0,225)
weight=3

while True:
    tStart=time.time()
    im = piCam.capture_array()
    cv2.putText(im,str(int(fps))+' FPS',pos,font,height,color,weight)
    cv2.imshow("piCam", im)
    if cv2.waitKey(1)==ord('q'):
        break
    tEnd=time.time()
    loopTime=tEnd - tStart
    fps=.9*fps + .1*1/loopTime
    print(fps)
cv2.destroyAllWindows()