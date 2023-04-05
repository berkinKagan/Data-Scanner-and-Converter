import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

print(pytesseract.image_to_string(Image.open("data11.jpeg"), lang = "tur"))

#with open("example.txt", "w") as f:
    #f.write(pytesseract.image_to_string(Image.open("data8.jpeg"), lang = "tur"))
for i in range(11,16):
        open((str(i) + "save.txt"), 'w+', encoding='utf-8').write(pytesseract.image_to_string(Image.open("data"+str(i)+".jpeg"), lang = "tur"))
    


