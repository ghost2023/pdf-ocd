from collections.abc import Buffer
import os
from PIL import Image
from PyPDF2 import PdfReader
import pytesseract

reader = PdfReader("./sosena.pdf")
names = []
dirname = os.path.dirname(__file__)

for page_index, page in enumerate(reader.pages):
    for image_file_object in page.images:
        name = "imgs/" + str(page_index) + image_file_object.name
        with open(name, "wb") as fp:
            fp.write(image_file_object.data)
            image = Image.open(name)
            txt = pytesseract.image_to_string(image,lang="amh")
            print(txt)
            print(
            "===================================================================="
            )

# for name in names: 
#     pass

