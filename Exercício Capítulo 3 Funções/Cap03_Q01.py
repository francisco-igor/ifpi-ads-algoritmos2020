def right_justify(s):
    quant_espaços = 70 - len(s)
    espaço = quant_espaços * ' '
    resultado = espaço + s
    print(resultado)

right_justify('s')
