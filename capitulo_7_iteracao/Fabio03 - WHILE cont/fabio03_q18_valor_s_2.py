'''Leia N, calcule e escreva o valor de S.'''

# ENTRADA
def main():
    n = int(input('Digite um valor para N: '))

    valor(n)

# PROCESSADOR
def valor(n):
    num = 1
    soma = 0
    while n >= 1:
        soma = soma + num / n
        num = num + 1
        n = n - 1
    print(soma)

# SAÍDA    
main()
