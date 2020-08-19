'''Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
Aritmética que tem por valor inicial A0 e razão R.'''

# ENTRADA
def main():
    v = int(input('Digite uma Variável A: '))
    l = int(input('Digite um Limite: '))
    r = int(input('Digite uma Razão: '))

    pa(v, l, r)

# PROCESSAMENTO
def pa(v, l, r):
    while v <= l:
        print(v)
        v = v + r

# SAÍDA
main()
