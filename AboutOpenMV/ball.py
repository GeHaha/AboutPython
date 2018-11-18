# Untitled - By: Gehaha - 周日 11月 18 2018

import sensor ,image,time

green_threshold = (0,80,-70,-10,-0,30)

#设置绿色的阈值，括号里面的数值分别是L A B 的最大值和最小值（minL, maxL, minA,
# maxA, minB, maxB），LAB的值在图像左侧三个坐标图中选取。如果是灰度图，则只需
#设置（min, max）两个数字即可。
sensor.reset()  # 初始化摄像头
sensor.set_pixformat(sensor.RGB565) #格式为RGB565
sensor.set_framesize(sensor.QQVGA) #使用qqvga速度快一些
sensor.skip_frames(time = 2000) #跳过2000s，使新设置生效，并且自动调节 白平衡
sensor.set_auto_whitebal(False)
clock = time.clock()  #追踪帧率

while(True):
    clock.tick()
    img = sensor.snapshot()
    blobs = img.find_blobs([green_threshold])

    if blobs:
        for b in blobs:
            img.draw_rectangle(b[0:4])
            img.draw_cross(b[5],b[6])
    print(clock.fps())
