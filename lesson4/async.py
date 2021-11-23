from Crypto import PublicKey
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

with open('secret.txt', 'rb') as fp:
    h = SHA256.new()
    h.update(fp.read())
    print(h.hexdigest())


key = RSA.generate(2048)
with open('private_key.pem','wb') as f:
    f.write(key.export_key('PEM'))
public_key = key.publickey()
with open('public_key.pem','wb') as f:
    f.write(public_key.export_key('PEM'))

# key.public_key

f.close()
