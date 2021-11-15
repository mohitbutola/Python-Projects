import qrcode #install "qrcode" module in your system using (pip install qrcode)

# install image module to use functions of Image in your projects using (pip install image)
img = qrcode.make('https://mohitbutola.000webhostapp.com/') #Specify the Text,Link,etc which you want to convert in aQR-Code

type(img)  # qrcode.image.pil.PilImage

img.save("My_Website_(qr_code_1.0).png")