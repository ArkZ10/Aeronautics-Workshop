import cv2
import numpy as np

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
servo1 = 0
servo2 = 0
servo3 = 0
servo4 = 0
fps1 = 0
fps2 = 0
fps3 = 0
fps4 = 0
red = (0, 0, 255)
blue = (255, 0, 0)
green = (0, 255, 0)
purple = (255, 87, 170)


def rectangle(servo, fps, cnt, color):
    area = cv2.contourArea(cnt)
    (x, y, w, h) = cv2.boundingRect(cnt)
    if area > 10:
        if 330 > x > 270 and 250 > y > 190:
        # if (x,y) == pixel_center :
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            if servo == 0:
                fps += 1
                seconds = int(fps / 28)
                print(seconds)
                if fps == 300:
                    servo += 1


def find_mask(masks, servo, fps, color):
    contours, _ = cv2.findContours(masks, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    for cnt in contours:
        rectangle(servo, fps, cnt, color)
        break


while True:
    _, cap = cam.read()
    frame = cv2.flip(cap, 1)
    height, width, _ = frame.shape
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    x_axis = int(width/2)
    y_axis = int(height/2)
    pixel_center = hsv_frame[y_axis, x_axis]
    hue_value = pixel_center[0]
    cv2.circle(frame, (x_axis, y_axis), 5, (0, 0, 0), 2)


    # lower mask (0-10)
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([5, 255, 255])
    mask0 = cv2.inRange(hsv_frame, lower_red, upper_red)
    # upper mask (170-180)
    lower_red = np.array([172, 120, 50])
    upper_red = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv_frame, lower_red, upper_red)
    # join my masks
    red_mask = mask0 + mask1

    # green color
    low_green = np.array([51, 87, 0])
    high_green = np.array([65, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)  # Color range

    # blue color
    low_blue = np.array([88, 128, 0])
    high_blue = np.array([132, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)  # Color range

    # purple color
    low_purple = np.array([23, 85, 199])
    high_purple = np.array([36, 151, 255])
    purple_mask = cv2.inRange(hsv_frame, low_purple, high_purple)  # Color range

    find_mask(red_mask, servo1, fps1, red)
    find_mask(green_mask, servo2, fps2, green)
    find_mask(blue_mask, servo3, fps3, blue)
    find_mask(purple_mask, servo4, fps4, purple)

    # cv2.rectangle(frame, (280, 200), (360, 280), (0, 0, 0), 2)
    cv2.rectangle(frame, (310, 230), (330, 250), (0, 0, 0), 2)
    cv2.imshow("Frame", frame)
    # cv2.imshow("RMask", mask)
    # cv2.imshow("gMask", green_mask)
    # cv2.imshow("bMask", blue_mask)
    # cv2.imshow("PMask", purple_mask)

    # Servo Movement
    if servo1 == 1:
        print('servo 1 (merah) gerak "harusnya"')
        servo1 += 1

    if servo2 == 1:
        print('servo 2 (Hijau) gerak "harusnya')
        servo2 += 1

    if servo3 == 1:
        print('servo 3 (Biru) gerak "harusnya')
        servo3 += 1

    if servo4 == 1:
        print('servo 4 (Ungu) gerak "harusnya')
        servo4 += 1

    key = cv2.waitKey(1)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()


# import cv2
# import numpy as np
#
# cam = cv2.VideoCapture(0)
# servo1 = 0
# servo2 = 0
# servo3 = 0
# servo4 = 0
# fps1 = 0
# fps2 = 0
# fps3 = 0
# fps4 = 0
#
# while True:
#     _, cap = cam.read()
#     frame = cv2.flip(cap, 1)
#     hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#     # red color
#     # low_red = np.array([0, 213, 0])
#     # high_red = np.array([92, 255, 255])
#     # red_mask = cv2.inRange(hsv_frame, low_red, high_red) #Color range
#     # lower mask (0-10)
#     lower_red = np.array([0, 50, 50])
#     upper_red = np.array([5, 255, 255])
#     mask0 = cv2.inRange(hsv_frame, lower_red, upper_red)
#     # upper mask (170-180)
#     lower_red = np.array([172, 120, 50])
#     upper_red = np.array([180, 255, 255])
#     mask1 = cv2.inRange(hsv_frame, lower_red, upper_red)
#     # join my masks
#     mask = mask0 + mask1
#
#     # green color
#     low_green = np.array([45, 60, 168])
#     high_green = np.array([87, 255, 255])
#     green_mask = cv2.inRange(hsv_frame, low_green, high_green)  # Color range
#
#     # blue color
#     low_blue = np.array([88, 128, 0])
#     high_blue = np.array([132, 255, 255])
#     blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)  # Color range
#
#     # purple color
#     low_purple = np.array([23, 85, 199])
#     high_purple = np.array([36, 151, 255])
#     purple_mask = cv2.inRange(hsv_frame, low_purple, high_purple)  # Color range
#
#     contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#     contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         (x, y, w, h) = cv2.boundingRect(cnt)
#         if area > 10:
#             if (x < 330 and y < 250 and x > 270 and y > 190 ):
#                 cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
#                 if servo1 == 0:
#                     fps1 += 1
#                     detik = int(fps1/28)
#                     print(detik)
#                     if fps1 == 300:
#                         servo1 += 1
#                     break
#                 break
#             break
#
#     contours, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#     contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         (x, y, w, h) = cv2.boundingRect(cnt)
#         if area > 10:
#             if (x < 330 and y < 250 and x > 270 and y > 190 ):
#                 cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#                 if servo2 == 0:
#                     fps2 += 1
#                     detik = int(fps2/ 28)
#                     print(detik)
#                     if fps2 == 300:
#                         servo2 += 1
#                     break
#                 break
#             break
#
#     contours, _ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#     contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
#     for cnt in contours :
#         area = cv2.contourArea(cnt)
#         (x, y, w, h) = cv2.boundingRect(cnt)
#         if area > 10:
#             if (x < 330 and y < 250 and x > 270 and y > 190 ):
#                 cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
#                 if servo3 == 0:
#                     fps3 += 1
#                     detik = int(fps3 / 28)
#                     print(detik)
#                     if fps3 == 300:
#                         servo3 += 1
#                     break
#                 break
#             break
#
#     contours, _ = cv2.findContours(purple_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#     contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         (x, y, w, h) = cv2.boundingRect(cnt)
#         if area > 10:
#             if (x < 330 and y < 250 and x > 270 and y > 190 ):
#                 cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 87, 170), 2)
#                 if servo4 == 0:
#                     fps4 += 1
#                     detik = int(fps4 / 28)
#                     print(detik)
#                     if fps4 == 300:
#                         servo4 += 1
#                     break
#                 break
#             break
#
#     # cv2.rectangle(frame, (280, 200), (360, 280), (0, 0, 0), 2)
#     cv2.rectangle(frame, (310, 230), (330, 250), (0, 0, 0), 2)
#     cv2.imshow("Frame", frame)
#     # cv2.imshow("RMask", mask)
#     # cv2.imshow("gMask", green_mask)
#     cv2.imshow("bMask", blue_mask)
#     # cv2.imshow("PMask", purple_mask)
#
#     #Servo Movement
#     if servo1 == 1 :
#         print('servo 1 (merah) gerak "harusnya"')
#         servo1 += 1
#
#     if servo2 == 1:
#         print('servo 2 (Hijau) gerak "harusnya')
#         servo2 += 1
#
#     if servo3 == 1:
#         print('servo 3 (Biru) gerak "harusnya')
#         servo3 += 1
#
#     if servo4 == 1:
#         print('servo 4 (Ungu) gerak "harusnya')
#         servo4 += 1
#
#     key = cv2.waitKey(1)
#     if key == 27:
#         break
# cam.release()
# cv2.destroyAllWindows()
