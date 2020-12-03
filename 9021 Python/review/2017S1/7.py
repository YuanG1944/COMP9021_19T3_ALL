''' ord(c) returns the encoding of character c.
    chr(e) returns the character encoded by e.
'''
def f(n):
    '''
    >>> f(1)
    A
    >>> f(2)
     A
    CBC
    >>> f(3)
      A
     CBC
    EDCDE
    >>> f(4)
       A
      CBC
     EDCDE
    GFEDEFG
    >>> f(30)
                                 A
                                CBC
                               EDCDE
                              GFEDEFG
                             IHGFEFGHI
                            KJIHGFGHIJK
                           MLKJIHGHIJKLM
                          ONMLKJIHIJKLMNO
                         QPONMLKJIJKLMNOPQ
                        SRQPONMLKJKLMNOPQRS
                       UTSRQPONMLKLMNOPQRSTU
                      WVUTSRQPONMLMNOPQRSTUVW
                     YXWVUTSRQPONMNOPQRSTUVWXY
                    AZYXWVUTSRQPONOPQRSTUVWXYZA
                   CBAZYXWVUTSRQPOPQRSTUVWXYZABC
                  EDCBAZYXWVUTSRQPQRSTUVWXYZABCDE
                 GFEDCBAZYXWVUTSRQRSTUVWXYZABCDEFG
                IHGFEDCBAZYXWVUTSRSTUVWXYZABCDEFGHI
               KJIHGFEDCBAZYXWVUTSTUVWXYZABCDEFGHIJK
              MLKJIHGFEDCBAZYXWVUTUVWXYZABCDEFGHIJKLM
             ONMLKJIHGFEDCBAZYXWVUVWXYZABCDEFGHIJKLMNO
            QPONMLKJIHGFEDCBAZYXWVWXYZABCDEFGHIJKLMNOPQ
           SRQPONMLKJIHGFEDCBAZYXWXYZABCDEFGHIJKLMNOPQRS
          UTSRQPONMLKJIHGFEDCBAZYXYZABCDEFGHIJKLMNOPQRSTU
         WVUTSRQPONMLKJIHGFEDCBAZYZABCDEFGHIJKLMNOPQRSTUVW
        YXWVUTSRQPONMLKJIHGFEDCBAZABCDEFGHIJKLMNOPQRSTUVWXY
       AZYXWVUTSRQPONMLKJIHGFEDCBABCDEFGHIJKLMNOPQRSTUVWXYZA
      CBAZYXWVUTSRQPONMLKJIHGFEDCBCDEFGHIJKLMNOPQRSTUVWXYZABC
     EDCBAZYXWVUTSRQPONMLKJIHGFEDCDEFGHIJKLMNOPQRSTUVWXYZABCDE
    GFEDCBAZYXWVUTSRQPONMLKJIHGFEDEFGHIJKLMNOPQRSTUVWXYZABCDEFG
    '''
    if n <1:
        return
    #print(matrix)
    '''kk = n // 26
    aph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for value in range(kk + 1):
        aph = aph + aph
    for num in range(n):
        k = num
        temp = aph[k:k+k+1]
        tempr = temp[::-1]
        if len(temp) == 1:
            print(' ' * (n - len(temp)) + temp)
        else:
            print(' ' * (n - len(temp)) + tempr + temp[1:])'''
    
    word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    kk = n // 26
    for value in range(kk + 1):
        word = word + word
    for num in range(n):
        k = num
        temp = word[k:k+k+1]
        rtemp = temp[::-1]
        if len(temp) == 1:
            print(' ' * (n - len(temp)) + temp)
        else:
            print(' ' * (n - len(temp)) + rtemp + temp[1:])
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # f(3)
