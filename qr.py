import os
import qrcode

img = qrcode.make("https://github.com/Baha-Rtemi")
img.save("QR.png", "PNG")
os.system("start QR.png")