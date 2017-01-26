
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



rand_list = range(100)
random.shuffle(rand_list)

print quick_sort(rand_list) == sorted(rand_list) 
