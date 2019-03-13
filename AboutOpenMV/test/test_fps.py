# Untitled - By: Gehaha - 周三 3月 13 2019

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.set_colorbar(True)



clock = time.clock()

for i in range(0,600):
    clock.tick()
    sensor.snapshot()

print("FPS:" ,clock.fps())
