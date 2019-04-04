import primeGenerator
import mcd
import random


def find_coprime_multiplicative_inverse(n: int, phi: int) -> int:
    while True:
        e = random.randint(3, n)
        gcd, d, _ = mcd.extended_euclidean(e, phi)
        if gcd == 1:
            return e, d%phi

def en_de_cript(k:int, n:int, m:int):
    return primeGenerator.fast_exp(m, k, n)


def main():
    p = primeGenerator.generate_prime(50)
    q = primeGenerator.generate_prime(50)
    n = p * q
    phi = (p - 1) * (q - 1)
    e, d = find_coprime_multiplicative_inverse(n, phi)
    m = random.randint(2, n)

    print("n= ",n,"\nphi= ",phi,"\ne= ",e,"\nd= ",d,"\nm= ",m)
    print((e*d)%phi)

    c = en_de_cript(e, n, m)
    e = en_de_cript(d, n, c)

    print("Encrypted: ",c)
    print("Decrypted: ",e)
    
if __name__ == "__main__":
    main()