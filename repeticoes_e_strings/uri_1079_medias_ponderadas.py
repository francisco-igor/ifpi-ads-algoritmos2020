def main():
    x = int(input())
    cont = 0
    while cont < x:
        a, b, c = input().split()
        mp = (float(a) * 2 + float(b) * 3 + float(c) * 5) / (2 + 3 + 5)
        print(f'{mp:.1f}')
        cont += 1
main()
