def main():
    A, B, C = input().split(' ')
    area(A, B, C)

def area(A, B, C):
    triangulo = (float(A) * float(C)) / 2
    circulo = 3.14159 * (float(C) ** 2)
    trapezio = ((float(A) + float(B)) * float(C)) / 2
    quadrado = float(B) * float(B)
    retangulo = float(A) * float(B)

    print('TRIANGULO: {:.3f}'.format(triangulo))
    print('CIRCULO: {:.3f}'.format(circulo))
    print('TRAPEZIO: {:.3f}'.format(trapezio))
    print('QUADRADO: {:.3f}'.format(quadrado))
    print('RETANGULO: {:.3f}'.format(retangulo))

main()
