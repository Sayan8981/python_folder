import os, pytesseract
from PIL import Image
#from pytesseract import pytesseract

class capture_text_from_images(object):
    
    def __init__(self) -> None:
        self.path_of_images = os.getcwd() + '/images/DarkPoster-lowres.png'
        
    def scrape_function(self):
        #import pdb;pdb.set_trace()
        self.img = Image.open(self.path_of_images)
        print (self.img)
        self.text = pytesseract.image_to_string(self.img)
        return self.text.split(',')
        
    def main(self):
        #import pdb;pdb.set_trace()
        print (self.scrape_function())


if __name__ == '__main__':
    capture_text_from_images().main()