def main():
    n = 1
    s = 0
    for d in range(1, 101):
        s = s + n / d
    print(f'{s:.2f}')

main()
