import random


def generate_random_number(k: int):
    random_number = [random.randint(0, 1) for i in range(k)]
    random_number[0], random_number[len(random_number) - 1] = 1, 1
    random_number = "".join(map(str, random_number))
    return int(random_number, 2)


def decompose(_n: int):
    n, r = _n - 1, 0
    while n % 2 == 0:
        n, r = n / 2, r + 1
    return r, int((_n - 1) / (2 ** r))


def compute_test_rabin(n: int, time: int):
    for i in range(time):
        if comp_rabin(random.randint(2, n - 1), n):
            return True
    return False


def fast_exp(base: int, esp: int, module: int):
    esp = [int(i) for i in list(bin(esp)[2:])]
    d, c = 1, 0
    for i in range(0, len(esp)):
        d = (d * d) % module
        c = 2 * c
        if esp[i] == 1:
            d = (d * base) % module
            c = c + 1
    return d


def comp_rabin(x: int, n: int):
    r, m = decompose(n)
    # x = (x ** m) % n
    x = fast_exp(x, m, n)
    for m in range(r):
        if x == (1 or n - 1) and m != r - 1:
            return True
        x = (x ** 2) % n
    if x != 1:
        return True
    else:
        return False


def generate_prime(k: int):
    flag, p, t = True, 0, 0
    while flag:
        p = generate_random_number(k)
        print("Tested: ", p)
        flag = compute_test_rabin(p, 5)
        t = t + 1
    return p, t


def main():
    k = 60
    p, t = generate_prime(k)
    print( "After:", t, " test!")
    print("Prime of: 2^", k," is ", p)


if __name__ == "__main__":
    main()

