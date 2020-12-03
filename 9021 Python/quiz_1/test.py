mapping = {2: 4, 3: 8, 4: 7, 5: 7}

one_to_one_part_of_mapping = {}
same = {}
for key, value in mapping.items():
    for key2, value2 in mapping.items():
        if key != key2 and value == value2:
            same[key] = value
for key in same.keys():
    mapping.pop(key)

one_to_one_part_of_mapping = mapping

print(one_to_one_part_of_mapping)
