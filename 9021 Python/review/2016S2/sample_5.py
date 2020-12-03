import sys


def f(a, b):
    '''
    Finds all numbers i and j with a <= i <= j <= b such that:
    - i + j is even;
    - when read from left to right, the digits in i are strictly increasing
    - when read from left to right, the digits in j are strictly decreasing
    - when read from left to right, the digits in the average of i and j are
      either strictly increasing or strictly decreasing

    Outputs the solutions from smallest i to largest i,
    and for a given i from smallest j to largest j.
    
    >>> f(10, 20)
    12 and 20 with 16 as average
    14 and 20 with 17 as average
    16 and 20 with 18 as average
    18 and 20 with 19 as average
    >>> f(30, 50)
    34 and 40 with 37 as average
    34 and 42 with 38 as average
    34 and 50 with 42 as average
    35 and 41 with 38 as average
    35 and 43 with 39 as average
    36 and 40 with 38 as average
    36 and 42 with 39 as average
    36 and 50 with 43 as average
    37 and 41 with 39 as average
    37 and 43 with 40 as average
    38 and 40 with 39 as average
    38 and 42 with 40 as average
    39 and 41 with 40 as average
    39 and 43 with 41 as average
    46 and 50 with 48 as average
    48 and 50 with 49 as average
    >>> f(400, 700)
    456 and 630 with 543 as average
    457 and 521 with 489 as average
    458 and 520 with 489 as average
    459 and 621 with 540 as average
    468 and 510 with 489 as average
    478 and 542 with 510 as average
    479 and 541 with 510 as average
    489 and 531 with 510 as average
    567 and 653 with 610 as average
    568 and 610 with 589 as average
    568 and 652 with 610 as average
    569 and 651 with 610 as average
    578 and 642 with 610 as average
    579 and 641 with 610 as average
    589 and 631 with 610 as average
    589 and 651 with 620 as average
    589 and 653 with 621 as average
    '''
    up = []
    down = []
    avgl = []
    reslut_list = []
    for value in range(a, b + 1):
        str_num = str(value)
        temp_list = list(str_num)
        if all(x < y for x, y in zip(temp_list, temp_list[1:])):
            temp_str = ''.join(temp_list)
            up.append(int(temp_str))
        if all(x > y for x, y in zip(temp_list, temp_list[1:])):
            temp_str = ''.join(temp_list)
            down.append(int(temp_str))
    for i in up:
        for j in down:
            if i < j and (i + j) % 2 == 0:
                reslut_list.append([i, j])
    for value in reslut_list:
        av = int((value[0] + value[1]) / 2)
        avv = list(str(av))
        if all(x < y for x, y in zip(avv, avv[1:])) or all(x > y for x, y in zip(avv, avv[1:])) :
            avgl.append([value[0], value[1], av])   
    for x, y, z in avgl:
        print(f"{x} and {y} with {z} as average")
            
    '''up_list = []
    down_list = []
    result_list = []
    avg_list = []
    avg_list2 = []
    for value in range(a, b + 1):
        str_num = str(value)
        temp_list = list(str_num)
        if all(x < y for x, y in zip(temp_list, temp_list[1:])):
            temp_str1 = ''.join(temp_list)
            up_list.append(int(temp_str1))
        if all(x > y for x, y in zip(temp_list, temp_list[1:])):
            temp_str2 = ''.join(temp_list)
            down_list.append(int(temp_str2))
    #print(up_list)
    #print(down_list)
    for i in up_list:
        for j in down_list:
            if i < j and (i + j) % 2 == 0:
                result_list.append([i ,j])
    #print(result_list)
    for value in result_list:
        avg = (value[0] + value[1])/2
        avg_list.append(int(avg))
        
    for num in range(len(avg_list)):
        str_num2 = str(avg_list[num])
        temp_list2 = list(str_num2)
        if all(x < y for x, y in zip(temp_list2, temp_list2[1:])) or all(x > y for x, y in zip(temp_list2, temp_list2[1:])):
            avg_list2.append([num, avg_list[num]])
    #print(avg_list2)
    for x, y in avg_list2:
        print(f"{result_list[x][0]} and {result_list[x][1]} with {y} as average")'''
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
