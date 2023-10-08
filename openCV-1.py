# Import required libraries
import cv2  # OpenCV for computer vision tasks
from picamera2 import Picamera2  # Library for controlling the Raspberry Pi Camera

# Initialize and configure the Pi Camera
piCam = Picamera2()
piCam.preview_configuration.main.size = (1280, 720)  # Set resolution
piCam.preview_configuration.main.format = "RGB888"  # Set format
piCam.preview_configuration.align()  # Align the configuration settings
piCam.configure("preview")  # Apply the 'preview' configuration
piCam.start()  # Start the camera

# Main loop to capture video frames
while True:
    frame = piCam.capture_array()  # Capture a frame from the camera
    
    # Display the captured frame
    cv2.imshow("piCam", frame)
    
    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Cleanup resources
cv2.destroyAllWindows()
