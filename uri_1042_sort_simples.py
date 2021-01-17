def main():
    a, b, c = input().split(' ')
    a = int(a)
    b = int(b)
    c = int(c)
    sort(a, b, c)

def sort(a, b, c):
    if a < b and a < c:
        d = a
        if b < c:
            e = b
            f = c
        else:
            e = c
            f = b
    elif b < a and b < c:
        d = b
        if a < c:
            e = a
            f = c
        else:
            e = c
            f = a
    else:
        d = c
        if a < b:
            e = a
            f = b
        else:
            e = b
            f = a

    print(d)
    print(e)
    print(f)
    print()
    print(a)
    print(b)
    print(c)

main()
