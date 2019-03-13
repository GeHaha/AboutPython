# Untitled - By: Gehaha - 周三 3月 13 2019

import sensor, image, time
import json
from pyb import UART

yellow_threshold = (46,100,-68,72,58,92)


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
        data = []
        for b in blobs:
            img.draw_rectangle(b.rect())
            img.draw_cross(b.cx(),b.cy())
            data.append(b.cx(),b.cy())

        data_out = json.dumps(set(data))
        uart.write(data_out + '\n')
        print('you send:',data_out)

    else:
        print('not found!')


