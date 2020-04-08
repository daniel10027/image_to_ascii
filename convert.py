from PIL import Image
import sys

greyscale = list(" -.':rLIVRQ")
#greyscale = list(" -.':rLIVXRMWQ@") 
#greyscale = list(" .,~:;irsXA253hMHGS#9B&@")

if len(sys.argv) != 4:
    print("Utilisation: ./convert.py <image_file> <max_height> <character_width_to_height_ratio> Make it better")
    sys.exit()
f, h, r = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])

img = Image.open(f)
img = img.convert("L") #convertion en Gry

(x,y) = img.size
newsize = (int(x/y*h*r), h) #la longueur  est r*height, l'aspect ration de l'image est conservé 
img = img.resize(newsize, Image.ANTIALIAS)

str = ""
for y in range(img.size[1]):
    for x in range(img.size[0]):
        lum = 255-img.getpixel((x,y))
        str += greyscale[(lum//24)] #24 pixels ton de rang
    str += "\n"

f = open((f.split(".")[0] + ".txt"), "w")
f.write(str)
f.close()
