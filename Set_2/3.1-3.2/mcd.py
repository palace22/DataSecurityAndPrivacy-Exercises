def euclidean_gcd(a: int, b: int) -> int:
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = (b, a % b)
    return a


def extended_euclidean(a: int, b: int) -> int:
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


def common_modules_faliure():
    n = 112137763021160565141095447514289188316099305050728548533990009459340088478604617874283528379792371687919406014282922583771903203542840497778554663219496576912001458191643798008255064443259316602248816694007897022508299325243314145599359546048231178850144548579269422836638239848102178140850949393175535681977
    e1, e2 = 3, 5
    c1, c2 = 82819140145469, 157356442552819173976949
    _, a, b = extended_euclidean(e1, e2)
    c1_exp = c1 ** a
    _, c2_exp, _ = extended_euclidean(c2, n)
    m = (c1_exp * c2_exp) % n
    print(m)


def main():
    common_modules_faliure()


if __name__ == "__main__":
    main()

