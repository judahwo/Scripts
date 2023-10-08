# Importing required libraries
import cv2                          # OpenCV for image processing
from picamera2 import Picamera2      # picamera2 for Raspberry Pi camera interface
import time                         # Standard Python library for time-related tasks

# Initialize the Picamera2 object
piCam = Picamera2()

# Set display width and height for preview
dispW = 720
dispH = 480

# Configure preview settings
piCam.preview_configuration.main.size = (dispW, dispH)
piCam.preview_configuration.main.format = "RGB888"
piCam.preview_configuration.controls.FrameRate = 30

# Apply the preview configurations and start the preview
piCam.preview_configuration.align()
piCam.configure("preview")
piCam.start()

# Initialize FPS (frames per second) variable and text properties
fps = 0
pos = (30, 60)                      # Position for FPS text
font = cv2.FONT_HERSHEY_SIMPLEX     # Font for FPS text
height = 1.5                        # Font height
color = (0, 0, 225)                 # Font color
weight = 3                          # Font weight (thickness)

# Initialize box properties
boxW = 250                          # Box width
boxH = 125                          # Box height
tlC = 50                            # Top-left corner (column)
tlR = 75                            # Top-left corner (row)
lrC = tlC + boxW                    # Lower-right corner (column)
lrR = tlR + boxH                    # Lower-right corner (row)
deltaC = 2                          # Change in column position per iteration
deltaR = 2                          # Change in row position per iteration
thickness = -1                      # Box thickness
Rcolor = (0, 125, 125)              # Rectangle color

# Main loop for display
while True:
    tStart = time.time()             # Capture start time for FPS calculation
    im = piCam.capture_array()       # Capture a frame
    
    # Overlay FPS on the frame
    cv2.putText(im, str(int(fps)) + ' FPS', pos, font, height, color, weight)
    
    # Logic to update box position and handle boundary conditions
    if tlC + deltaC < 0 or lrC + deltaC > dispW - 1:
        deltaC = deltaC * (-1)
    if tlR + deltaR < 0 or lrR + deltaR > dispH - 1:
        deltaR = deltaR * (-1)
    tlC = tlC + deltaC
    tlR = tlR + deltaR
    lrC = lrC + deltaC
    lrR = lrR + deltaR
    
    # Draw the rectangle on the frame
    cv2.rectangle(im, (tlC, tlR), (lrC, lrR), Rcolor, thickness)
    
    # Display the frame
    cv2.imshow("piCam", im)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break
    
    # Calculate FPS
    tEnd = time.time()
    loopTime = tEnd - tStart
    fps = .9 * fps + .1 * 1 / loopTime
    print(fps)

# Destroy any created OpenCV windows
cv2.destroyAllWindows()