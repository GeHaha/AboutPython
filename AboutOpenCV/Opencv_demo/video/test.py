# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
cameraCapture = cv2.VideoCapture(0)

fps = 30

size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoWrite = cv2.VideoWriter(
        'MyOutputVid.avi',cv2.VideoWriter_fourcc('X','V','I','D'),
        fps,size)

success ,frame = cameraCapture.read()
numFramesRemaining = 10*fps -1
while success and numFramesRemaining > 0:
    videoWrite.write(frame)
    sucess ,frame = cameraCapture.read()
    numFramesRemaining -= 1
cameraCapture.release()

    