# ENTRADA
valor_em_minutos = int(input("Valor em minutos: "))

# PROCESSAMENTO
horas = valor_em_minutos // 60
minutos = valor_em_minutos % 60

# SAÍDA
print("{} mins = {} h e {} mins".format(valor_em_minutos, horas, minutos))