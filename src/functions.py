import PIL
from PIL import Image
import os 
import json


#still a work in progress, class not needed so far

class Get_Image():
    """Class with the functionality to get the image and its sizes"""
    def __init__(self):
        pass

    @staticmethod      
    def get_image() -> str:
        accepted = ["jpg", "png", "jpeg"]  
        with open("src/information.json", "r") as f:
            data = json.load(f)
            image = data["image"]
            for i in accepted:
                if image.endswith(i):
                    return image

    @staticmethod
    def get_size() -> list:
        with open("src/information.json", "r") as f:
            data = json.load(f)
            size_y = data["size_y"]
            size_x = data["size_x"]
            if int(size_y) and int(size_x): 
                return [size_y, size_x]
           


                    
    
     
