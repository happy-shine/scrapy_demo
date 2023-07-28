import json

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64


def b(t):
    # 将UTF-8字符串转为字节串
    key = "EB444973714E4A40876CE66BE45D5930".encode('utf-8')
    iv = "B5A8904209931867".encode('utf-8')

    # 解码base64
    t = base64.b64decode(t)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext_padded = cipher.decrypt(t)
    plaintext = unpad(plaintext_padded, AES.block_size).decode('utf-8')

    return plaintext


with open("base64.txt", "r") as file:
    base64_ciphertext = file.read()

result = b(base64_ciphertext)
print(result)
