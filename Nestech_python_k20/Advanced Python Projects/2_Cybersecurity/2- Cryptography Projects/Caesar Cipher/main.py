import string

# Function to encrypt a message using the Caesar cipher / Chức năng mã hóa một thông báo bằng mật mã Caesar
def encrypt(message, key):
    # Generate the mapping of characters / Tạo ánh xạ của các ký tự
    mapping = {}
    for i in range(len(string.ascii_lowercase)):
        mapping[string.ascii_lowercase[i]] = string.ascii_lowercase[(i+key) % len(string.ascii_lowercase)]
    for i in range(len(string.ascii_uppercase)):
        mapping[string.ascii_uppercase[i]] = string.ascii_uppercase[(i+key) % len(string.ascii_uppercase)]

    # Encrypt the message / Mã hóa tin nhắn
    result = ''
    for c in message:
        if c in mapping:
            result += mapping[c]
        else:
            result += c
    return result

# Function to decrypt a message using the Caesar cipher / Chức năng giải mã một thông điệp bằng mật mã Caesar
def decrypt(message, key):
    # Generate the mapping of characters / Tạo ánh xạ của các ký tự
    mapping = {}
    for i in range(len(string.ascii_lowercase)):
        mapping[string.ascii_lowercase[i]] = string.ascii_lowercase[(i-key) % len(string.ascii_lowercase)]
     
    for i in range(len(string.ascii_uppercase)):
        mapping[string.ascii_uppercase[i]] = string.ascii_uppercase[(i-key) % len(string.ascii_uppercase)]
        
    # for i,j in enumerate(mapping):
    #     print(f"key: {j} - value: {mapping[j]}")
    
    # Decrypt the message / Giải mã tin nhắn
    result = ''
    for c in message:
        if c in mapping:
            result += mapping[c]
        else:
            result += c
    return result

# Example usage / Ví dụ sử dụng
message = 'This is an encrypted message'
key = 3
encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)

print('Original message:', message)
print('Encrypted message:', encrypted)
print('Decrypted message:', decrypted)
