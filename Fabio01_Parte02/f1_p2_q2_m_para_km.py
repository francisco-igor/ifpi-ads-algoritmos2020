# Leia um número inteiro de metros, calcule e escreva quantos Km e quantos metros ele corresponde.

# ENTRADA
metros = int(input('Leia um valor em m: '))

# PROCESSAMENTO
km = metros // 1000
m = metros % 1000

# SAÍDA
print(f'O valor {metros}m corresponde a {km}km e {m}m.')
