# Leia uma velocidade em m/s, calcule e escreva esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)

# ENTRADA
Vms = int(input("Um valor em metros por segundo: "))

# PROCESSAMENTO
Vkmh = Vms * 3.6

# SAÍDA
print("A velocidade {} m/s equivale a {:.0f} km/h".format(Vms,Vkmh))
