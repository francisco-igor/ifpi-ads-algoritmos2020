nome = input()
salario_fixo = float(input())
total_vendas = float(input())

renda = ((total_vendas * 15) / 100) + salario_fixo

print('TOTAL = R$ {:.2f}'.format(renda))
