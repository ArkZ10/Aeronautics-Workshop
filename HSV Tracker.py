import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0) ## untuk membaca camera video capture dan 0 untuk webcam
width = int(cam.get(3)) ## mengambil lebar camera
height = int(cam.get(4)) ## mengambil tinggi camera


low_H = [0, 0] ## memberi nilai
low_S = [0, 0]
low_V = [0, 0]
high_H = [255, 255]
high_S = [255, 255]
high_V = [255, 255]

low_H1 = [0, 0] ## memberi nilai
low_S1 = [0, 0]
low_V1 = [0, 0]
high_H1 = [255, 255]
high_S1 = [255, 255]
high_V1 = [255, 255]

low_H_name = 'low H' ## memberi nama
low_S_name = 'low S'
low_V_name = 'low V'
high_H_name = 'high H'
high_S_name = 'high S'
high_V_name = 'high V'

window_detection_name = 'HSV1 Trackbar'
window_detection_name1 = 'HSV2 Trackbar'

def on_low_H_tresh_trackbar(val):
    global low_H
    global high_H
    low_H[0] = val
    low_H[0] = min(high_H[0]-1, low_H[0])
    cv.setTrackbarPos(low_H_name, window_detection_name, low_H[0]) ## memberi posisi trackbar
def on_high_H_tresh_trackbar(val):
    global low_H
    global high_H
    high_H[0] = val
    high_H[0] = max(high_H[0], low_H[0]+1)
    cv.setTrackbarPos(high_H_name, window_detection_name, high_H[0])
def on_low_S_tresh_trackbar(val):
    global low_S
    global high_S
    low_S[0] = val
    low_S[0] = min(high_S[0]-1, low_S[0])
    cv.setTrackbarPos(low_S_name, window_detection_name, low_S[0])
def on_high_S_tresh_trackbar(val):
    global low_S
    global high_S
    high_S[0] = val
    high_S[0] = max(high_S[0], low_S[0] + 1)
    cv.setTrackbarPos(high_S_name, window_detection_name, high_S[0])
def on_low_V_tresh_trackbar(val):
    global low_V
    global high_V
    low_V[0] = val
    low_V[0] = min(high_V[0]-1, low_V[0])
    cv.setTrackbarPos(low_V_name, window_detection_name, low_V[0])
def on_high_V_tresh_trackbar(val):
    global low_V
    global high_V
    high_V[0] = val
    high_V[0] = max(high_V[0], low_V[0] + 1)
    cv.setTrackbarPos(high_V_name, window_detection_name, high_V[0])

#TRACKBAR2
def on_low_H_tresh_trackbar1(val1):
    global low_H1
    global high_H1
    low_H1[0] = val1
    low_H1[0] = min(high_H1[0]-1, low_H1[0])
    cv.setTrackbarPos(low_H_name, window_detection_name1, low_H1[0]) ## memberi posisi trackbar
def on_high_H_tresh_trackbar1(val1):
    global low_H1
    global high_H1
    high_H1[0] = val1
    high_H1[0] = max(high_H1[0], low_H1[0]+1)
    cv.setTrackbarPos(high_H_name, window_detection_name1, high_H1[0])
def on_low_S_tresh_trackbar1(val1):
    global low_S1
    global high_S1
    low_S1[0] = val1
    low_S1[0] = min(high_S1[0]-1, low_S1[0])
    cv.setTrackbarPos(low_S_name, window_detection_name1, low_S1[0])
def on_high_S_tresh_trackbar1(val1):
    global low_S1
    global high_S1
    high_S1[0] = val1
    high_S1[0] = max(high_S1[0], low_S1[0] + 1)
    cv.setTrackbarPos(high_S_name, window_detection_name1, high_S1[0])
def on_low_V_tresh_trackbar1(val1):
    global low_V1
    global high_V1
    low_V1[0] = val1
    low_V1[0] = min(high_V1[0]-1, low_V1[0])
    cv.setTrackbarPos(low_V_name, window_detection_name1, low_V1[0])
def on_high_V_tresh_trackbar1(val1):
    global low_V1
    global high_V1
    high_V1[0] = val1
    high_V1[0] = max(high_V1[0], low_V1[0] + 1)
    cv.setTrackbarPos(high_V_name, window_detection_name1, high_V1[0])

cv.namedWindow(window_detection_name)
# cv.namedWindow(window_detection_name1)

