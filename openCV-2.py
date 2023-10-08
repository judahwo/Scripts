# Description: This program displays the frames per second (FPS) of the camera
#              preview on the screen. The FPS is calculated by taking the
#              reciprocal of the time it takes to capture and display a frame.
#              The FPS is displayed in the upper left corner of the screen.
#              The FPS is calculated using a low-pass filter to smooth the
#              value. The FPS is displayed in red text with a thickness of 3.
#              The FPS is displayed until the user presses 'q' to quit.

# Import necessary libraries
import cv2
from picamera2 import Picamera2
import time

# Initialize camera and preview settings
piCam = Picamera2()
dispW = 1280
dispH = 720
piCam.preview_configuration.main.size = (dispW, dispH)
piCam.preview_configuration.main.format = "RGB888"
piCam.preview_configuration.controls.FrameRate = 30
piCam.preview_configuration.align()
piCam.configure("preview")
piCam.start()

# Initialize FPS and text properties
fps = 0
pos = (30, 60)
font = cv2.FONT_HERSHEY_SIMPLEX
height = 1.5
color = (0, 0, 225)
weight = 3

# Main loop for capturing frames and displaying FPS
while True:
    tStart = time.time()
    im = piCam.capture_array()
    
    # Overlay FPS on the frame
    cv2.putText(im, str(int(fps)) + ' FPS', pos, font, height, color, weight)
    
    # Display the frame
    cv2.imshow("piCam", im)
    
    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break
    
    # Calculate FPS
    tEnd = time.time()
    loopTime = tEnd - tStart
    fps = .9 * fps + .1 * 1 / loopTime
    print(fps)

# Cleanup
cv2.destroyAllWindows()
