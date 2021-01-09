import PIL
from PIL import Image
import os 
import json


class Get_Image():
    def __init__(self):
        self.example = {"image": "test.png", "size_x": 100, "size_y": 100}
        self.path = "src\\"

        if os.path.isfile(f"src\\information.json"):
            with open("src\\information.json", "r") as f:
                self.example = json.load(f)
    
    def save(self):
       with open("src\\information.json", "w") as f:
           json.dump(self.example, f)
    
    
    def create_folder1(self): 
        if os.path.isdir("images") == False:
            try:
               os.mkdir("images")   
            except:
                print("something went wrong while making the directory")

            
    def get_image(self):
        with open("src\\information.json", "r") as f:
            data = json.load(f)
            image = data["image"]
            if image in os.listdir("images"):
                if image.endswith(".png")  or image.endswith (".jpg"):
                    return image
            
            

        
        
                
  


                    
    
     