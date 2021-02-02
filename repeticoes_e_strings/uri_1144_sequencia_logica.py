def main():
    n = int(input())

    x = 1
    y = 1
    z = 1
    if 1 < n < 1000:
        while x <= n:
            print(x, y, z)
            y = y + 1
            z = z + 1
            print(x, y, z)
            x = x + 1
            y = x ** 2
            z = x ** 3

main()
