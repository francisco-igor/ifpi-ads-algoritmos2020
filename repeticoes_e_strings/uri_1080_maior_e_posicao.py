def main():
    z = 0
    pos = 1
    cont = 0
    while cont < 100:
        x = int(input())
        if x > z:
            y = x
            p = pos
            z = x
        pos += 1
        cont += 1
    print(y)
    print(p)
main()