def TrackBar1():
    cv.createTrackbar(low_H_name, window_detection_name, low_H[0], 255, on_low_H_tresh_trackbar) ## membuat trackbar
    cv.createTrackbar(high_H_name, window_detection_name, high_H[0], 255, on_high_H_tresh_trackbar)
    cv.createTrackbar(low_S_name, window_detection_name, low_S[0], 255, on_low_S_tresh_trackbar)
    cv.createTrackbar(high_S_name, window_detection_name, high_S[0], 255, on_high_S_tresh_trackbar)
    cv.createTrackbar(low_V_name, window_detection_name, low_V[0], 255, on_low_V_tresh_trackbar)
    cv.createTrackbar(high_V_name, window_detection_name, high_V[0], 255, on_high_V_tresh_trackbar)

def TrackBar2():
    cv.createTrackbar(low_H_name, window_detection_name1, low_H1[0], 255, on_low_H_tresh_trackbar1) ## membuat trackbar
    cv.createTrackbar(high_H_name, window_detection_name1, high_H1[0], 255, on_high_H_tresh_trackbar1)
    cv.createTrackbar(low_S_name, window_detection_name1, low_S1[0], 255, on_low_S_tresh_trackbar1)
    cv.createTrackbar(high_S_name, window_detection_name1, high_S1[0], 255, on_high_S_tresh_trackbar1)
    cv.createTrackbar(low_V_name, window_detection_name1, low_V1[0], 255, on_low_V_tresh_trackbar1)
    cv.createTrackbar(high_V_name, window_detection_name1, high_V1[0], 255, on_high_V_tresh_trackbar1)

TrackBar1()
# TrackBar2()

while(True): ## infinite loop
    ret, img = cam.read() ## untuk mendapatkan frame/gambar yang dapat dan ret untuk tahu apakah capture berjalan dengan baik contoh zoom dan pycharm berjalan bersama
    img_flip = cv.flip(img, 1) ## untuk flip camera
    HSV = cv.cvtColor(img_flip, cv.COLOR_BGR2HSV) ## mengubah warna

    # bnw = cv.inRange(HSV, (low_H[0]+low_H1[0], low_S[0]+low_S1[0], low_V[0]+low_V1[0]), (high_H[0]+high_H1[0], high_S[0]+high_S1[0], high_V[0]+high_V1[0])) ## memberi range
    bnw = cv.inRange(HSV, (low_H[0], low_S[0], low_V[0]), (high_H[0], high_S[0], high_V[0]))  ## memberi range
    contours = cv.findContours(bnw.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2] ## untuk mendapatkan contoursnya


    cv.imshow('Camera', img_flip) ## Untuk display
    cv.imshow('Thresholds', bnw)

    if cv.waitKey(1) == 27: ## mengambil ascii character
        break

cam.release() ## release camera agar bisa dipakai untuk app lain
cv.destroyAllWindows() ## Mematikan semua window

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_red = np.array([92, 36, 49])
    high_red = np.array([158, 196, 108])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)

    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for cnt in contours :
        area = cv2.contourArea(cnt)
        if area > 30 :
            (x, y, w, h) = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0))
            break
        print(area)

    cv2.imshow("Frame", frame)
    cv2.imshow("RMask", red_mask)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

# import cv2
# import time
#
# if __name__ == '__main__':
#
#     # Start default camera
#     video = cv2.VideoCapture(0);
#
#     # Find OpenCV version
#     (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
#
#     # With webcam get(CV_CAP_PROP_FPS) does not work.
#     # Let's see for ourselves.
#
#     if int(major_ver) < 3:
#         fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
#         print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
#     else:
#         fps = video.get(cv2.CAP_PROP_FPS)
#         print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
#
#     # Number of frames to capture
#     num_frames = 120;
#
#     print("Capturing {0} frames".format(num_frames))
#
#     # Start time
#     start = time.time()
#
#     # Grab a few frames
#     for i in range(0, num_frames):
#         ret, frame = video.read()
#
#     # End time
#     end = time.time()
#
#     # Time elapsed
#     seconds = end - start
#     print("Time taken : {0} seconds".format(seconds))
#
#     # Calculate frames per second
#     fps = num_frames / seconds
#     print("Estimated frames per second : {0}".format(fps))
#
#     # Release video
#     video.release()