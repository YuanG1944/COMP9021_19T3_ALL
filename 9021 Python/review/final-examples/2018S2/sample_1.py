import itertools as tool
def remove_consecutive_duplicates(word):
    '''
    >>> remove_consecutive_duplicates('')
    ''
    >>> remove_consecutive_duplicates('a')
    'a'
    >>> remove_consecutive_duplicates('ab')
    'ab'
    >>> remove_consecutive_duplicates('aba')
    'aba'
    >>> remove_consecutive_duplicates('aaabbbbbaaa')
    'aba'
    >>> remove_consecutive_duplicates('abcaaabbbcccabc')
    'abcabcabc'
    >>> remove_consecutive_duplicates('aaabbbbbaaacaacdddd')
    'abacacd'
    '''
    # Insert your code here (the output is returned, not printed out)
    '''b = []
    word = word + '!'
    #word = list(word)
    for x, y in zip(word, word[1:]):
        if x != y:
            b.append(x)
    b = ''.join(b)
    print(f'\'{b}\'')'''
    a = ''.join([x for x, y in tool.groupby(word)])
    print(f"\'{a}\'")

if __name__ == '__main__':
    import doctest
    doctest.testmod()

