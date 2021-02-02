def main():
    n = int(input())

    if 1 < n < 1000:
        x = 1
        y = 1
        z = 1
        cont = 0
        while cont < n:
            print(x, y, z)
            x = x + 1
            y = x ** 2
            z = x ** 3

            cont = cont + 1

main()
