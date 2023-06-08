# /Take a link, convert into qr and save in the device. 

import qrcode

link=input("Paste your link here: ")
name=input("Enter name of QR: ")
qr= qrcode.make(link)
qr.save(f"{name}.png")
