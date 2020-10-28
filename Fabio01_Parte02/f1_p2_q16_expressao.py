# Leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão: D = R + S / 2, onde R = (A + B)² e S = (B + C)².

# ENTRADA
A = int(input('Leia o número A: '))
B = int(input('Leia o número B: '))
C = int(input('Leia o número C: '))

# PROCESSAMENTO
R = A ** 2 + B ** 2
S = B ** 2 + C ** 2

D = (R + S) / 2

# SAÍDA
print(f'O resultado da expressão é {D}')
