def main():
    a, b, c = input().split()
    a = float(a)
    b = float(b)
    c = float(c)
    triangulo(a, b, c)

def triangulo(a, b, c):
    if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
        perimetro = a + b + c
        print('Perimetro = {:.1f}'.format(perimetro))

    else:
        area = ((a + b) * c) / 2
        print('Area = {:.1f}'.format(area))

main()
