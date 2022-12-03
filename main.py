import pyotp
import qrcode
key = 'lmouuudkey'
totp = pyotp.TOTP(key)
uri = pyotp.totp.TOTP(key).provisioning_uri(name='user', issuer_name='Lmouuud')
qrcode.make(uri).save("qr.png")
while True:
    print(totp.verify(input('code :')))

