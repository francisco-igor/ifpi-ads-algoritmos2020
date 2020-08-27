'''Leia N, calcule e escreva o valor de S.'''

# ENTRADA
def main():
    n = int(input('Digite um valor para N: '))

    valor(n)

# PROCESSADOR
def valor(n):
    den = 1
    soma = 0
    while den <= n:
        soma = soma + 1 / den
        den = den + 1
        soma = soma * -1

    if soma < 0:
        soma = soma * -1

    print(soma)

# SAÍDA    
main()
