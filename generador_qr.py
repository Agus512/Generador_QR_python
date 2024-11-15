import qrcode
from PIL import Image

#Formato de QR
try:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    #Datos del QR
    qr.add_data('https://www.youtube.com/')
    qr.make(fit=True)

    #Crea imagen
    img = qr.make_image(fill='black', back_color='white')

    #Guarda la imagen
    img.save('C:/Users/admin/Desktop/img/codigo_qr.png') #Lugar donde quieras guardar la imagen
    print("El código QR se generó correctamente y se guardo en 'codigo_qr.png'.")

except Exception as e:
    print(f"error: {e}")
