# Untitled - By: Gehaha - 周一 5月 20 2019

import sensor, image, time,math


# 颜色跟踪阈值(灰度最小，灰度最大值)
threshold_list = [(200,255)]

# 设置目标温度范围
min_temp_in_celsius = 20.0
max_temp_in_celsius = 35.0
print("resetting lepton....")



sensor.reset()
sensor.ioctl(sensor.IOCTL_LEPTON_SET_MEASUREMENT_MODE,True)
sensor.ioctl(sensor.IOCTL_LEPTON_SET_MEASUREMENT_RANGE,min_temp_in_celsius,max_temp_in_celsius)
print("Lepton Res (%dx%d)" % (sensor.ioctl(sensor.IOCTL_LEPTON_GET_WIDTH),
                              sensor.ioctl(sensor.IOCTL_LEPTON_GET_HEIGHT)))
print("Radiometry Available: " + ("Yes" if sensor.ioctl(sensor.IOCTL_LEPTON_GET_RADIOMETRY) else "No"))


sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 5000)
clock = time.clock()

#只有像素大于“pixel_threshold”且面积大于“area_threshold”的blod才会被下面的“find_blobs”返回
#如果更改相机分辨率，请更改“pixels_threshold”和“area_threshold”。
# “merge = True”合并图像中的所有重叠blob。
def map_g_to_temp(g):
    return ((g * (max_temp_in_celsius - min_temp_in_celsius)) / 255.0) + min_temp_in_celsius

while(True):
    clock.tick()
    img = sensor.snapshot()
    for blob in img.find_blobs(threshold_list, pixels_threshold=200, area_threshold=200, merge=True):
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(),blob.cy())
        stats = img.get_statistics(threshold = threshold_list,roi = blob.rect())
        img.draw_string(blob.x(),blob.y()-10,"%.2f C" % map_g_to_temp(stats.mean()), mono_space=False)
    print("FPS %f - Lepton Temp: %f C" % (clock.fps(), sensor.ioctl(sensor.IOCTL_LEPTON_GET_FPA_TEMPERATURE)))
