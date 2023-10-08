import cv2
from picamera2 import Picamera2
import time

piCam = Picamera2()
dispW=720
dispH=480
piCam.preview_configuration.main.size = (dispW,dispH)
piCam.preview_configuration.main.format="RGB888"
piCam.preview_configuration.controls.FrameRate=30
piCam.preview_configuration.align()
piCam.configure("preview")
piCam.start()

fps = 0
pos = (30, 60)
font = cv2.FONT_HERSHEY_SIMPLEX
height = 1.5
color = (0 , 0, 225)
weight=3

boxW = 250
boxH = 125
tlC = 50
tlR = 75
lrC = tlC + boxW
lrR = tlR + boxH
deltaC = 2
deltaR = 2
thickness = -1
Rcolor = (0, 125, 125)

while True:
    tStart=time.time()
    im = piCam.capture_array()
    cv2.putText(im,str(int(fps))+' FPS',pos,font,height,color,weight)
    if tlC + deltaC < 0 or lrC + deltaC > dispW - 1:
        deltaC = deltaC*(-1)
    if tlR + deltaR < 0 or lrR + deltaR > dispH - 1:
        deltaR = deltaR*(-1)
    tlC = tlC + deltaC
    tlR = tlR + deltaR
    lrC = lrC + deltaC
    lrR = lrR + deltaR
    cv2.rectangle(im, (tlC, tlR), (lrC, lrR), Rcolor, thickness)
    cv2.imshow("piCam", im)
    if cv2.waitKey(1)==ord('q'):
        break
    tEnd=time.time()
    loopTime=tEnd - tStart
    fps=.9*fps + .1*1/loopTime
    print(fps)
cv2.destroyAllWindows()