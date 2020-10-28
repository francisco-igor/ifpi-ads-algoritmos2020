# Escreva um algoritmo que, tendo como dados de entrada 2 pontos quaisquer no plano, ponto1 (x1,y1) e ponto2 (x2,y2), escreva a distância entre eles, conforme fórmula abaixo.
# d = √(x2 - x1)² + (y2 - y1)²

# ENTRADA
x1 = int(input('Leia o ponto x1: '))
y1 = int(input('Leia o ponto y1: '))
x2 = int(input('Leia o ponto x2: '))
y2 = int(input('Leia o ponto y2: '))

# PROCESSAMENTO
d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# SAÍDA
print(f'A distância entre os pontos é de {d:.1f}cm.')
