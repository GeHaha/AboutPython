# Untitled - By: Gehaha - 周三 3月 13 2019

import sensor,time

sensor.reset()
sensor.set_brightness(0)
sensor.set_saturation(3)
sensor.set_gainceiling(8)
sensor.set_contrast(2)

sensor.set_framesize(sensor.QVGA)
sensor.set_pixformat(sensor.RGB565)

#启用色条测试模式
sensor.set_colorbar(True)

#跳过几帧，让传感器稳定下来
for i in range(0,30):
    image = sensor.snapshot()

t = [lambda r,g,b: r < 70 and g < 70 and b < 70,
     lambda r, g, b: r < 70  and g < 70  and b > 200,  # Blue
     lambda r, g, b: r > 200 and g < 70  and b < 70,   # Red
     lambda r, g, b: r > 200 and g < 70  and b > 200,  # Purple
     lambda r, g, b: r < 70  and g > 200 and b < 70,   # Green
     lambda r, g, b: r < 70  and g > 200 and b > 200,  # Aqua
     lambda r, g, b: r > 200 and g > 200 and b < 70,   # Yellow
     lambda r, g, b: r > 200 and g > 200 and b > 200]  # White

# color bars are inverted for OV7725
if(sensor.get_id() == sensor.OV7725):
    t = t[::-1]

#320X240 image with 8 color bars each one is approx 40 pixel
#我们从帧缓冲区的中心开始，并且从每个彩条的中心平均10个采样像素的值
for i in range(0,8):
    avg = (0,0,0)
    idx = 40*i + 20
    for off in range(0,10):
        rgb = image.get_pixel(idx + off,120)
        avg = tuple(map(sum,zip(avg,rgb)))

    if not t[i](avg[0]/10 ,avg[1]/10,avg[2]/10):
        raise Exception("COLOR BARS TEST FAILED"
        "BAR#(%d): RGB(%d,%d,%d)" %(i+1,avg[0]/10,avg[1]/10,avg[2]/10))

print("COLOR BARS TEST PASSED....")


