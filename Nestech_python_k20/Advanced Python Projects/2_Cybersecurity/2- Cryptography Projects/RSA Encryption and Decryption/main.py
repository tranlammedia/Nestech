import random
from math import gcd

def generate_keys(p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    while True:
        e = random.randrange(1, phi_n)
        if gcd(e, phi_n) == 1:
            break
    
    d = pow(e, -1, phi_n)
    
    return (e, n), (d, n)

def encrypt(plain_text, public_key):
    e, n = public_key
    cipher_text = [pow(ord(char), e, n) for char in plain_text]
    return cipher_text

def decrypt(cipher_text, private_key):
    d, n = private_key
    plain_text = [chr(pow(char, d, n)) for char in cipher_text]
    return ''.join(plain_text)

if __name__ == '__main__':
    p = 61
    q = 53
    public_key, private_key = generate_keys(p, q)
    print('Public key:', public_key)
    print('Private key:', private_key)
    
    plain_text = 'This is the text'
    cipher_text = encrypt(plain_text, public_key)
    print('Cipher text:', cipher_text)
    
    decrypted_text = decrypt(cipher_text, private_key)
    print('Decrypted text:', decrypted_text)






#1. import random: import thư viện random để sinh số ngẫu nhiên.


#2. from math import gcd: import hàm gcd (greatest common divisor) trong thư viện math để tìm ước chung lớn nhất.


#3. def generate_keys(p, q): Hàm tạo ra cặp khóa công khai và khóa bí mật. 
# Truyền vào hai số nguyên p và q, đây là hai số nguyên tố khác nhau được sử dụng để tạo khóa.


#4. n = p * q: Tính n bằng tích của p và q.


#5. phi_n = (p - 1) * (q - 1): Tính giá trị của hàm phi Euler (phi_n) cho p và q. 
# Giá trị này được sử dụng để tạo khóa bí mật.


#6. while True: Thực hiện vòng lặp vô hạn để tạo khóa công khai.


#7. e = random.randrange(1, phi_n): Chọn một số ngẫu nhiên trong khoảng từ 1 đến giá trị của hàm phi Euler.


#8. if gcd(e, phi_n) == 1: Kiểm tra xem e có ước chung lớn nhất với phi_n là 1 hay không. 
# Nếu có, dừng vòng lặp và sử dụng e như khóa công khai.


#9. d = pow(e, -1, phi_n): Tính khóa bí mật d bằng cách tính phần tử nghịch đảo của e mod phi_n bằng cách 
# sử dụng hàm pow.


#10. return (e, n), (d, n): Trả về cặp khóa công khai và khóa bí mật.


#11. def encrypt(plain_text, public_key): Hàm thực hiện mã hóa văn bản đơn giản. 
# Nhận vào văn bản rõ và khóa công khai.


#12. e, n = public_key: Lấy giá trị khóa công khai.


#13. cipher_text = [pow(ord(char), e, n) for char in plain_text]: 
# Mã hóa văn bản rõ bằng cách sử dụng khóa công khai. 
# Mỗi ký tự trong văn bản rõ được mã hóa thành một số nguyên và lưu trữ trong một mảng. 
# Hàm ord trả về mã ASCII của ký tự.


#14. return cipher_text: Trả về văn bản được mã hóa.


#15. def decrypt(cipher_text, private_key): Hàm thực hiện giải mã văn bản. Nhận vào văn bản