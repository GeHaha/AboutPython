# Untitled - By: Gehaha - 周二 3月 12 2019

import sensor, image, time
from pyb import UART
import json


yellow_threshold = (65,100,-10,6,24,51)


sensor.reset()

sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(10)
sensor.set_auto_whitebal(False)

clock = time.clock()
uart = UART(3,115200)

while(True):
    clock.tick()
    img = sensor.snapshot()
    blobs = img.find_blobs([yellow_threshold])
    if blobs:
        print('sum:',len(blobs))
        output_str = json.dumps(blobs)
        for b in blobs:
            #Draw a rect around the blob
            img.draw_rectangle(b.rect())
            img.draw_cross(b.cx(),b.cy())
        print('you send:',output_str)
        uart.write(output_str + '\n')
    else:
        print('not found!')

