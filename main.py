import os
import sys
from PIL import Image
import pyfiglet
import PIL

banner = pyfiglet.figlet_format("Kompresor IMG")
print(banner)
print("""1.Umieść plik main.py w folderze ze zdjęciami.
2.Uruchom program przez CMD.(python main.py)
3.Zdjęcia znajdują sie w folderze Kompresja.""")
print("Made by NiC0d3m V0.1")
print("\n")

os.makedirs("Kompresja")
def Kompres(file, verbose = True):
    filepath = os.path.join(os.getcwd(), file)

    cd = os.getcwd()
    
    picture = Image.open(filepath)

    os.chdir('.\Kompresja')

    picture.save(file,"JPEG", optimize = True , quality=20) # <---- Zmiana wielkosci zdjecia

    os.chdir("..")

    return

def main():

 
    verbose = True

    cwd= os.getcwd()

    formats = ('.jpg', ',jpeg')

    for file in os.listdir(cwd):

        if os.path.splitext(file)[1].lower() in formats:
            print("Kompresja",file)
            Kompres(file, verbose)
        
    print("Zakonczono")

if __name__ == "__main__":
    main()