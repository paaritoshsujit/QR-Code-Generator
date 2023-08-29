import qrcode
from PIL import Image

# Get the data from user
# data = input('Enter the URL of the QR to be created : ')
data = 'https://github.com/paaritoshsujit'

# Generate the QR Code for the data
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# Create the image of the QR
image = qr.make_image(fill='black', back_color='white')

# Save the image of the QR
image.save('qr_code.png')
Image.open('qr_code.png')