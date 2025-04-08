# # Linear search
# def get_key_index(key):
#     for num in range(len(lst)):
#         if lst[num] == key:
#             return num
#         continue
#
# lst = [2,4,1,5,8,9]
#
# print(get_key_index(4))


# Binary Search

def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if number_to_find > mid_number:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

def find_all_occurances(numbers, number_to_find):
    index = binary_search(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >=0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i<len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)

numbers_list = [12, 15, 15, 15, 17, 19, 21, 24, 45, 67]

number_to_find = int(input("Enter the number to find: "))

Index = find_all_occurances(numbers_list, number_to_find)
Recurssive_Index = binary_search_recursive(numbers_list, number_to_find, 0,3)

print(f"Number found at index {Index}")
# print(f"Number found at index {Recurssive_Index}")

