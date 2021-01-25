# Maximum subarray problem
# https://en.wikipedia.org/wiki/Maximum_subarray_problem
# also known as: maximum sum problem, maximum sum subarray problem

import random


def max_sum_subarray_kadane(array):
    """returns the max sum of a contiguous subarray within array"""
    best_sum = float("-inf")
    current_sum = float("-inf")
    for val in array:
        current_sum = max(val + current_sum, val)
        best_sum = max(best_sum, current_sum)
    return best_sum


def max_sum_subarray_first_attempt(array):
    """returns the max sum of a contiguous subarray within array"""
    best = 0
    current_best = float("-inf")
    subarray_total = 0
    for val in array:
        if val + subarray_total < val:
            # reset total, simulates clearing out current subarray
            subarray_total = 0
        subarray_total += val
        if subarray_total > current_best:
            current_best = subarray_total
        if current_best > best:
            best = current_best
    return best


def max_sum_subarray_brute_force(array):
    max_sum = float("-inf")
    for i, val in enumerate(array):
        for j in range(i+1, len(array)):
            current_sum = sum(array[i:j+1])
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum


test_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # [4, −1, 2, 1],  sum 6
assert(6 == max_sum_subarray_first_attempt(test_array))
assert(6 == max_sum_subarray_kadane(test_array))
assert(6 == max_sum_subarray_brute_force(test_array))

test_array2 = [-20, 62, 48, 75, 52, 27, 81, 34, 83, -77]
assert(462 == max_sum_subarray_first_attempt(test_array2))
assert(462 == max_sum_subarray_kadane(test_array2))
assert(462 == max_sum_subarray_brute_force(test_array2))

test_array3 = [38, 18, 94, 90, -12, 56, -40, -30, -23, -7]
assert(284 == max_sum_subarray_first_attempt(test_array3))
assert(284 == max_sum_subarray_kadane(test_array3))
assert(284 == max_sum_subarray_brute_force(test_array3))

# randomized test
rand_array = random.sample(range(-300, 300), 300)

max_kadane_algo = max_sum_subarray_kadane(rand_array)
max_kadane_algo_first_attempt = max_sum_subarray_first_attempt(rand_array)
max_brute_force = max_sum_subarray_brute_force(rand_array)

assert(max_kadane_algo == max_kadane_algo_first_attempt == max_brute_force)
print(max_kadane_algo, max_kadane_algo_first_attempt, max_brute_force)
