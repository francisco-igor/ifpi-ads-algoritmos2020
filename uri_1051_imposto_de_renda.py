def main():
    v = float(input())
    ir(v)

def ir(x):
    if x <= 2000:
        print('Isento')
    
    elif 2000.01 <= x <= 3000:
        d = x - 2000
        ir = (d * 8) / 100
        print(f'R$ {ir:.2f}')

    elif 300.01 <= x <= 4500:
        d = x - 3000
        i = (1000 * 8) / 100
        ir = (d * 18) / 100 + i
        print(f'R$ {ir:.2f}')

    elif x > 4500:
        d = x - 4500
        i = (1000 * 8) / 100
        i2 = (1500 * 18) / 100
        ir = (d * 28) / 100 + i + i2
        print(f'R$ {ir:.2f}')

main()
