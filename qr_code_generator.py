import qrcode
from PIL import Image

def generate_colorful_qr_code():
    print("🎨 Colorful QR Code Generator 🎨")

    # Ask user for data
    data = input("Enter the text or URL to generate a colorful QR Code: ")

    # Ask user for colors
    fill = input("Choose a color for the QR (e.g., black, blue, red, green): ")
    back = input("Choose a background color (e.g., white, yellow, pink): ")

    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Make image with chosen colors
    img = qr.make_image(fill_color=fill, back_color=back)

    # Save image
    filename = "colorful_qr_code.png"
    img.save(filename)

    print(f"\n✅ Done! Your colorful QR Code is saved as '{filename}'")

    try:
        img.show()
    except:
        print("Can't show image, but it was saved.")

if __name__ == "__main__":
    generate_colorful_qr_code()
