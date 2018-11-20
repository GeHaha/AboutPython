# Untitled - By: Gehaha - 周二 11月 20 2018

import sensor, image, pyb
RED_LED_PIN = 1
BLUE_LED_PIN = 3


sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.B128X128)
sensor.set_windowing((92,112))
sensor.skip_frames(10) # let new settings take affect
sensor.skip_frames(time = 2000)
num = 1 # 设置被拍摄者序号，第一个人的图片保存到s1文件夹中，第二个保存到说中，以此类推
n = 20
while(n):
    #红灯亮
    pyb.LED(RED_LED_PIN).on()
    sensor.skip_frames(time = 3000)

    #红灯灭，蓝灯亮
    pyb.LED(RED_LED_PIN).off()
    pyb.LED(BLUE_LED_PIN).on()

    # 保存截取的的图片到sd卡
    print(n)
    sensor.snapshot().save("singtown/s%s/%s.pgm" %(num,n))
    n -= 1
    pyb.LED(BLUE_LED_PIN).off()
    print("Done! Rest the camera to see the saved image")
