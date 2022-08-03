from PIL import Image, ImageFilter

# before = Image.open("bridge.bmp")
# after = before.filter(ImageFilter.BoxBlur(10))
# after.save("out.bmp")

Image.open("bridge.bmp").filter(ImageFilter.BoxBlur(10)).save("bridge-out.bmp")