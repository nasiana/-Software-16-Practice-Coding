"""
EXAMPLE SOLUTION FOR 3 LARGEST NUMBERS WITHOUT SORTING

Check test cases below to test your code
"""

def find_3_largest_nums(array):
    three_largest = [None, None, None]
    for num in array:
        update_largest(three_largest, num)
    return three_largest


def update_largest(three_largest, num):
    if three_largest[2] is None or num > three_largest[2]:
        shift_n_update(three_largest, num, 2)
    elif three_largest[1] is None or num > three_largest[1]:
        shift_n_update(three_largest, num, 1)
    elif three_largest[0] is None or num > three_largest[0]:
        shift_n_update(three_largest, num, 0)


def shift_n_update(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]


#########################################################################

# Case 1, result = [18, 141, 541]

# array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
# print(find_3_largest_nums(array))

#####################################################

# Case 2, result = [8, 8, 10]
# array = [8, 8, 8, 8, 8, 8, 8, 8, 10, 8, 8, 8, 8, 8]
# print(find_3_largest_nums(array))

#####################################################

# Case 3, result = [1, 1, 1]
# array = [1, 1, 1, 1, 1, 1, 1, 1]
# print(find_3_largest_nums(array))

####################################################

# Case 4, result = [-2, -1, 7]
# array = [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]
# print(find_3_largest_nums(array))

####################################################
