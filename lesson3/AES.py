from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

plaintext = b'hello world!!!!!'

key = get_random_bytes(16)
# key = b'aaaaaaaaaaaaaaaa'

mode_dict = {
    'ECB': AES.MODE_ECB,
    'CTR': AES.MODE_CTR, 
    'CBC': AES.MODE_CBC
}

for mode_name, mode_flag in mode_dict.items():
    print(f'Working with mode: {mode_name}')
    enc = AES.new(key, mode_flag)
    dec = AES.new(key, mode_flag)

    for i in range(1,6):
        ciphertext = enc.encrypt(plaintext)
        print(f'{i}) ciphertext: {ciphertext}')
        decrypted_ciphertext = dec.decrypt(ciphertext)
    print('----------------------------------------------------')
    # print(f'{i}) decrypted_ciphertext: {decrypted_ciphertext}')