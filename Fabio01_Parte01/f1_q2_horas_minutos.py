# ENTRADA
horas = int(input("Valor em horas: "))
minutos = int(input("Valor em minutos "))

# PROCESSAMENTO
hora_para_minutos = horas * 60
minutos_total = hora_para_minutos + minutos

# SAÍDA
print("{} h e {} mins equivalem a {} mins".format(horas, minutos, minutos_total))