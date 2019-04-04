

def euclidean_gcd( a:int, b:int)->int:
    if a<b: a,b = b,a 
    while b!=0: a,b=(b, a%b) 
    return a

def extended_euclidean(a:int, b:int)->int:
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


def main():
    pass
    
if __name__ == "__main__":
    main()   