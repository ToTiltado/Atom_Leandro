strg = lambda x: x[round((len(x)/2)+0.1)-1] if len(x) % 2 == 1 else ''
print(strg('SQL'))
