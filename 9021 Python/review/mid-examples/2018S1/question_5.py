

def f(word):
    '''
    Recall that if c is an ascii character then ord(c) returns its ascii code.
    Will be tested on nonempty strings of lowercase letters only.

    >>> f('x')
    The longest substring of consecutive letters has a length of 1.
    The leftmost such substring is x.
    >>> f('xy')
    The longest substring of consecutive letters has a length of 2.
    The leftmost such substring is xy.
    >>> f('ababcuvwaba')
    The longest substring of consecutive letters has a length of 3.
    The leftmost such substring is abc.
    >>> f('abbcedffghiefghiaaabbcdefgg')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is bcdefg.
    >>> f('abcabccdefcdefghacdef')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is cdefgh.
    '''
    asc_list = []
    temp = []
    b = []
    word = word + "#"
    for value in word:
        asc_list.append(ord(value))
    for x, y in zip(asc_list, asc_list[1:]):
        if x + 1 == y:
            temp.append(x)
        else:
            temp.append(x)
            b.append(temp)
            temp = []
    t = 0
    for value in b:
        if len(value) > t:
            t = len(value)
    for value in b:
        if len(value) == t:
            f = value
            break
    w = []
    for value in f:
        w.append(chr(value))
    w = ''.join(w)
    print(f"The longest substring of consecutive letters has a length of {len(w)}.")
    print(f"The leftmost such substring is {w}.")
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
