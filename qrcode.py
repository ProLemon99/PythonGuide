import os
import qrcode

output_folder = "qr_codes"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

img_input = input("Send a portal: ")
file_name = input("Enter a name for your QR code: ")

img = qrcode.make(img_input)
img_path = os.path.join(output_folder, f"{file_name}.png")
img.save(img_path, "PNG")

print(f"QR code saved as {img_path}!")