p = int(input('Quer executar o programa da forma 1 ou da 2? '))
if p == 1:
    x = [0,1,2,3,4,5,6,7,8,9]
    y = [0,1,4,9,16,25,36,49,64,81]
elif p == 2:
    print(list(zip(x,y)))
    x = [0,1,2,3,4,5,6,7,8,9]
    y = [0,1,2**2,3**2,4**2,5**2,6**2,7**2,8**2,9**2]
    print(list(zip(x,y)))
else:
    print('Digite um numero valido animal!!Reinicie o programa')
#Esse programa possui duas formas de fazer
