print('----------------------------------')
print('TRIANGULO VALIDO')
print('----------------------------------')
a = int(input('Qual e o valor do lado A?'))
b = int(input('Qual e o valor do lado B?'))
c = int(input('Qual e o valor do lado C?'))
print('----------------------------------')
ab = a + b
ac = a + c
bc = b + c
if ab >= c and ac >= b and bc >= a:
    print('---------------')
    print('VALIDO')
    print('---------------')
else:
    print('---------------')
    print('INVALIDO')
    print('---------------')
