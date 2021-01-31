def main():
    while True:
        x, y = input().split()
        x = int(x)
        y = int(y)

        if x < y:
            print('Crescente')
        elif x > y:
            print('Decrescente')
        else:
            break
main()
