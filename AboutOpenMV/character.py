# Untitled - By: Gehaha - 周日 11月 25 2018

import sensor, image, time

sensor.reset()

#sensor settings
sensor.set_contrast(3)
sensor.set_gainceiling(16)
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.VGA)
sensor.set_windowing((320,240))

sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False,value = 100)

#画出特征点

def draw_keypoints(img,kpts):
    if kpts:
        print(kpts)
        img.draw_keypoints(kpts)
        img = sensor.snapshot()
        time.sleep(1000)

kpts1 = None
#kpts1保存目标物体的特征，可以从文件导入特征，但是不建议这么做。
#kpts1 = image.load_descriptor("/desc.orb")
#img = sensor.snapshot()
#draw_keypoints(img, kpts1)
clock = time.clock()
while(True):
    clock.tick()
    img = sensor.snapshot()
    if (kpts1 == None):
        kpts1 = img.find_keypoints(max_keypoints =150,threshold = 10,scale_factor = 1.2)
        draw_keypoints(img,kpts1)

    else:
        kpts2 = img.find_keypoints(max_keypoints = 150,threshold = 10,normalized = True)
        if (kpts2):
            match = image.match_descriptor(kpts1,kpts2,threshold = 85)


            if (match.count() >10):
                img.draw_rectangle(match.rect())
                img.draw_cross(match.cx(),match.cy(),size = 10)

            print(kpts2,"matched:%d dt:%d" %(match.count(),match.theta()))

    img.draw_string(0,0,"FPS:%.2f"%(clock.fps()))

