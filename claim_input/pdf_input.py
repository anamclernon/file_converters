import typing
from PIL import Image
from pytesseract import pytesseract


def get_text_from_pdf(path_to_tesseract: str, path_to_image: str) -> list:
    #Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = path_to_tesseract

    #Open image with PIL
    img = Image.open(path_to_image)
    #Extract text from image
    text = pytesseract.image_to_string(img)

    return text.split()

# get text as separate words


