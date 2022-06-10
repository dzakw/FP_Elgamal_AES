#CBC dekrip
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

input_file = 'file-enkripsi-AES-CBC.bin' # Input file
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import elgamal
# salt_word = b'inisaltnya'
salt = input('Masukkan key:')

salt_byte = bytes(salt, 'utf-8')
# print(salt_byte)
# print(salt_word)
password = 'jeki123'
key = PBKDF2(password, salt_byte, dkLen=32)
# print(key)

dekrip_key = key # The key used for encryption (do not store/read this from the file)

#CFB dekrip
from Crypto.Cipher import AES

input_file = 'file-enkripsi-AES.txt'
output_file = 'file-dekripsi-AES.txt'
# key = b'YOUR KEY'

file_in = open(input_file, 'rb')
iv = file_in.read(16)
ciphered_data = file_in.read()
file_in.close()

cipher = AES.new(dekrip_key, AES.MODE_CFB, iv=iv)
original_data = cipher.decrypt(ciphered_data) # No need to un-pad

file_out = open(output_file, 'wb')
file_out.write(original_data)
file_out.close()

#CBC dekrip
# # Read the data from the file
# file_in = open(input_file, 'rb') # Open the file to read bytes
# iv = file_in.read(16) # Read the iv out - this is 16 bytes long
# ciphered_data = file_in.read() # Read the rest of the data
# file_in.close()

# cipher = AES.new(dekrip_key, AES.MODE_CBC, iv=iv)  # Setup cipher
# original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size) # Decrypt and then up-pad the result