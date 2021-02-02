def main():
    n = int(input())

    cont = 0
    while cont < n:
        x, y = input().split()
        x = int(x)
        y = int(y)

        s = 0
        c = 0
        while c < y:
            if x % 2 != 0:
                s = s + x
                c = c + 1
            x = x + 1
            
        cont = cont + 1
        print(s)

main()
