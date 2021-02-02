def main():
    x = 0
    a = 0
    g = 0
    d = 0
    while x != 4:
        x = int(input())

        if x == 1:
            a = a + 1
        elif x == 2:
            g = g + 1
        elif x == 3:
            d = d + 1
    print('MUITO OBRIGADO')
    print(f'Alcool: {a}')
    print(f'Gasolina: {g}')
    print(f'Diesel: {d}')

main()
