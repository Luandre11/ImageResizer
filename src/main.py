from functions import Get_Image
from PIL import Image
import random

Image_Class = Get_Image()


def RandomNumbers():
        characters = random.choices(range(1, 100), k=3)
        return characters

def NewName(image):
       numbersString = ''.join(map(str, RandomNumbers()))
       return f"{numbersString}{image}"


def ModifyImage():
     if Image_Class.get_image():
        size1 = Image_Class.get_size()[0]
        size2 = Image_Class.get_size()[1]
        imagen = Image_Class.get_image()
        PillowImage = Image.open(f"images/{imagen}")
        ImageResized = PillowImage.resize((size1, size2), resample = Image.ANTIALIAS)
        ImageResized.save(f"newImages/{NewName(imagen)}")
        print("everything's done")
     else:
        print("something went wrong")


ModifyImage()





