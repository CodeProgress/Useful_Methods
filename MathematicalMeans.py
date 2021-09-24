import math


def arithmatic_mean(nums):
    ''' The sum divided by the count '''
    return sum(nums)/len(nums)

def geometric_mean(nums):
    ''' The nth root of the product of n numbers '''
    return math.pow(math.prod(nums), 1/len(nums))

def harmonic_mean(nums):
    ''' The reciprocal of the arithmetic mean of the reciprocals '''
    sum_recipricols = sum([1/x for x in nums])
    return 1/(sum_recipricols/len(nums))


assert arithmatic_mean([3, 4, 5]) == 4
assert geometric_mean([4, 1, 1/32]) == .5
assert harmonic_mean([1, 4, 4]) == 2
