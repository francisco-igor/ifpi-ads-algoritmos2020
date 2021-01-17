def main():
    a, b, c = input().split()
    a = float(a)
    b = float(b)
    c = float(c)
    eh_triangulo(a, b, c)

def eh_triangulo(a, b, c):
    if a >= b and a >= c:
        d = a
        if b >= c:
            e = b
            f = c
        else:
            e = c
            f = b
    elif b >= a and b >= c:
        d = b
        if a >= c:
            e = a
            f = c
        else:
            e = c
            f = a
    elif c >= a and c >= b:
        d = c
        if a >= b:
            e = a
            f = b
        else:
            e = b
            f = a
    elif a == b and b == c:
        d = a
        e = b
        f = c

    a = d
    b = e
    c = f

    if a >= b + c:
        print('NAO FORMA TRIANGULO')
    else:
        if (a ** 2) == (b ** 2) + (c ** 2):
            print('TRIANGULO RETANGULO')

        elif (a ** 2) > (b ** 2) + (c ** 2):
            print('TRIANGULO OBTUSANGULO')

        elif (a ** 2) < (b ** 2) + (c ** 2):
            print('TRIANGULO ACUTANGULO')

        if a == b == c:
            print('TRIANGULO EQUILATERO')
        elif a == b != c or b == c != a or a == c != b:
            print('TRIANGULO ISOSCELES')

main()
