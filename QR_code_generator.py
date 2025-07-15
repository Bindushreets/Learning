import qrcode
import qrcode.constants

# Data you want to encode

data = "https://www.innovationmerge.com/"

# Create QR Code Instance

qr = qrcode.QRCode(
    version=1,                                              # Controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_H,      # High Error Correction
    box_size=10,                                            # Size of each box in pixels\
    border=4,                                               # Border in boxes (minimum is 4)
)

# Add Data to the QR code :

qr.add_data(data)
qr.make(fit=True)

# Create an Image :

img = qr.make_image(fill_color="black", back_color="white")

# Save the Image :

img.save("innovationmerge.png")

print("QR Code generated and saved as innovationmerge.png ")