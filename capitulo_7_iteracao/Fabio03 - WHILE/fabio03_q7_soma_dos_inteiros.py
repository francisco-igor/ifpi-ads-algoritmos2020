'''Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido.'''

# ENTRADA
def main():
    n = int(input('Digite um número: '))
    soma(n)

# PROCESSAMENTO
def soma(n):
    m = n
    soma = 0
    while n >= 1:
        soma = soma + n
        n = n - 1
    
    print(f'A soma dos números inteiros de 1 até {m} é {soma}.')

# SAÍDA
main()
