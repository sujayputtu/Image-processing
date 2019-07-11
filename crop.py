from PIL import Image
img = Image.open("single_column_text.png")
area = (40, 100, 40, 100)
cropped_img = img.crop(area)
cropped_img.show()