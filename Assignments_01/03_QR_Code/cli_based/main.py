from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("E:/Q3/assignment_4/Assignments_01/03_QR_Code/my_qrcode.png")

result = decode(img)
print(result)