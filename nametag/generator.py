import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf", 25)
img = Image.new("RGBA", (200,200), (120,20,20))
draw = ImageDraw.Draw(img)
draw.text((0,0), "abcdefghijklmnopQRSTUVWXYZ", (255,255,0), font=font)
img.save("test.png")