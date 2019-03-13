# Untitled - By: Gehaha - 周四 3月 7 2019

import sensor, image, time,fir ,lcd

#rest sensor
sensor.reset()
#set sensor settings
sensor.set_contrast(1)
sensor.set_brightness(0)
sensor.set_saturation(2)
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)

# 以下寄存器微调图像传感器窗口，使其与fir传感器对齐
if (sensor.get_id() == sensor.OV2640):
    sensor.__write_reg(0xFF,0X01) # switch to the reg bank
    sensor.__write_reg(0x17,0x19) # set HSTART
    sensor.__write_reg(0x18,0x43) # set HSTOP

# Initialize the thermal sensor
fir.init()
# Initialize the thermal sensor
lcd.init()

#fps clock
clock = time.clock()

while(True):
    clock.tick()

    # Capture an image
    image = sensor.snapshot()

    ta, ir, to_min, to_max = fir.read_ir()

    # Draw IR data on the framebuffer
    fir.draw_ir(image, ir)

    # Draw ambient, min and max temperatures.
    image.draw_string(0, 0, "Ta: %0.2f"%ta, color = (0xFF, 0x00, 0x00))
    image.draw_string(0, 8, "To min: %0.2f"%to_min, color = (0xFF, 0x00, 0x00))
    image.draw_string(0, 16, "To max: %0.2f"%to_max, color = (0xFF, 0x00, 0x00))




    #display image on LCD
    lcd.display(image)
    #print FPS
    print(clock.fps())
