# Sabendo que latão é constituído de 70% de cobre e 30% de zinco, escreva um algoritmo que calcule a quantidade de cada um desses componentes para se obter certa quantidade de latão (em kg), informada pelo usuário.

# ENTRADA
latao = float(input('Quantidade em kg de latão: '))

# PROCESSAMENTO
cobre = ((latao * 70) / 100) * 1000
zinco = ((latao * 30) / 100) * 1000

# SAÍDA
print(f'Serão necessários {cobre:.0f}g de cobre e {zinco:.0f}g de zinco para obter {latao}kg de latão.')
