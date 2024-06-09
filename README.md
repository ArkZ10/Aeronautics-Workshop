# Aeronautics Workshop Code

## TVDM COLOR DETECT

This Python code uses OpenCV to capture video from a webcam, process the frames to detect colored objects (red, green, blue, and purple), and draw rectangles around them if they fall within a specific area on the screen. It identifies objects based on their color in the HSV color space, uses contour detection to find and draw bounding rectangles around the largest detected objects, and counts frames to potentially control servo movements, indicated by the increment of the servo variables. The code includes mechanisms to print messages when certain frame counts are reached, indicating when a servo should move, and displays the processed video feed with bounding boxes around the detected colored objects.


## QR Scanner 

This code captures video from a webcam, decodes QR codes in real-time using the Pyzbar library, and displays the results. It initializes the webcam with a resolution of 640x480 pixels and enters a loop to continuously read frames. For each frame, it detects QR codes, checks if they fit within a specified region and size, decodes the QR code data, and prints it. It draws a polygon around the detected QR codes and overlays the decoded data as text on the image. A fixed rectangle is drawn on the frame for visual reference, and the processed video is displayed until the 'Escape' key is pressed to exit the loop.

## HSV Tracker


This script captures video from a webcam and allows users to manipulate HSV (Hue, Saturation, Value) thresholds using trackbars to filter colors in real-time. It initializes the webcam, retrieves its width and height, and sets up global variables for HSV ranges. Functions to handle trackbar events are defined to update these HSV values. Two sets of trackbars (though only one is used in this script) allow dynamic adjustment of the HSV range for filtering. The main loop captures frames, converts them to HSV color space, applies the HSV thresholds to create a binary mask, and finds contours within the mask. The filtered video and original video are displayed until the 'Escape' key is pressed. Additionally, there is a second part of the script detecting red objects by their HSV values and drawing bounding rectangles around them.
