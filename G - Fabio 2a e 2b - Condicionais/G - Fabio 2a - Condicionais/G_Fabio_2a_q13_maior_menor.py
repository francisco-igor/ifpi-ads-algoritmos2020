'''Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. Considere que todos os valores são
diferentes.'''

# ENTRADA
def main():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    n3 = int(input('Digite outro número: '))
    n4 = int(input('Digite outro número: '))
    n5 = int(input('Digite outro número: '))
    maior_menor(n1, n2, n3, n4, n5)

# PROCESSAMENTO
def maior_menor(n1, n2, n3, n4, n5):
    if n1 != n2 != n3 != n4 != n5:
        menor = n1
        if n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
            menor = n2
        elif n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
            menor = n3
        elif n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
            menor = n4
        elif n5 < n1 and n5 < n2 and n5 < n3 and n5 < n4:
            menor = n5
        maior = n1
        if n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
            maior = n2
        elif n3 > n1 and n3 > n2 and n3 > n4 and n2 > n5:
            maior = n3
        elif n4 > n1 and n4 > n2 and n4 > n3 and n2 > n5:
            maior = n4
        elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
            maior = n5
        print(f'O número {maior} é o maior e o número {menor} é o menor.')

# SAÍDA
main()
