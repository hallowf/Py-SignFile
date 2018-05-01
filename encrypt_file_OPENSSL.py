import OpenSSL
from OpenSSL import crypto
import base64
key_file = open("C:\my.pem", "r")
key = key_file.read()
key_file.close()
password = "password of prk"

if key.startswith('-----BEGIN '):
    pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, key, password)
else:
    pkey = crypto.load_pkcs12(key, password).get_privatekey()
print pkey
data = "_test.txt"
sign = OpenSSL.crypto.sign(pkey, data, "sha256")
print sign

data_base64 = base64.b64encode(sign)
print data_base64
