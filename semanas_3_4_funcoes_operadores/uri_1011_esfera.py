def main():
    R = float(input())
    esfera(R)

def esfera(R):
    pi = 3.14159

    esfera = (4/3) * pi * (R**3)

    print('VOLUME = {:.3f}'.format(esfera))

main()
