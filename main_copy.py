from copy import copy, deepcopy

# lst = [1, 2, 3, 4, 5]
# lst_two = copy(lst)

# lst[1] = 9

# print(lst)
# print(lst_two)

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# lst_two = copy(lst)
lst_two = deepcopy(lst)

lst[0][1] = 9

print(lst)
print(lst_two)
