# Desc: This program uses the Pi Camera v2 to capture video and display it on the screen.
#       The video feed is displayed in a window titled "piCam". The video feed is
#       displayed until the user presses 'q' to quit.

# Import necessary libraries
import cv2  # OpenCV library for computer vision
from picamera2 import Picamera2  # Library for Pi Camera v2
import time  # Standard Python library for time-related tasks

# Initialize Pi Camera settings
piCam = Picamera2()
dispW = 720
dispH = 480
piCam.preview_configuration.main.size = (dispW, dispH)
piCam.preview_configuration.main.format = "RGB888"
piCam.preview_configuration.controls.FrameRate = 30
piCam.preview_configuration.align()
piCam.configure("preview")
piCam.start()

# Initialize FPS display settings
fps = 0
pos = (30, 60)
font = cv2.FONT_HERSHEY_SIMPLEX
height = 1.5
color = (0, 0, 225)
weight = 3

# Initialize rectangle settings
upperLeft = (550, 300)
lowerRight = (650, 375)
rColor = (255, 0, 255)
thickness = 3

# Initialize circle settings
cent = (450, 250)
cColor = (0, 255, 255)
cThick = 7
r = 35

# Main loop to capture and display video
while True:
    tStart = time.time()
    im = piCam.capture_array()
    
    # Overlay FPS on video feed
    cv2.putText(im, str(int(fps)) + ' FPS', pos, font, height, color, weight)
    
    # Draw rectangle and circle on video feed
    cv2.rectangle(im, upperLeft, lowerRight, rColor, thickness)
    cv2.circle(im, cent, r, cColor, cThick)
    
    # Display video feed
    cv2.imshow("piCam", im)
    
    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break
    
    # Update FPS calculation
    tEnd = time.time()
    loopTime = tEnd - tStart
    fps = .9 * fps + .1 * 1 / loopTime
    print(fps)

# Cleanup
cv2.destroyAllWindows()
