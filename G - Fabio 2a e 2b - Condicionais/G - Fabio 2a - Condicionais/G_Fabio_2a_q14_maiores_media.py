'''Leia 5 (cinco) números inteiros, calcule a sua média e escreva os que são maiores que a média.'''

# ENTRADA
def main():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    n3 = int(input('Digite um número: '))
    n4 = int(input('Digite um número: '))
    n5 = int(input('Digite um número: '))
    media(n1, n2, n3, n4, n5)

# PROCESSAMENTO
def media(n1, n2, n3, n4, n5):
    media_a = (n1 + n2 + n3 + n4 + n5) / 5
    if n1 > media_a or n2 > media_a or n3 > media_a or n4 > media_a or n5 > media_a:
        if n1 > media_a:
            print(f'O número {n1} é maior que a média.')
        if n2 > media_a:
            print(f'O número {n2} é maior que a média.')
        if n3 > media_a:
            print(f'O número {n3} é maior que a média.')
        if n4 > media_a:
            print(f'O número {n4} é maior que a média.')
        if n5 > media_a:
            print(f'O número {n5} é maior que a média.')
    else:
        print('Nenhum número é maior que a média.')
# SAÍDA
main()
