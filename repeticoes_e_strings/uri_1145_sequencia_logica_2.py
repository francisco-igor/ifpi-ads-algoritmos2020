def main():
    x, y = input().split()
    x = int(x)
    y = int(y)

    if 1 < x < 20:
        if x < y < 100000:
            a = 1
            b = 0
            while a <= y:
                while b < x - 1:
                    print(a, end=' ')
                    a = a + 1
                    b = b + 1
                print(a)
                b = 0
                a = a + 1

main()
