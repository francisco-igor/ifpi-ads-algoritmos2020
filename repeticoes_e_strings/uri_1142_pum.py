def main():
    n = int(input())

    x = 1
    y = 2
    z = 3
    cont = 0
    while cont < n:
        print(x, y, z, 'PUM')
        cont = cont + 1
        x = x + 4
        y = x + 1
        z = y + 1

main()
