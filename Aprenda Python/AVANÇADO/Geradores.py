def potencia(num):
    for x in range(num):
        yield x**2
for p in potencia(10):
    print(p)
