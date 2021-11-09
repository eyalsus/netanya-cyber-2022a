from consts import ABC

def caesar_cipher(message, key):
    convered_str = ''
    for ch in message.upper():
        ch_index = ABC.index(ch)
        new_ch_index =  (ch_index + key) % 26
        # convered_str = convered_str + ABC[new_ch_index]
        convered_str += ABC[new_ch_index]
    return convered_str

def encrypt(message, key):
    return caesar_cipher(message, key)

def decrypt(message, key):
    return caesar_cipher(message, key * -1)

key = 3
plaintext = 'ABCXYZ'
ciphertext = encrypt(plaintext, key)
new_plaintext = decrypt(ciphertext, key)
if plaintext == new_plaintext:
    print(':)', plaintext, ciphertext)
else:
    print(':(', plaintext, ciphertext)


