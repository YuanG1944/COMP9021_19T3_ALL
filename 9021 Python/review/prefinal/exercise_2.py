
def rearrange(L, from_first = True):
    '''
    Returns a new list consisting of:
    * in case "from_first" is True:
         L's first member if it exists, then
         L's last member if it exists, then
         L's second member if it exists, then
         L's second last member if it exists, then
         L's third member if it exists...
    * in case "from_first" is False:
         L's last member if it exists, then
         L's first member if it exists, then
         L's second last member if it exists, then
         L's second member if it exists, then
         L's third last member if it exists...

    >>> L = []
    >>> rearrange(L), L
    ([], [])
    >>> L = [10]
    >>> rearrange(L, False), L
    ([10], [10])
    >>> L = [10, 20]
    >>> rearrange(L), L
    ([10, 20], [10, 20])
    >>> L = [10, 20, 30]
    >>> rearrange(L), L
    ([10, 30, 20], [10, 20, 30])
    >>> L = [10, 20, 30, 40]
    >>> rearrange(L, False), L
    ([40, 10, 30, 20], [10, 20, 30, 40])
    >>> L = [10, 20, 30, 40, 50]
    >>> rearrange(L, False), L
    ([50, 10, 40, 20, 30], [10, 20, 30, 40, 50])
    >>> L = [10, 20, 30, 40, 50, 60]
    >>> rearrange(L), L
    ([10, 60, 20, 50, 30, 40], [10, 20, 30, 40, 50, 60])
    >>> L = [10, 20, 30, 40, 50, 60, 70]
    >>> rearrange(L), L
    ([10, 70, 20, 60, 30, 50, 40], [10, 20, 30, 40, 50, 60, 70])
    '''
    l1 = L
    k = []
    if from_first:
        if len(l1) % 2 == 0:
            a = int(len(l1) / 2)
            l2 = l1[::-1]
            for num in range(a):
                k.append(l1[num])
                k.append(l2[num])
            return k
        else:
            a = int(len(l1) // 2)
            l2 = l1[::-1]
            for num in range(a+1):
                k.append(l1[num])
                k.append(l2[num])
            return k[:-1]
    else:
        if len(l1) % 2 == 0:
            a = int(len(l1) / 2)
            l2 = l1[::-1]
            for num in range(a):
                k.append(l2[num])
                k.append(l1[num])
            return k
        else:
            a = int(len(l1) // 2)
            l2 = l1[::-1]
            for num in range(a+1):
                k.append(l2[num])
                k.append(l1[num])
            return k[:-1]
            
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
