# COMP9021 19T3 - Rachid Hamadi
# Sample Exam Question 8


'''
Will be tested with letters a string of DISTINCT UPPERCASE letters only.
'''

import itertools as tool

def f(letters):
    '''
    >>> f('ABCDEFGH')
    There is no solution
    >>> f('GRIHWSNYP')
    The pairs of words using all (distinct) letters in "GRIHWSNYP" are:
    ('SPRING', 'WHY')
    >>> f('ONESIX')
    The pairs of words using all (distinct) letters in "ONESIX" are:
    ('ION', 'SEX')
    ('ONE', 'SIX')
    >>> f('UTAROFSMN')
    The pairs of words using all (distinct) letters in "UTAROFSMN" are:
    ('AFT', 'MOURNS')
    ('ANT', 'FORUMS')
    ('ANTS', 'FORUM')
    ('ARM', 'FOUNTS')
    ('ARMS', 'FOUNT')
    ('AUNT', 'FORMS')
    ('AUNTS', 'FORM')
    ('AUNTS', 'FROM')
    ('FAN', 'TUMORS')
    ('FANS', 'TUMOR')
    ('FAR', 'MOUNTS')
    ('FARM', 'SNOUT')
    ('FARMS', 'UNTO')
    ('FAST', 'MOURN')
    ('FAT', 'MOURNS')
    ('FATS', 'MOURN')
    ('FAUN', 'STORM')
    ('FAUN', 'STROM')
    ('FAUST', 'MORN')
    ('FAUST', 'NORM')
    ('FOAM', 'TURNS')
    ('FOAMS', 'RUNT')
    ('FOAMS', 'TURN')
    ('FORMAT', 'SUN')
    ('FORUM', 'STAN')
    ('FORUMS', 'NAT')
    ('FORUMS', 'TAN')
    ('FOUNT', 'MARS')
    ('FOUNT', 'RAMS')
    ('FOUNTS', 'RAM')
    ('FUR', 'MATSON')
    ('MASON', 'TURF')
    ('MOANS', 'TURF')
    '''
    dictionary = 'dictionary.txt'
    solutions = []
    # Insert your code here
    # with open(dictionary) as dicc:
    #     valid_word = set()
    #     for value in dicc:
    #         valid_word.add(value.rstrip())
    #
    # for length in range(len(letters)):
    #     a = tool.permutations(letters, length)
    #     for value in a:
    #         k = ''.join(value)
    #         if k in valid_word:
    #             b = set(letters) - set(k)
    #             b2 = tool.permutations(b, len(letters) - length)
    #             for value2 in b2:
    #                 k2 = ''.join(value2)
    #                 if k2 in valid_word and k < k2:
    #                     solutions.append((k, k2))
    # solutions = sorted(solutions)
    with open("dictionary.txt") as dicc:
        valid_word = set()
        for value in dicc:
            valid_word.add(value.rstrip())
    for length in range(len(letters)):
        a = tool.permutations(letters, length)
        for value in a:
            w1 = ''.join(value)
            if w1 in valid_word:
                b = set(letters) - set(w1)
                b2 = tool.permutations(b, len(letters) - length)
                for value2 in b2:
                    w2 = ''.join(value2)
                    if w2 in valid_word and w1 < w2:
                        solutions.append((w1, w2))
    solutions = sorted(solutions)

        
    if not solutions:
        print('There is no solution')
    else:
        print(f'The pairs of words using all (distinct) letters in "{letters}" are:')
        for solution in solutions:
            print(solution)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
