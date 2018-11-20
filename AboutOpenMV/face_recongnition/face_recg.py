# Untitled - By: Gehaha - 周二 11月 20 2018

import sensor, image, pyb

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.B128X128)
sensor.set_windowing((92,112))
sensor.skip_frames(10)
sensor.skip_frames(time = 5000)

clock = time.clock()

#SUB = "S1"
NUM_SUBJECTS = 6 # 图像库中不同人数、一共六人
NUM_SUBJECTS = 20 # 每人有20张样本图片

#拍摄当前人
img = sensor.snapshot()
#img = img.Image("singtown/%s/1.pgm"%(SUB))
d0 = img.find_lbp((0,0.img.width(),img.height()))
#d0为当前人脸的lbp特征
img = None
pmin = 999999
num = 0
def min(pmin,a,s):
    global num
    if a < pmin:
        pmin = a
        num = s
     return pmin

for s in range(1,NUM_SUBJECTS +1):
    dist = 0
    for i in range(2,NUM_SUBJEXTS_IMGS+1):
        img= imgage.Image("singtown/s%d/%d.pgm"%(s, i))
        d1 = img.find_lbp((0,0,img.width(),img.height()))
        #d1 为第s文件夹中的第i张图片的lbp特征
        dist += image.match_descriptor(d0,d1)
    print("Average dist for subject %d: %d"%(s, dist/NUM_SUBJECTS_IMGS))
    pmin = min(pmin, dist/NUM_SUBJECTS_IMGS, s)#特征差异度越小，被检测人脸与此样本更相似更匹配。
    print(pmin)
print(num)

while(True):
    clock.tick()
    img = sensor.snapshot()
    print(clock.fps())
