from cryptography.fernet import Fernet

message = 'Hello there!'
print('Original: ', message)

key = Fernet.generate_key()
fernet = Fernet(key)
message = fernet.encrypt(message.encode())
print('Encrypted: ', message)

message = fernet.decrypt(message)
print('Decrypted: ',message)