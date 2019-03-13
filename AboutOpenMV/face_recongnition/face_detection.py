# Untitled - By: Gehaha - 周二 3月 12 2019

import sensor, image, time

sensor.reset()

sensor.set_contrast(1)
sensor.set_gainceiling(16)

sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QVGA)


# load haar cascade
face_cascade = image.HaarCascade("frontalface",stages = 25)

print(face_cascade)


clock = time.clock()

while(True):

    clock.tick()
    img = sensor.snapshot()
    objects = img.find_features(face_cascade,threshold = 1,scale = 1.35)


    for r in objects:
        img.draw_rectangle(r)

        print(clock.fps())


