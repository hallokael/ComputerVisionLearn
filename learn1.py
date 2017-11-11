from PIL import Image
from pylab import *
# 读取图像到数组中
from numpy import *
im = array(Image.open('empire.jpg'))
im2 = 255 - im #  对图像进行反相处理
im3 = (100.0/255) * im + 100 # 将图像像素值变换到 100...200 区间
im4 = 255.0 * (im/255.0)**2 # 对图像像素值求平方后得到的图像
im5 = 1.0*im
pil_im = Image.fromarray(uint8(im5))
#浮点运算破坏了im5的数据类型，导致乘以1.0后反相

# 新建一个图像
a=figure()
l1=a.add_subplot(221)
l2=a.add_subplot(222)
l3=a.add_subplot(223)
l4=a.add_subplot(224)# 不使用颜色信息
l1.imshow(im3)
l2.imshow(im5)
l3.imshow(im4)
l4.imshow(pil_im)
#gray()
# 在原点的左上角显示轮廓图像
#contour(im3, origin='image')
show()