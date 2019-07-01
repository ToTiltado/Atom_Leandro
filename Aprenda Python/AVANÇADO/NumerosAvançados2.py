def rgb_hex(num):
    if type(num) != tuple or any([not (i >= 0 and i < 256) for i in num]) or len(num) != 3:
        raise Exception('Invalido')
    hexv = '#'
    for i in num:
        hexv += hex(round(i))[2:].zfill(2).upper()
    return hexv
print(rgb_hex((255,255,255)))
print(rgb_hex((0,0,0)))
print(rgb_hex((43,89,215)))
print(rgb_hex((96,140,15)))
print(rgb_hex((251,0,15)))
