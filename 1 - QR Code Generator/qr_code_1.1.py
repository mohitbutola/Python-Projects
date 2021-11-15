import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,) #Changing Box and Border of QR code 

qr.add_data("https://mohitbutola.000webhostapp.com/")
qr.make(fit=True) #If data exit then create a QR code

img = qr.make_image(fill_color="black",back_color="green") # changing The Colour code of QRcode

img.save("My_Website_(qr_code_1.1).png") #Saving the QR code in the given Formate
