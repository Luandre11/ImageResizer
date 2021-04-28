from functions import Get_Image
from PIL import Image
import random


def RandomNumbers() -> list:
    characters = random.choices(range(1, 100), k=3)
    return characters


def newName(image) -> str:
    numbersString = ''.join(map(str, RandomNumbers()))
    return f"{numbersString}{image}"


def ModifyImage():
    try:
        if Get_Image.get_image():
            size1 = Get_Image.get_size()[0]
            size2 = Get_Image.get_size()[1]
            imagen = Get_Image.get_image()
            PillowImage = Image.open(f"images/{imagen}")
            ImageResized = PillowImage.resize(
            (size1, size2), resample=Image.ANTIALIAS)
            ImageResized.save(f"newImages/{newName(imagen)}")
            print("everything done")
        else:
            raise Exception
    except Exception as exc:
        print(exc)


if __name__ == "__main__":
    ModifyImage()
