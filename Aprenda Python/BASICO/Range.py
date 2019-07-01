for r in range(0, 51):
    if r % 3 == 0 and r % 5 == 0 and r !=0:
        print('{} - FizzBuzz'.format(r))
    elif r % 3 == 0 and r != 0:
        print('{} - Fizz'.format(r))
    elif r % 5 == 0 and r != 0:
        print('{} - Buzz'.format(r))
    
