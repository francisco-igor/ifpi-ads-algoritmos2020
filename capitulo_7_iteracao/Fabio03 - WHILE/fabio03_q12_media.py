'''Leia N e uma lista de N números e escreva a soma e a média de todos os números da lista.'''

# ENTRADA
def main():
    n = int(input('Digite um número: '))
    l = int(input('Digite a quantidade de números da lista: '))
    media(n, l)

# PROCESSAMENTO
def media(n, l):
    soma = 0
    while n <= l:
        soma = soma + n
        n = n + 1
    print(f'A soma de todos os números é {soma}', end=' ')
    soma = soma / 2
    print(f'e a média é {soma}.')
        
# SAÍDA
main()
