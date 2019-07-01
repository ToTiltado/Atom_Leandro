palavra = str(input('Qual e a sua palavra? '))
def vogais(str):
    return [x for x in str if x.lower() in ['a', 'e', 'i' 'o', 'u']]
print(vogais(palavra))
