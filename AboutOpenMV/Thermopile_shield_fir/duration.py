# Untitled - By: Gehaha - 周三 3月 13 2019

import pyb
import sensor,image,time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(10)
clock = time.clock()

while (True):
    clock.tick()
    img = sensor.snapshot()
    print(clock.fps())


    time_start = pyb.millis()

    duration = pyb.elapsed_millis(time_start)

