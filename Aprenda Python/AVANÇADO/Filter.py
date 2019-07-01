def primo(n):
    for i in range(2, n):
       if n % i == 0:
            return False
    return n > 1
print(list(filter(primo, range(0,101))))
