import os

from PIL import Image   

def abrir_image(ruta_img):
    imagen = Image.open(ruta_img)
    imagen.show()

ruta_relativa = "Lost Lamb.jpg"
ruta_absoluta = os.path.join(os.getcwd(), ruta_relativa)
abrir_image(ruta_absoluta)
