
def f(N):
    '''
    >>> f(20)
    Here are your banknotes:
    $20: 1
    >>> f(40)
    Here are your banknotes:
    $20: 2
    >>> f(42)
    Here are your banknotes:
    $2: 1
    $20: 2
    >>> f(43)
    Here are your banknotes:
    $1: 1
    $2: 1
    $20: 2
    >>> f(45)
    Here are your banknotes:
    $5: 1
    $20: 2
    >>> f(2537)
    Here are your banknotes:
    $2: 1
    $5: 1
    $10: 1
    $20: 1
    $100: 25
    '''
    banknote_values = [1, 2, 5, 10, 20, 50, 100]
    banknotes = dict.fromkeys(banknote_values, 0)
    # Insert your code here
    print('Here are your banknotes:')
    m = str(N)
    g = int(m[-1])
    if  0 < g < 5:
        if g == 1:
            print(f'$1: 1')
        if g % 2 == 0:
            print(f'$2: {int(g / 2)}')
        else:
            print(f'$1: {int(g % 2)}')
            print(f'$2: {int(g // 2)}')
    if g == 5:
        print(f'$5: 1')
    if g > 5:
        g1 = g - 5
        if g1 % 2 == 0:
            print(f'$2: {int(g1 / 2)}')
            print(f'$5: 1')
        else:
            print(f'$1: {int(g1 % 2)}')
            print(f'$2: {int(g1 // 2)}')
            print(f'$5: 1')
    
    if N >= 10:
        s = int(m[-2])
        if s % 2 != 0:
            print(f'$10: {int(s % 2)}')
            print(f'$20: {int(s // 2)}')
        else:
            print(f'$20: {int(s / 2)}')
    if N >= 100:
        b = int(m[0:-2])
        s1 = s % 2
        print(f'$100: {b}')
    
                        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
