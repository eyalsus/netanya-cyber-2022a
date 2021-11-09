from consts import ABC

def vigenere_cipher(message, key, mode=1):
    convered_str = ''
    for index, ch in enumerate(message.upper()):
        ch_index = ABC.index(ch)
        key_index = ABC.index(key[index % len(key)])
        convered_str += ABC[(ch_index + mode*key_index) % 26]
    return convered_str

def encrypt(message, key):
    return vigenere_cipher(message, key)

def decrypt(message, key):
    return vigenere_cipher(message, key, mode=-1)

key = 'ABRA'
plaintext = 'ABCDEFA'
ciphertext = encrypt(plaintext, key)
new_plaintext = decrypt(ciphertext, key)
if plaintext == new_plaintext:
    print(':)', plaintext, ciphertext)
else:
    print(':(', plaintext, ciphertext)
