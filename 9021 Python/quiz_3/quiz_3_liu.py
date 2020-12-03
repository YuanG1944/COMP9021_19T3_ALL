# Written by *** and Eric Martin for COMP9021

# Reading the number written in base 8 from right to left,
# keeping the leading 0's, if any:
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
#
# We start from a position that is the unique position
# where the switch is on.
#
# Moving to a position switches on to off, off to on there.

import sys

on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
     )

# INSERT YOUR CODE HERE
#step 1： 八进制数转换list
def direction(e,ori,list): #e表示移动方向,list类型
    moves = { 0:(0,1),1:(1,1),2:(1,0),3:(-1,-1),4:(0,-1),5:(-1,-1),6:(-1,0),7:(-1,1)}
    x,y = ori
    print(ori)
    dx,dy = moves[e]
    x += dx
    y += dy
    ori =(x,y)
    list.append(ori)
    return ori
    #print((x,y))


def switch(e,list):
    if e in list:
        #print('sww')
        for i in range(0,len(list) - 1):
            if e == list[i]:
                print('switch')
                list.remove(e)
                list.remove(e)
                break



def sys_out():
    (x1, y1) = list2[0]
    x_max,y_max = (x1,y1)
    x_min,y_min = (x1,y1)
    if list2:
        for (xn,yn) in list2:
            print(xn,yn)
           # tem = list2[i]
            #xn = tem[0]
           # yn = tem[1]
            if x_max < xn: x_max = xn;print(x_max)
            if y_max < yn: y_max = yn;print(y_max)
            if x_min > xn: x_min = xn
            if y_min > yn: y_min = yn
        out_len_x = x_max - x_min + 1
        out_len_y = y_max - y_min + 1
        print(out_len_x,out_len_y)
        x,y = (x_min,y_max)
        #print(x_min,y_max)
        for j in range(0,out_len_y):
            for i in range(0,out_len_x):
                #print((x,y))
                if (x,y) in list2:
                    #print('woshinidie')
                    print('\u26aa',end='')
                else: print('\u26ab',end='')
                x = x + 1
            y = y - 1
            x = x_min
            print('')

code1 = int(code)
print('code=',code1)
list1 = []

list2 = []
ori = (0,0)
list2.append(ori)
x = 0
while True:
    x = code1 % 8
    list1.append(x)
    code1 = code1 // 8
    if code1 == 0: break
if nb_of_leading_zeroes != 0:
    list1.append(0 * nb_of_leading_zeroes)
print(list1)
for i in list1:
    ori = direction(i,ori,list2)
    switch(ori,list2)
    print (ori)
print(list2)
sys_out()