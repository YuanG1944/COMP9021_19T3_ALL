# You might find the ord() function useful.

def longest_leftmost_sequence_of_consecutive_letters(word):
    '''
    You can assume that "word" is a string of
    nothing but lowercase letters.
    
    >>> longest_leftmost_sequence_of_consecutive_letters('')
    ''
    >>> longest_leftmost_sequence_of_consecutive_letters('a')
    'a'
    >>> longest_leftmost_sequence_of_consecutive_letters('zuba')
    'z'
    >>> longest_leftmost_sequence_of_consecutive_letters('ab')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('bcab')
    'bc'
    >>> longest_leftmost_sequence_of_consecutive_letters('aabbccddee')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('aefbxyzcrsdt')
    'xyz'
    >>> longest_leftmost_sequence_of_consecutive_letters('efghuvwijlrstuvabcde')
    'rstuv'
    '''
    if word == '':
        print("''")
    if word:
        word = word + "#"
        asc = []
        for value in word:
            asc.append(ord(value))
        
        temp = []
        a = []
        for x, y in zip(asc, asc[1:]):
            if x + 1 == y:
                temp.append(x)
            else:
                temp.append(x)
                a.append(temp)
                temp = []
        mm = 0
        for value in a:
            if len(value) > mm:
                mm = len(value)
        for value in a:
            if len(value) == mm:
                k = value
                break
        f = []
        for value in k:
            f.append(chr(value))
        f = ''.join(f)
        print("'" + f + "'")
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
