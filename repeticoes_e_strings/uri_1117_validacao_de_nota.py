def main():
    while True:
        n1 = float(input())
        if 0 <= n1 <= 10:
            nota1 = n1
            break
        else:
            print('nota invalida')
    while True:
        n2 = float(input())
        if 0 <= n2 <= 10:
            nota2 = n2
            break
        else:
            print('nota invalida')
    media = (nota1 + nota2) / 2
    print(f'media = {media:.2f}')
main()
