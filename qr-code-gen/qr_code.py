import qrcode
from PIL import Image

# Data for the QR code
data = "https://drive.google.com/drive/folders/1kRcBNsbxi30Eb7IDfU5LTuvYvoquXmk4"

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,  # Size of each box in pixels
    border=4,  # Thickness of the border (in boxes)
)
qr.add_data(data)
qr.make(fit=True)


# Create the QR code image
qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGBA')

# Load the image to use as the overlay
overlay_image_path = "C:\\Users\\ayush\\C++\\cp_sucks\\CTF\\cultrang-logo.png" 
# Update this with your image path
overlay_image = Image.open(overlay_image_path).convert('RGBA')

# Resize overlay image to fit the QR code
qr_size = qr_image.size
overlay_image = overlay_image.resize(qr_size, Image.LANCZOS)

# Create a new image for the final output
final_image = Image.new('RGBA', qr_size, (255, 255, 255, 255))

# Replace black in the QR code with the overlay image
qr_pixels = qr_image.load()
overlay_pixels = overlay_image.load()
for y in range(qr_size[1]):
    for x in range(qr_size[0]):
        if qr_pixels[x, y] == (0, 0, 0, 255):  # Black color in RGBA
            final_image.putpixel((x, y), overlay_pixels[x, y])

# Save or show the final image
final_image.save("C:\\Users\\ayush\\C++\\cp_sucks\\CTF\\cultrang-qr.png")
final_image.show()