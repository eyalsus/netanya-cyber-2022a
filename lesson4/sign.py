from Crypto.PublicKey import RSA
from Crypto.Signature import pss
from Crypto.Hash import SHA256

message = None
with open('secret2.txt', 'rb') as f:
    message = f.read()

with open('private_key.pem', 'rb') as f:
    private_key = RSA.import_key(f.read())
hash = SHA256.new(message)
print(f'hash: {hash.hexdigest()}')
signature = pss.new(private_key).sign(hash)
print(f'signature: {signature}')
with open('signature.dat', 'wb') as f:
    f.write(signature)
