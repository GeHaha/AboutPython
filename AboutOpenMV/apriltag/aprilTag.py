# Untitled - By: Gehaha - 周二 11月 20 2018

import sensor ,image,time,math
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(30)
sensor.set_auto_gain(False)  #must turn this off to prenvent image washout
sensor.set_auto_whitebal(False)
clock = time.clock()

while (True):
        clock.tick()
        img = sensor.snapshot()
        for tag in img.find_apriltags():   # defaults to TAG36H11 without "families"
             img.draw_rectangle(tag.rect(),color = (255,0,0))
             img.draw_cross(tag.cx(),tag.cy(),color = (0,255,0))
             degrees = 180 * tag.rotation() /math.pi
             print(tag.id(),degrees)
