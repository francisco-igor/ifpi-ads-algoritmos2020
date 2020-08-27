'''Leia N, calcule e escreva o valor de S.'''

# ENTRADA
def main():
    n = int(input('Digite um valor para N: '))

    valor(n)

# PROCESSADOR
def valor(n):
    d = 1
    soma = 0
    while d <= n:
        soma = soma + 1/d
        d = d + 1
    print(soma)

# SAÍDA    
main()
