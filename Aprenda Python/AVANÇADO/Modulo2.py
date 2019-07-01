from collections import OrderedDict
p1 = int(input('Quer executar qual parte do código a 1 ou a 2: '))
if p1 == 1:
    d =  OrderedDict()
    d[1] = 'P'
    d[2] = 'Y'
    d[3] = 'T'
    d[4] = 'H'
    d[5] = 'O'
    d[6] = 'N'
    for d1, d2 in d.items():
        print(d1,d2)
#Aqui Aparecerá outra forma de fazer que estou tentando entender como funciona
elif p1 == 2:
    print(OrderedDict({d:value for value, d in enumerate('Python')}))
else:
    print('Digite um numero valido animal!!!')
#Entendi como funciona kkk
