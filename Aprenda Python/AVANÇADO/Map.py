list(map(lambda x: print('{} ------> {}'.format(x,x)) if x % 3 == 0 or x % 5 == 0 else print('{} ------>{}'.format(x,x ** 2)),range(0, 31)))
