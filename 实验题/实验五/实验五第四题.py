from PIL import Image
from PIL import ImageFilter 
from PIL import ImageEnhance 
im= Image.open("实验5图片.jpg")
im1=im.resize((350,350))
im2=im1.rotate(90)
im3=im2.filter(ImageFilter.CONTOUR)
om=ImageEnhance.Contrast(im3)
om.enhance(20).save("实验图片5修改.jpg")
