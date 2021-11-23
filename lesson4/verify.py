from Crypto.PublicKey import RSA
from Crypto.Signature import pss
from Crypto.Hash import SHA256

message = None
with open('secret2.txt', 'rb') as f:
    message = f.read()

with open('public_key.pem', 'rb') as f:
    public_key = RSA.import_key(f.read())

with open('signature.dat', 'rb') as f:
    known_signature = f.read()

hash = SHA256.new(message)
verifier = pss.new(public_key)
try:
    verifier.verify(hash, known_signature)
    print("The signature is authentic.")
except (ValueError, TypeError):
    print("The signature is not authentic.")

