import math as m
import random


bit_length = 1024


def gen_prime(bit_length=1024):
    while True:
        num = random.getrandbits(bit_length)
        if is_prime(num):
            return num



def is_prime(n, k=5):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True





def inverse(a: int, m: int) -> int:
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def gcd(a: int, b: int) -> int:
    return a if b == 0 else m.gcd(a, a % b)


def generate_keypair(p, q, bit_length):
    # Генерим простые числа
    p = gen_prime(bit_length)
    q = gen_prime(bit_length)

    # Модуль
    n = p * q
    # Ф-ия Эйлера
    phi = (p-1) * (q-1)

    # Выбираем открытый ключ e, такой что 1 < e < phi и e взаимно прост с phi
    e = random.randrange(2, phi)
    while m.gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Вычисляем закрытый ключ d, такой что d * e ≡ 1 (mod phi)
    d = inverse(e, phi)

    # Возвращаем открытый и закрытый ключ
    return ((e, n), (d, n))


# Шифрование
def encrypt(public_key, plaintext):
    e, n = public_key
    # Шифруем каждую букву
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

# Расшифровка
def decrypt(private_key, ciphertext):
    d, n = private_key
    # Расшифровываем каждую букву
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plaintext)
