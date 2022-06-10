from traceback import print_tb
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
salt_word = input('Masukkan key:')
salt_byte = bytes(salt_word, 'utf-8')
print(salt_byte)
# print(salt_word)
password = 'jeki123'
key = PBKDF2(password, salt_byte, dkLen=32)
# print(key)

# #CBC enkrip
# from Crypto.Cipher import AES
# from Crypto.Util.Padding import pad

# output_file = 'file-enkripsi-AES-CBC.bin' # Output file
# data = b'Halo, ini percobaan aes' # Must be a bytes object
# new_key = key # The key you generated

# # Create cipher object and encrypt the data
# cipher = AES.new(new_key, AES.MODE_CBC) # Create a AES cipher object with the key using the mode CBC
# ciphered_data = cipher.encrypt(pad(data, AES.block_size)) # Pad the input data and then encrypt

# file_out = open(output_file, "wb") # Open file to write bytes
# file_out.write(cipher.iv) # Write the iv to the output file (will be required for decryption)
# file_out.write(ciphered_data) # Write the varying length ciphertext to the file (this is the encrypted data)
# file_out.close()

#CFB enkrip
from Crypto.Cipher import AES

output_file = 'file-enkripsi-AES.txt'
data = b'Halo, ini percobaan AES'

cipher = AES.new(key, AES.MODE_CFB) # CFB mode
ciphered_data = cipher.encrypt(data) # Only need to encrypt the data, no padding required for this mode

file_out = open(output_file, "wb")
file_out.write(cipher.iv)
file_out.write(ciphered_data)
file_out.close()

# #CFB dekrip
# from Crypto.Cipher import AES

# input_file = 'file-enkripsi-AES.txt'
# # key = b'YOUR KEY'

# file_in = open(input_file, 'rb')
# iv = file_in.read(16)
# ciphered_data = file_in.read()
# file_in.close()

# cipher = AES.new(new_key, AES.MODE_CFB, iv=iv)
# original_data = cipher.decrypt(ciphered_data) # No need to un-pad


# #store the file
# import json
# from base64 import b64encode, b64decode

# # These are placeholders for the values that we need to store to be read out later to decrypt. You may require other values than these like the tag or nonce
# ciphertext = b'...'
# iv = b'...'

# # Create the Python dictionary with the required data
# output_json = {
#     'ciphertext': b64encode(ciphertext).decode('utf-8'),
#     'iv': b64encode(iv).decode('utf-8')
# }

# # Save this dictionary to a JSON file
# with open('encrypted_file.json', 'w') as outfile:
#     json.dump(output_json, outfile)


# # Now to get all the data for decryption:
# with open('encrypted_file.json') as infile:
#     input_json = json.load(infile)

# # Get all the fields from the dictionary read from the JSON file
# ciphertext = input_json['ciphertext']
# iv = input_json['iv']