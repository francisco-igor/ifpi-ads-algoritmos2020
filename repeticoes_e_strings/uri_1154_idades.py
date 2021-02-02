def main():
    soma = 0
    x = 0
    cont = 0
    while x >= 0:
        x = int(input())
        if x >= 0:
            soma = soma + x
            cont = cont + 1

    media = soma / cont
    print(f'{media:.2f}')
main()
