def  xor_encrypt(inText, key):
    outText = ""

    for x in range(0, len(inText)):
        outText += chr(ord(inText[x]) ^ ord(key[x % len(key)]))

    return outText

key = "qw8J"
data = {"showpassword":"yes","bgcolor":"#ffffff"}

import json
data = json.dumps(data)
print(data)
data = xor_encrypt(data, key)
print(data)
import base64
data = base64.b64encode(data.encode())
print(data)

data = base64.b64decode(data)
print(data)
data = xor_encrypt(data.decode(), key)
print(data)
data = json.loads(data)
print(data['showpassword'])
print(data['bgcolor'])
