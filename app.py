# import module
from pdf2image import convert_from_path

# Store Pdf with convert_from_path function
images = convert_from_path('Lab 1.pdf',500,poppler_path=r'C:\Program Files\Release-22.04.0-0\poppler-22.04.0\Library\bin')

for i in range(len(images)):

	# Save pages as images in the pdf
	images[i].save('page'+ str(i) +'.jpg', 'JPEG')