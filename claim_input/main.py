#date signed and postal code doesnt work
# and do outpatient no, maybe try make it work for multiple images
from pdf_input import get_text_from_pdf
from data_into_variables import get_data_from_text
from fill_pdfs import fill_pdf

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract"

path_to_image = r"C:\Users\anamc\OneDrive\Documents\Health insurance\Claims\To_be_claimed\bill.jpg"

filename = r"C:\Users\anamc\OneDrive\Documents\Health insurance\template_claim.pdf"

#change this everytime
new_filename = r"C:\Users\anamc\OneDrive\Documents\Health insurance\Auto_claimform.pdf" 

text = get_text_from_pdf(path_to_tesseract, path_to_image)

info = get_data_from_text(text) #execute only this to get what data will be inputed

fill_pdf(info, filename, new_filename)


