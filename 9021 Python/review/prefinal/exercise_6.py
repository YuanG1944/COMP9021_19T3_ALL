# ord(c) returns the encoding of character c.
# chr(e) returns the character encoded by e.


def rectangle(width, height):
    '''
    Displays a rectangle by outputting lowercase letters, starting with a,
    in a "snakelike" manner, from left to right, then from right to left,
    then from left to right, then from right to left, wrapping around when z is reached.
    
    >>> rectangle(1, 1)
    a
    >>> rectangle(2, 3)
    ab
    dc
    ef
    >>> rectangle(3, 2)
    abc
    fed
    >>> rectangle(17, 4)
    abcdefghijklmnopq
    hgfedcbazyxwvutsr
    ijklmnopqrstuvwxy
    ponmlkjihgfedcbaz
    '''
    word = 'abcdefghijklmnopqrstuvwxyz'
    a = width * height
    j = int(a // 26)
    k = int(a % 26)
    word = word * j + word[:k]
    new = [word[i: i + width] for i in range(0, len(word), width)]
    for num in range(len(new)):
        if num % 2:
            new[num] = new[num][::-1]
    for value in new:
        print(value)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
