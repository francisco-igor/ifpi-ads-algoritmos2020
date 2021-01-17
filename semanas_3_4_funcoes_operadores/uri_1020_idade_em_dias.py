def main():
    i = int(input())
    idade(i)

def idade(i):
    anos = i // 365
    resto = i % 365

    meses = resto // 30

    dias = resto % 30

    print('{} ano(s)'.format(anos))
    print('{} mes(es)'.format(meses))
    print('{} dia(s)'.format(dias))

main()
