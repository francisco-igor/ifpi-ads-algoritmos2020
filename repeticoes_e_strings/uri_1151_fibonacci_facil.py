def main():
    n = int(input())

    if 0 < n < 46:
        soma = 0
        d1 = 0
        d2 = 1
        cont = 1
        while cont < n:
            print(d1, end=' ')
            soma = d1 + d2
            d1 = d2
            d2 = soma
            cont = cont + 1
            if cont == n:
                print(d1)

main()
