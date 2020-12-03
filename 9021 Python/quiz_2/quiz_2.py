# COMP9021 19T3 - Rachid Hamadi
# Quiz 2 *** Due Thursday Week 3


import sys
from random import seed, randrange
from pprint import pprint

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}

# INSERT YOUR CODE HERE
#-------------------------------------------------question1-------------------------------------------------------------
condition_list = []
cycle_list2 = []
def cycle_f(k):
    if mapping[k] in keys:
        condition_list.append(k)
        condition_list.append(mapping[k])
        if mapping[mapping[k]] not in condition_list:
            cycle_f(mapping[k])
    return condition_list

for num in range(len(keys)):
    condition_list = []
    cycle_f(keys[num])
    if condition_list != [] and mapping[condition_list[-1]] != condition_list[0]:
        condition_list = []
    else:
        l2 = list(set(condition_list))
        l2.sort(key=condition_list.index)
        if sorted(l2) not in cycle_list2 and l2 != []:
            cycle_list2.append(sorted(l2))
            cycles.append(l2)

#--------------------------------------------Question2------------------------------------------------------------------
def get_key(dict, value):
    return [k for k, v in dict.items() if v == value]

mapping_value = []
count_num = []

reversed_one_to_one_mapping = {}
same = {}
mapping2 = mapping.copy()
for key, value in mapping2.items():
    for key2, value2 in mapping2.items():
        if key != key2 and value == value2:
            same[key] = value
for key in same.keys():
    mapping2.pop(key)

for key, value in mapping2.items():
    reversed_one_to_one_mapping[value] = [key]
reversed_one_to_one_mapping = {key: reversed_one_to_one_mapping[key] for key in sorted(reversed_one_to_one_mapping)}

for key in mapping:
    mapping_value.append(mapping[key])

for value in range(len(mapping_value) - 1):
    count_num.append(mapping_value.count(mapping_value[value]))
count_num = sorted(count_num)

for value in count_num:
    reversed_dict_per_length[value] = {}

for num in range(len(mapping_value) - 1):
    count_num1 = (mapping_value.count(mapping_value[num]))
    for key, value in mapping.items():
        if count_num1 == 1:
            reversed_dict_per_length[count_num1] = reversed_one_to_one_mapping
        else:
            reversed_dict_per_length[count_num1][mapping_value[num]] = get_key(mapping, mapping_value[num])


print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)


