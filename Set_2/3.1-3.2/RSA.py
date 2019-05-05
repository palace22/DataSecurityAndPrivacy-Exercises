from primeGenerator import generate_prime, fast_exp
from mcd import extended_euclidean
import random
import time

def find_coprime_multiplicative_inverse(n: int, phi: int) -> int:
    while True:
        e = random.randint(3, n)
        gcd, d, _ = extended_euclidean(e, phi)
        if gcd == 1:
            return e, d % phi


def en_de_crypt(k: int, n: int, m: int):
    start_time = time.time()
    m = fast_exp(m, k, n)
    return m, time.time()-start_time

def crt_decryption(s_p:int, s_q:int, p:int, q:int, d:int)->int:     
   
    _, q_inv, _ = extended_euclidean(q, p) 
    _, p_inv, _ = extended_euclidean(p, q) 
    s_p = s_p*q*(q_inv%p)
    s_q = s_q*p*(p_inv%q)

    s = (s_p+s_q)%(q*p)
    start_time = time.time()
    m = fast_exp(s, d, p*q)
    return m, time.time()-start_time

def rsa_coeff(l:int):
    p = generate_prime(l)
    q = generate_prime(l)
    while p == q:
        q = generate_prime(l)

    n = p * q
    phi = (p - 1) * (q - 1)
    e, d = find_coprime_multiplicative_inverse(n, phi)

    return p,q,n,e,d

def main():
    p,q,n,e,d = rsa_coeff(1000)
    tot = 0
    print("RSA module: ", n)
    for i in range(0,100):
        m = random.randint(2, n)
        s_p = fast_exp(m,e,p)
        s_q = fast_exp(m,e,q)

        c, _ = en_de_crypt(e, n, m)

        decrypt_m, decr_standard_time = en_de_crypt(d, n, c)
        crt_decrypt_m, decr_crt_time = crt_decryption(s_p, s_q, p, q, d)
        diff = decr_standard_time - decr_crt_time
        tot = tot + diff
        print("DEC STD: ", decr_standard_time)
        print("DEC CRT: ", decr_crt_time)
        print("DIFF:    ", diff,"\n")
    # print("Message: ", m)
    # print("Encrypted: ", c)
    # print("Decrypted: ", decrypt_m)
    # print("Decrypted: ", crt_decrypt_m)
    print("TOT.: ",tot)


if __name__ == "__main__":
    main()
