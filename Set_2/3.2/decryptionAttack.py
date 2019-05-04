import random
import numpy as np
from mcd import euclidean_gcd
from primeGenerator import decompose, fast_exp
from RSA import rsa_coeff
import time

def find_coprime(n: int) -> int:
    while True:
        x = random.randint(1, n-1)
        if euclidean_gcd(x, n) == 1:
            return x

def find_factor(x:int, m:int, r:int, n:int)->int:
    x = fast_exp(x, m, n)
    if x == 1:
        return -999
    for j in range(1, r + 1):
        x_old = x
        x = fast_exp(x, 2, n)
        if  x == 1:
            if x_old % n != n-1:
                return euclidean_gcd(x_old+1, n)
            else:
                return -999
    return -999

def decryptionexp(n, d, e):
    r, m = decompose(d * e)
    n_factor, count = -999, 0
    while True:
        x = find_coprime(n)
        n_factor = find_factor(x,m,r,n)
        count = count + 1
        if n_factor != -999:
            return n_factor, count
           

def main():
    time_execution = []
    tot_iterations = 0
    x = time.time()
    number_of_test = 10
    for i in range(number_of_test):
        p,q,n,e,d = rsa_coeff(200)
        start_time = time.time()
        n_factor, count = decryptionexp(n, d, e)
        time_execution.append(time.time()-start_time)
        tot_iterations = tot_iterations + count
    
    mean_iterations = tot_iterations/number_of_test
    mean_time = np.mean(time_execution)
    variance_time = np.var(time_execution)
    print(time_execution)
    print(mean_iterations)
    print(mean_time)
    print(variance_time)

if __name__ == "__main__":
    main()    