N = int(input())

horas = N // 3600
resto = N % 3600

minutos = resto // 60

segundos = resto % 60

print('{}:{}:{}'.format(horas, minutos, segundos))
