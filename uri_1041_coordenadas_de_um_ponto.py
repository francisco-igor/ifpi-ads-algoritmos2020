def main():
    x, y = input().split(' ')
    x = float(x)
    y = float(y)
    pontos(x, y)

def pontos(x, y):
    if x == 0 and y == 0:
        print('Origem')

    elif x != 0 and y != 0:
        if x > 0 and y > 0:
            print('Q1')
        elif x < 0 and y > 0:
            print('Q2')
        elif x < 0 and y < 0:
            print('Q3')
        elif x > 0 and y < 0:
            print('Q4')

    else:
        if x == 0:
            print('Eixo Y')
        else:
            print('Eixo X')

main()
