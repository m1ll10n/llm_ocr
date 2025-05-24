import easyocr
from PIL import Image
import base64

# import input

# convert input (base64 or pdf) to image
image_decode = base64.b64decode()

# read image and extract data with easyocr
reader = easyocr.Reader(["en"])
result = reader.readtext("../sample_input/base64.txt")

print(result)
