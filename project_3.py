3. #QR Code Generator
import qrcode
data = "https://www.youtube.com/watch?v=NyTkaQHdySM&list=RDNyTkaQHdySM&start_radio=1"
qr = qrcode.make(data)
qr.save("qrcode.png")

