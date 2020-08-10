# ENTRADA
salário = int(input('Salário do trabalhador: R$ '))

# PROCESSAMENTO
aumento = (salário * 25) / 100

novo_salário = salário + aumento

# SAÍDA
print('O novo salário do trabalhor é de R$ {:.2f}'.format(novo_salário))