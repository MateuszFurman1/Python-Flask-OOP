def find_boundaries(numbers_list):
    my_list = []
    if numbers_list == []:
        return None
    else:
        my_list.append(min(numbers_list))
        my_list.append(max(numbers_list))
    return tuple(my_list)
print(find_boundaries([-1, 5, 6, 8]))

def find_boundaries_1(numbers_list_1):
    if numbers_list_1 == []:
        return None
    else:
        x = sorted(list(numbers_list_1))
        y = [x[0],  x[-1]]
        return tuple(y)
print(find_boundaries_1([-1, 5, 6, 8]))