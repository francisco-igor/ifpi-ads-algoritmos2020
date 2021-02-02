def main():
    x = int(input())
    y = int(input())

    soma = 0
    if x > y:
        while y <= x:
            if y % 13 != 0:
                soma = soma + y
            y = y + 1
        print(soma)
    elif x < y:
        while x <= y:
            if x % 13 != 0:
                soma = soma + x
            x = x + 1
        print(soma)

main()
