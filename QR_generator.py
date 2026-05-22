import qrcode

# Data to store in QR code

data = input(" Enter text or URl : ")

# Create QR code

qr = qrcode.QRCode(
    version = 1,
    box_size = 10,
    border = 5
)
qr.add_data(data)
qr.make(fit = True)

# Generate Image

img = qr.make_image(fill_color = "black" , back_color = "white")

#Save Iamge

file_name = "qrcode.png"
img.save(file_name)
print(f"QR code saved as {file_name}")