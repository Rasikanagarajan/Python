from PIL import Image,ImageFilter,ImageDraw,ImageFont

img=Image.open("image.png")
# img.show()
r=img.rotate(45)
# r.show()

rs=img.resize((100,150))
# rs.show()

f=img.transpose(Image.FLIP_LEFT_RIGHT)
# f.show()

r.save("edit.png")

i=Image.new("RGB",(300,300),color="red")
draw=ImageDraw.Draw(i)
font=ImageFont.load_default()
draw.text((10,40),"hello",font=font,fill="black")
# i.show()

b=img.filter(ImageFilter.BLUR())
b.show()