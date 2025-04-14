import qrcode

data = "AreNab"

# img = qrcode.make(data)

# img.save("E:/Q3/assignment_4/Assignments_01/03_QR_Code/my_qrcode.png")

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color = "pink", back_color = "white")

img.save("E:/Q3/assignment_4/Assignments_01/03_QR_Code/my_qrcode1.png")
