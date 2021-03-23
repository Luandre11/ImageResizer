import PIL
from PIL import Image
import os 
import json


class Get_Image():
    def __init__(self):
        self.example = {"image": "test.png", "size_x": 500, "size_y": 500}

        if os.path.isfile(f"src/information.json"):
            with open("src/information.json", "r") as f:
                self.example = json.load(f)
    
    def save(self):
       with open("src/information.json", "w") as f:
           json.dump(self.example, f)
    
            
    def get_image(self):
        accepted = ["jpg", "png", "jpeg"]
        with open("src/information.json", "r") as f:
            data = json.load(f)
            image = data["image"]
            for i in accepted:
                if image.endswith(i):
                    return image


    def get_size(self):
        with open("src/information.json", "r") as f:
            data = json.load(f)
            size_y = data["size_y"]
            size_x = data["size_x"]
            if int(size_y) and int(size_x): 
                return [size_y, size_x]
            else:
                print("the size_x and size_y must be int types")





        
        
                
  


                    
    
     