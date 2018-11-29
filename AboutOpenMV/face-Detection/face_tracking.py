# Untitled - By: Gehaha - 周四 11月 29 2018

import sensor, image, time

#Reset sensor

sensor.reset()
sensor.set_contrast(3)
sensor.set_gainceiling(16)
sensor.set_framesize(sensor.VGA)

sensor.set_pixformat(sensor.GRAYSCALE)
sensor.skip_frames(time = 2000)

# Load Haar Cascade
# 默认情况下，这将使用所有阶段，较低的阶段更快但不太准确。
face_cascade = image.HaarCascade('FRONTALFACE',stages = 25)
print(face_cascade)

kpts1 = None

while(kpts1 == None):
    img = sensor.snapshot()
    img.draw_string(0,0,"Looking for a face....")
    # Find faces
    objects = img.find_features(face_cascade,threshold = 0.5,scale = 1.25)
    if objects:
        #在每个方向上将ROI扩大31个像素
        face = (objects[0][0]-31,objects[0][-1]-31,objects[0][2]+31*2,objects[0][3]+31*2)
        #使用检测面大小作为ROI提取关键点
        kpts1 = img.find_keypoints(threshold = 10,scale_factor = 1.1 ,max_keypoints= 100,roi= face)
        # Draw a rectangle around the first face
        img.draw_rectangle(objects[0])

    #Draw keypoints
    print(kpts1)
    img.draw_keypoints(kpts,size = 24)
    img = sensor.snapshot()
    time.sleep(2000)

    #FPS clock
    clock = time.clock()

    while(True):
        clock.tick()
        img = sensor.snapshot()
        #从整个帧中提取关键点
        kpts2 = img.find_keypoints(threshold = 10,scale_factor = 1.1,max_keypoints =100,normalized = True)

        if(kpts2):
            #将第一组关键点于第二组关键点匹配
            c = image.match_descriptor(kpts1,kpts2,threshold = 85)
            match = c[6]
            if (match > 5):
                img.draw_rectangle(c[2:6])
                img.draw_cross(c[],c[],size = 10)
                print(kpts2,"matched:%d dt:%d"(match,c[7]))
            img.draw_string(0,0,"FPS:%.2f"%(clock.fps()))
