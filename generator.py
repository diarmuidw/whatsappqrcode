from urllib.parse import urlencode
import qrcode
from PIL import Image

def create_whatsapp_url(phone_number, text):
    # Construct the parameters dictionary for URL encoding
    params = {'text': text}
    
    # URL encode the parameters
    encoded_params = urlencode(params)
    
    # Construct the WhatsApp URL
    whatsapp_url = f'https://wa.me/{phone_number}?{encoded_params}'
    
    return whatsapp_url

def generate_qr_code_with_logo(url, logo_path, filename='qrcode_with_logo.png'):
    # Create a QR code instance
    # Depending on the size of the logo, you may need to change the box_size

    qr = qrcode.QRCode(version=1, box_size=10, border=1)
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR code instance
    qr_code_img = qr.make_image(fill_color="black", back_color="white")
    
    # Open the logo image
    logo = Image.open(logo_path)
    
    # Calculate the position to center the logo on the QR code
    position = ((qr_code_img.size[0] - logo.size[0]) // 2, (qr_code_img.size[1] - logo.size[1]) // 2)
    
    # Paste the logo on the QR code
    qr_code_img.paste(logo, position, logo)
    
    # Save the image to a file
    qr_code_img.save(filename)
    
    return qr_code_img

def display_qr_code(image):
    image.show()

# Example usage:
phone_number = '1555123456'
text = 'sample text'
logo_path = '../data/logo.png'  # Replace with the path to your logo image file

whatsapp_url = create_whatsapp_url(phone_number, text)
print(f'WhatsApp URL: {whatsapp_url}')

# Generate QR code with logo
qr_code_with_logo_img = generate_qr_code_with_logo(whatsapp_url, logo_path, filename='whatsapp_qrcode_with_logo.png')
print('QR code with logo generated and saved as whatsapp_qrcode_with_logo.png')

# Display the QR code with logo
display_qr_code(qr_code_with_logo_img)
