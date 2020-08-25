'''Leia N e uma lista de N números e escreva o maior número da lista.'''

# ENTRADA
def main():
    v = int(input('Digite um valor N: '))
    n = int(input('Quantos números terão na lista a partir de N: '))

    maior(v, n)

# PROCESSAMENTO
def maior(v, n):
    maior_num = v + n
    while v > maior_num:
        maior_num = v
    print(maior_num, 'é o maior valor dentro da lista.')

# SAÍDA
main()
