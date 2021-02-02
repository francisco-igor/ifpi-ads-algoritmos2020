def main():
    d = 1
    s = 0
    for n in range(1, 40, 2):
        s = s + n / d
        d = d * 2
    print(f'{s:.2f}')

main()
