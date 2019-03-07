# Untitled - By: Gehaha - 周四 3月 7 2019

import sensor, image, time,fir

#reset sensor
sensor.reset()

#set sensor settings
sensor.set_contrast(1)
sensor.set_brightness(0)
sensor.set_saturation(2)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)

#以下寄存器微调图像传感器窗口，使其与FIR传感器对齐
if (sensor.get_id()== sensor.OV7725):
    sensor.__write_reg(0xFF,0x01) #switch to reg bank
    sensor.__write_reg(0x17,0x19) #set HSTART
    sensor.__write_reg(0x18,0x43) #set HSTOP

#初始化热传感器
fir.init()
#FPS clock
clock = time.clock()

while (True):
    clock.tick()

    #capture on image
    image = sensor.snapshot()

    #capture FIR data
    # ta: Ambient temperature
    # ir: Object temperatures(IR array)
    # to_min: Minimum object temperature
    # to_max: Maximum object temperature

    ta,ir,to_min,to_max = fir.read_ir()

    #scale the image and belnd it with the framebuffer
    fir.draw_ir(image,ir)

    image.draw_string(0,0,"Ta:%0.2f"%ta,color =(0xFF,0x00,0x00))
    image.draw_string(0,8,"To min:%0.2f"%to_min,color =(0xFF,0x00,0x00))
    image.draw_string(0,16,"To max:%0.2f"%to_max,color =(0xFF,0x00,0x00))

    # print FPS
    print(clock.fps())


