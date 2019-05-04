import primeGenerator
import mcd
import random


def find_coprime_multiplicative_inverse(n: int, phi: int) -> int:
    while True:
        e = random.randint(3, n)
        gcd, d, _ = mcd.extended_euclidean(e, phi)
        if gcd == 1:
            return e, d % phi


def en_de_cript(k: int, n: int, m: int):
    return primeGenerator.fast_exp(m, k, n)

def rsa_coeff(l:int):
    p = primeGenerator.generate_prime(l)
    q = primeGenerator.generate_prime(l)
    while p == q:
        q = primeGenerator.generate_prime(l)

    n = p * q
    phi = (p - 1) * (q - 1)
    e, d = find_coprime_multiplicative_inverse(n, phi)

    return p,q,n,e,d

def main():
    p,q,n,e,d = rsa_coeff(1000)
    m = random.randint(2, n)

    c = en_de_cript(e, n, m)
    e = en_de_cript(d, n, c)

    print("Message: ", m)
    print("Encrypted: ", c)
    print("Decrypted: ", e)


if __name__ == "__main__":
    main()
