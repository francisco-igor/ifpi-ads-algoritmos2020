'''Leia N, calcule e escreva o valor de S.'''

# ENTRADA
def main():
    s = 0
    num = 1
    den = 1

# PROCESSAMENTO
    while num <= 99:
        s = s + num / den
        num = num + 2
        den = den + 1
    print(s)

# SAÍDA
main()
