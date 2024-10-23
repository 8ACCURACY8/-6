import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    gcd, x, y = gcd_extended(e, phi)
    if gcd != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % phi

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Вибір e, яке взаємно просте з phi та 1 < e < phi
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Обчислення d
    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    p = 61
    q = 53
    public, private = generate_keypair(p, q)
    print("Public key:", public)
    print("Private key:", private)

    message = "Hello World"
    encrypted_msg = encrypt(public, message)
    print("Encrypted message:", ''.join(map(lambda x: str(x), encrypted_msg)))

    decrypted_msg = decrypt(private, encrypted_msg)
    print("Decrypted message:", decrypted_msg)

def read_file(filename):
    with open(filename, 'rb') as file:
        return file.read()

def write_file(filename, data):
    with open(filename, 'wb') as file:
        file.write(data)

if __name__ == '__main__':
    p = 61
    q = 53
    public, private = generate_keypair(p, q)
    print("Public key:", public)
    print("Private key:", private)

    
    input_filename = 'input.txt'
    output_filename = 'encrypted.txt'
    data = read_file(input_filename)
    encrypted_data = encrypt(public, data.decode())
    encrypted_bytes = ' '.join(map(lambda x: str(x), encrypted_data)).encode()
    write_file(output_filename, encrypted_bytes)

    print("Файл зашифровано і збережено як", output_filename)

   
    input_filename = 'encrypted.txt'
    output_filename = 'decrypted.txt'
    data = read_file(input_filename)
    encrypted_data = list(map(int, data.decode().split()))
    decrypted_data = decrypt(private, encrypted_data).encode()
    write_file(output_filename, decrypted_data)

    print("Файл розшифровано і збережено як", output_filename)

import time


start_time = time.time()

end_time = time.time()
print("Час виконання RSA:", end_time - start_time)


start_time = time.time()

end_time = time.time()
print("Час виконання DES:", end_time - start_time)
