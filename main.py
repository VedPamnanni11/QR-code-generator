import qrcode as qr

while True:

    url = qr.make(input("Enter a URL or text for a qr code : "))
    url.save(input("What do you want the file to be saved as?, and don't forget to add '.png' at the end : "))