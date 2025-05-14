import qrcode

url = "https://example.com"

# Generate QR code
qr = qrcode.make(url)

# Save the image
qr.save("images/qr_code.png")

print("QR code generated and saved as qr_code.png")
