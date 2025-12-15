from PIL import Image,ImageFilter,ImageDraw,ImageFont

img=Image.open("image.png")
img.show()

# f=img.transpose(Image.FLIP_LEFT_RIGHT)
# # f.show()

b=img.filter(ImageFilter.BLUR)
# b.show()