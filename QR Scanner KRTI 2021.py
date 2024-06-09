import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640) ##width
cap.set(4, 480) ##Height

while True:
    _, img = cap.read()

    for barcode in decode(img):
        (x, y, w, h) = barcode.rect

        if (x+w < 379 and y+h < 299 and x > 261 and y > 181 and 96 < w < 110 and 96 < h < 110):
            mydata = barcode.data.decode('utf-8')## turn into a string
            print(mydata)
            pts = np.array([barcode.polygon],np.int32)
            pts = pts.reshape((-1,1,2))
            cv2.polylines(img,[pts],True,(255,0,0),2)
            pts2 = barcode.rect
            cv2.putText(img,mydata,(pts2[0],pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 1)

    cv2.rectangle(img, (261, 181), (379, 299), (0, 0, 0), 2)
    cv2.imshow('Result', img)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()