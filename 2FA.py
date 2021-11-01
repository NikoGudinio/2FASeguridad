import pyotp
import qrcode

clave = pyotp.random_base32()
print("Clave:", clave)

totp_object = pyotp.TOTP(clave)

#Se realiza la Autenticacion por medio de otp utilizando el algoritmo de totp

qr_text = totp_object.provisioning_uri(name="2FA", issuer_name="Seguridad")
print(qr_text)

#Genera un QR
img = qrcode.make(qr_text)
f = open("output.png", "wb")
img.save(f)
f.close()

#Validar con el Google Authenticator ingresando el codigo que te genera
otp = input("ingresar el OTP: ")
validar = totp_object.verify(otp)
print(validar)