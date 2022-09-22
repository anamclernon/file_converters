from PIL import Image

image_path = "C:/Users/anamc/OneDrive/Pictures/Verordnung.jpg"
image_new_path = r'C:\Users\anamc\OneDrive\Documents\Health insurance\Physio_Verordnung.pdf'
image_1 = Image.open(image_path)
im_1 = image_1.convert('RGB')
im_1.save(image_new_path)

# hasnt been updating wtf