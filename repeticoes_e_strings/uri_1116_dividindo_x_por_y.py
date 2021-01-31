def main():
    n = int(input())
    cont = 0
    while cont < n:
        x, y = input().split()
        x = int(x)
        y = int(y)

        if y == 0:
            print('divisao impossivel')
        else:
            divisao = x / y
            print(f'{divisao:.1f}')
        cont += 1
main()
