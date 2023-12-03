import pytesseract as tess
from pdf2image import convert_from_path
from PIL import Image


#Donde esta instalado tesseract-ocr en el sistema
tess.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"


#Para pdf2image hay que especificar donde esta poppler si no es linux
img = convert_from_path("ej.pdf") #Aqui poner donde saca el pdf

text_file = open("./output/ej.txt", "w") #Aqui poner donde se guarda lo que transcribio

#Abre el pdf y lo guarda como imagen
for i in range(len(img)):
    img[i].save("./temp/" + str(i)+".jpg","JPEG")

    #Abre la imagen guardada y la transcribe
    temp = Image.open("./temp/" + str(i) +".jpg")
    content = tess.image_to_string(temp)
    print(content)
    text_file.write(content)

text_file.close()
