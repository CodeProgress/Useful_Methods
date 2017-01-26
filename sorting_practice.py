
import random

def quick_sort(a_list):
    # Base case
    if len(a_list) <= 1:
        return a_list
    pivot = random.randint(0, len(a_list)-1)
    pivot_value = a_list[pivot]
    lower = []
    eq = []
    higher = []

    for i in a_list:
        if i < pivot_value:
            lower.append(i)
        elif i > pivot_value:
            higher.append(i)
        else:
            eq.append(i)

    # Recursive step
    return quick_sort(lower) + eq + quick_sort(higher)

def merge_sort(a_list):
    # Base case
    if len(a_list) <= 1:
        return a_list
    mid = len(a_list)/2

    # Recursive steps
    left = merge_sort(a_list[:mid])
    right = merge_sort(a_list[mid:])
    
    # Continue execution
    sorted_list = []
    left_i = 0
    right_i = 0
    while True:
        if left[left_i] < right[right_i]:
            sorted_list.append(left[left_i])
            left_i += 1
        else:
            sorted_list.append(right[right_i])
            right_i += 1

        if left_i == len(left):
            sorted_list += right[right_i:]
            break
        elif right_i == len(right):
            sorted_list += left[left_i:]
            break

    return sorted_list

rand_list = range(100)
random.shuffle(rand_list)

print quick_sort(rand_list) == merge_sort(rand_list) == sorted(rand_list) 
