def cat_dog(s):
    a = s.count('dog')
    b = s.count('cat')
    if a == b:
        return True
    else:
        return False
print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('catxxdogxxxdog'))
print(cat_dog('catxdogxdogxcat'))
