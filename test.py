from PIL import Image
import pytesseract

img = Image.open("single_column_text.png")
#left, top, right, bottom = 15, 60, 80, 5
print(img)

box = tuple()
box= (0, 0, 147, 122)


img2 = img.crop(box)

print(img2)
img2.save("cropped.png")