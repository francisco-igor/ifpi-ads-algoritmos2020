# O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escreva um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.

# ENTRADA
custo = float(input('Leia o custo de fábrica de um carro novo: '))

# PROCESSAMENTO
distribuidor = (custo * 28) / 100
impostos = (custo * 45) / 100

custo_consumidor = custo + distribuidor + impostos

# SAÍDA
print(f'O custo de um carro novo para o consumidor é de $ {custo_consumidor:.2f}')
