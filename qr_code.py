import qrcode as qrcode_default


text_for_qrcode = str(input("Qr Code text: "))

advance_option = str.lower(input("Enable advance option: (yes/no)"))
if advance_option == "yes" :
    border_size = int(input("Border size: "))
    fill_color= str.lower(input("Fill color: (red/green/blue/yellow etc)"))
    back_color= str.lower(input("Background color: (red/green/blue/yellow etc)"))
else:
    border_size = 2
    fill_color = "black"
    back_color = "white"


qrcode = qrcode_default.QRCode(border=2)
qrcode.add_data(text_for_qrcode)
qrcode.make(fit=True)
qrcode_image = qrcode.make_image(fill_color=fill_color,back_color=back_color)

file_title = text_for_qrcode[0:10].replace(" ","_")


qrcode_image.save(file_title + "_qr_code.png")
