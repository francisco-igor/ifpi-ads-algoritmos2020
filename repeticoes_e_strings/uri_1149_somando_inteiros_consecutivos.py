def main():
    x = input().split()
    a = int(x[0])
    ultimo = len(x) - 1
    n = int(x[ultimo])

    soma = 0
    for i in range(n):
        soma = soma + i + a
    print(soma)

main()
