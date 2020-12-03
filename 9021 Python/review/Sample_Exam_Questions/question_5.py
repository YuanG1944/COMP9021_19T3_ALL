# COMP9021 19T3 - Rachid Hamadi
# Sample Exam Question 5


'''
Will be tested with year between 1913 and 2013.
You might find the reader() function of the csv module useful,
but you can also use the split() method of the str class.
'''

import csv

def f(year):
    '''
    >>> f(1914)
    In 1914, maximum inflation was: 2.0
    It was achieved in the following months: Aug
    >>> f(1922)
    In 1922, maximum inflation was: 0.6
    It was achieved in the following months: Jul, Oct, Nov, Dec
    >>> f(1995)
    In 1995, maximum inflation was: 0.4
    It was achieved in the following months: Jan, Feb
    >>> f(2013)
    In 2013, maximum inflation was: 0.82
    It was achieved in the following months: Feb
    '''
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    # Insert your code here
    year_list = []
    year_dic = {}
    m_list =[]
    with open('cpiai.csv') as data:
        content = list(map(list, csv.reader(data, delimiter=',')))
        for value in content[1:]:
            date = value[0][:4]
            if date == str(year):
                year_list.append(value)
        year_list = sorted(year_list, key= lambda x: x[2])
        for num in range(len(year_list)):
            k = year_list[-1][-1]
            if year_list[num][-1] == k:
                year_dic[year_list[num][0]] = k
        for key, value in year_dic.items():
            month = key[5:7]
            m = months[int(month) - 1]
            m_list.append(", " + m)
        mm = ''.join(m_list)
        print(f"In {year}, maximum inflation was: {k}")
        print(f"It was achieved in the following months: {mm[2:]}")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
