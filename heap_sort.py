import heapq
import random

def heap_sort(iterable):
    """Equivalent to sorted(iterable)
    Source:  http://docs.python.org/2/library/heapq.html
    """
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]



######## Tests ########

test1 = random.sample(xrange(10000), 10000)
test2 = []
test3 = [0]
test4 = [1]
test5 = [-1]
test6 = [-1, 0, 1]

for i in [test1, test2, test3, test4, test5, test6]:
    assert heap_sort(i) == sorted(i)
