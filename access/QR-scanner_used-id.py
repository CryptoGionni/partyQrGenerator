# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 17:44:27 2022

@author: gio
main source: https://towardsdatascience.com/build-your-own-barcode-and-qrcode-scanner-using-python-8b46971e719e
checking used id: https://www.youtube.com/watch?v=IOhZqmSrjlE

"""

import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time

used_barcodes = []

def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)

    for obj in barcode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
        
        cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
        
        if barcodeData not in used_barcodes:
            print("ok, entra")
            used_barcodes.append(barcodeData)
            time.sleep(3)
        elif barcodeData in used_barcodes:
            print("già usato")
            time.sleep(3)
        else:
            pass
            #print("Barcode: "+barcodeData +" | Type: "+barcodeType)

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    decoder(frame)
    cv2.imshow('Image', frame)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break