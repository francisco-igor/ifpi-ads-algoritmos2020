def main():
    while True:
        m, n = input().split()
        m = int(m)
        n = int(n)

        if m <= 0 or n <= 0:
            break
        elif m > n:
            soma = 0
            while m >= n:
                print(n, end=' ')
                soma = soma + n
                n += 1
            print(f'Sum={soma}')
        elif m < n:
            soma = 0
            while m <= n:
                print(m, end=' ')
                soma = soma + m
                m += 1
            print(f'Sum={soma}')
main()
