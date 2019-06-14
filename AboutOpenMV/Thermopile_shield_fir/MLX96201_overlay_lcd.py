# Untitled - By: Gehaha - 周一 5月 20 2019

# MLX90621 Overlay Demo
#
#此示例显示如何将热图叠加到openMV Cam的主摄像头实时视频输出上


import sensor, image, time, fir, lcd

ALT_OVERLAY = False # Set to True to allocate a second ir image.

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA2)
sensor.skip_frames(time = 2000)

# 初始化热传感器
fir.init(type=fir.FIR_MLX90621)

# Init the lcd.
lcd.init()

# 分配另一个帧缓冲区以获得更流畅的视频
extra_fb = sensor.alloc_extra_fb(sensor.width(), sensor.height(), sensor.RGB565)

# FPS clock
clock = time.clock()

while (True):
    clock.tick()

    # Capture an image
    img = sensor.snapshot()

    # Capture FIR data
    #   ta: 环境温度
    #   ir: 物体温度(IR阵列)
    #   to_min: 最低物体温度
    #   to_max: 最高物体温度
    ta, ir, to_min, to_max = fir.read_ir()

    if not ALT_OVERLAY:
        # 缩放图像并使用帧缓冲区进行贴图
        fir.draw_ir(img, ir)
    else:
        # 创建一个次映像，然后混合到帧缓冲区。
        extra_fb.clear()
        fir.draw_ir(extra_fb, ir, alpha=256)
        img.blend(extra_fb, alpha=128)

    # 绘制环境温度，最小和最高温度。
    img.draw_string(8, 0, "Ta: %0.2f C" % ta, color = (255, 0, 0), mono_space = False)
    img.draw_string(8, 8, "To min: %0.2f C" % to_min, color = (255, 0, 0), mono_space = False)
    img.draw_string(8, 16, "To max: %0.2f C"% to_max, color = (255, 0, 0), mono_space = False)

    lcd.display(img)
    # Force high quality streaming...
    img.compress(quality=90)
#   print(clock.fps())
