def main():
    N = float(input())
    contador(N)

def contador(N):
    cem = N // 100
    resto = N - cem * 100

    cinquenta = resto // 50
    resto = resto - cinquenta * 50

    vinte = resto // 20
    resto = resto - vinte * 20

    dez = resto // 10
    resto = resto - dez * 10

    cinco = resto // 5
    resto = resto - cinco * 5

    dois = resto // 2
    resto = resto - dois * 2

    um = resto // 1
    resto = resto - um * 1
    um = float('{:.2f}'.format(um))
    resto = float('{:.2f}'.format(resto))

    cinquenta_cents = resto // 0.50
    resto = resto - cinquenta_cents * 0.50
    cinquenta_cents = float('{:.2f}'.format(cinquenta_cents))
    resto = float('{:.2f}'.format(resto))

    vinte_cinco_cents = resto // 0.25
    resto = resto - vinte_cinco_cents * 0.25
    vinte_cinco_cents = float('{:.2f}'.format(vinte_cinco_cents))
    resto = float('{:.2f}'.format(resto))

    dez_cents = resto // 0.10
    resto = resto - dez_cents * 0.10
    dez_cents = float('{:.2f}'.format(dez_cents))
    resto = float('{:.2f}'.format(resto))

    cinco_cents = resto // 0.05
    resto = resto - cinco_cents * 0.05
    cinco_cents = float('{:.2f}'.format(cinco_cents))
    resto = float('{:.2f}'.format(resto))

    um_cent = resto // 0.01
    um_cent = float('{:.2f}'.format(um_cent))

    print('NOTAS:')
    print('{} nota(s) de R$ 100.00'.format(int(cem)))
    print('{} nota(s) de R$ 50.00'.format(int(cinquenta)))
    print('{} nota(s) de R$ 20.00'.format(int(vinte)))
    print('{} nota(s) de R$ 10.00'.format(int(dez)))
    print('{} nota(s) de R$ 5.00'.format(int(cinco)))
    print('{} nota(s) de R$ 2.00'.format(int(dois)))
    print('MOEDAS:')
    print('{} moeda(s) de R$ 1.00'.format(int(um)))
    print('{} moeda(s) de R$ 0.50'.format(int(cinquenta_cents)))
    print('{} moeda(s) de R$ 0.25'.format(int(vinte_cinco_cents)))
    print('{} moeda(s) de R$ 0.10'.format(int(dez_cents)))
    print('{} moeda(s) de R$ 0.05'.format(int(cinco_cents)))
    print('{} moeda(s) de R$ 0.01'.format(int(um_cent)))

main()
