'''Leia N, calcule e escreva os N primeiros termos de seqüência (1, 3, 6, 10, 15,...).'''

# ENTRADA
def main():
    n = int(input('Digite um número N: '))

    sequencia(n)

# PROCESSAMENTO
def sequencia(n):
    s = 1
    v = 2
    while v <= n + 1:
        print(s, end=' ')
        s = s + v
        v = v + 1

# SAÍDA
main()
