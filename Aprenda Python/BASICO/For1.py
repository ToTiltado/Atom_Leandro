l = [1,4,5,67,7,8,6,54,4,3,1,21,1,9,0]
for n in l:
    if n % 2 == 0 and n != 0:
        print('NUMERO PAR:')
        print(n)
    elif n == 0:
        print('ZERO E UM NUMERO NEUTRO')
    else:
        print('NUMERO IMPAR')
        print(n)
