def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    tempo(a, b)

def tempo(a, b):
    if a >= b:
        b = b + 24
        duracao = b - a
        print('O JOGO DUROU {} HORA(S)'.format(duracao))

    else:
        duracao = b - a
        print('O JOGO DUROU {} HORA(S)'.format(duracao))

main()
