# 12. New list from two lists
list1 = [10, 21, 4, 45, 66, 93]
list2 = [12, 14, 95, 3, 73, 6]
new_list = [x for x in list1 if x % 2 != 0] + [y for y in list2 if y % 2 == 0]
print("New list:", new_list)
