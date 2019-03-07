# Untitled - By: Gehaha - 周四 3月 7 2019

# 笑脸识别历程
import sensor,time,image,os,nn
sensor.reset()
sensor.set_contrast(2)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)

#加载微笑检测网络
net = nn.load('/smile.network')

#load face haar cascade
face_cascade = image.HaarCascade("frontalface",stages = 25)
print(face_cascade)

#FPS clock
clock = time.clock()
while (True):
    clock.tick()

    # capture snapshot
    img = sensor.snapshot()

    # 识别人脸
    objects = img.find_features(face_cascade,threshold = 0.75,scale_factor = 1.25)
    #检测微笑
    for r in objects:
        # resize and center detection area
        r = [r[0]+10,r[1]+25,int(r[2]*0.70),int(r[2]*0.70)]
        img.draw_rectangle(r)
        out = net.forward(img,roi = r,softmax= True)
        img.draw_string(r[0], r[1], ':)' if (out[0] > 0.8) else ':(', color=(255), scale=2)
    print(clock.fps())
