def main():
    x = int(input())
    y = int(input())

    if x > y:
        y = y + 1
        while x > y:
            if y % 5 == 2 or y % 5 == 3:
                print(y)
            y = y + 1
    elif x < y:
        x = x + 1
        while x < y:
            if x % 5 == 2 or x % 5 == 3:
                print(x)
            x = x + 1

main()
