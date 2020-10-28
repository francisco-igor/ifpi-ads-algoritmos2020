# Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada: o número de anos que ele fuma, o no de cigarros fumados por dia e o preço de uma carteira (1 carteira tem 20 cigarros).

# ENTRADA
anos = int(input('Nº de anos que fuma: '))
cigarros_por_dia = int(input('Quantos cigarros fumados por dia: '))
preco_carteira = float(input('Preço da carteira de cigarro: '))

# PROCESSAMENTO
carteira = 20

dias_total = anos * 365
qtd_cigarros = cigarros_por_dia * dias_total
carteiras_total = qtd_cigarros / carteira
total_gasto = preco_carteira * carteiras_total

# SAÍDA
print(f'A quantidade de dinheiro gasto pelo fumante é de $ {total_gasto:.2f}')
