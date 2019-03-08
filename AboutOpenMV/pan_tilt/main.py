# Untitled - By: Gehaha - 周五 3月 8 2019

import sensor ,image,time

from pid import PID
from pyb import Servo

pan_servo = Servo(1)
tilt_servo = Servo(2)

red_threshold = (13,49,18,61,6,47)

pan_pid = PID(P = 0.07,i= 0,imax = 90) #脱机运行或者图像传输，使用这个pid
tilt_pid = PID(p = 0.05,i = 0,imax = 90) #脱机运行或者禁用图像传输，使用这个PID


# initialize the camera sensor
sensor.reset()
sensor.set_contrast(1)
sensor.set_gainceiling(16)

#use RGB565
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QQQVGA)
sensor.set_vflip(True)

sensor.skip_frames(10)
sensor.set_auto_whitebal(False)
clock = time.clock()


face_cascade = image.HaarCascade("frontalface", stages=25)

def find_max(blods):
    max_size = 0
    for blod in blods:
        if blod[2]*blod[3] > max_size:
            max_blod = blod
            max_size = blod[2]*blod[3]
    return max_blod


while(True):
    clock.tick()
    img = sensor.snapshot()


    blods = img.find_features(face_cascade, threshold=0.75, scale=1.35)
    if blods:
        max_blod = find_max(blobs)
        pan_error = max_blob[0]+max _blob[2]/2- img.width()/2
        tilt_error = max_blob[1]+max _blob[3]/2 - img.height()/2

        print("pan_error:",pan_error)

        img.draw_rectangle(max_blob)
        img.draw_cross(int(max_blob[0]+max _blob[2]/2,max_blob[1])+int(max _blob[3]/2()))

        pan_output = pan_pid.get_pid(pan_error,1)/2
        tilt_output = tilt_pid.get_pid(tilt_error,1)

        print("pan_output",pan_output)
        pan_servo.angle(pan_servo.angle() + pan_output)
        tilt_servo.angle(tilt_servo.angle()-tilt_output)
