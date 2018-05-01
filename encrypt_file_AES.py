from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

file = open("_test.txt", "r")
data_str = file.read()
data = data_str.encode("latin-1")

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

file_out = open("encrypted_test.txt", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
