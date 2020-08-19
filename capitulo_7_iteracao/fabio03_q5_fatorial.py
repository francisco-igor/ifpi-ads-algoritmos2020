'''Leia um número, calcule e escreva seu fatorial.'''

# ENTRADA
def main():
    n = int(input('Digite um número: '))

    fatorial(n)

# PROCESSAMENTO
def fatorial(n):
    t = 1
    while n > 0:
        t = t * n
        n = n - 1
    print(t)

# SAÍDA
main()
