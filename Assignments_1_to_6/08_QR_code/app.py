# QR code

# firstly install qr code module
# command: pip install qrcode

import qrcode

def generate_qr(data, filename="qrcode.png"):
    
    # Generates a QR code from the given data and saves it as an image file.

    # Parameters:
    # - data (str): The text or URL to encode in the QR code.
    # - filename (str): The name of the output image file (default: 'qrcode.png').
    
    try:
        # Create a QR code object
        qr = qrcode.QRCode(
            version=1,  # Size of the QR code (1-40, higher means bigger)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
            box_size=10,  # Size of each box in the QR grid
            border=4  # Border thickness
        )
        
        qr.add_data(data)  # Add data to the QR code
        qr.make(fit=True)  # Optimize the QR code size

        # Create and save the QR code image
        img = qr.make_image(fill="black", back_color="white")
        img.save(filename)
        print(f"\n✅ QR code generated successfully and saved as '{filename}'!\n")

    except Exception as e:
        print(f"\n❌ An error occurred: {e}\n")

def main():
    
    # Main function to take user input and generate a QR code.
    
    print("\n📌 QR Code Generator")
    print("=====================")
    
    data = input("\nEnter the text or URL to encode in QR code: ").strip()
    filename = input("Enter the filename to save (default: qrcode.png): ").strip()
    
    if not filename:
        filename = "qrcode.png"  # Default filename if not provided
    
    generate_qr(data, filename)

if __name__ == "__main__":
    main()
