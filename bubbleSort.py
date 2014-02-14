
import random

def bubble_sort(aList):
    """Sorts aList in place and returns it, O(n**2)
    Great for "almost sorted" lists.
    """
    if len(aList) < 2:
        return aList

    end = len(aList) - 1
    while end:
        #move largest val to end
        start = 0
        while start < end:
            if aList[start] > aList[start+1]:
                #swap                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                aList[start], aList[start+1] = aList[start+1], aList[start]
            start += 1
        end -= 1
    return aList


######## Tests ########

test1 = random.sample(xrange(1000), 1000)
test2 = []
test3 = [0]
test4 = [1]
test5 = [-1]
test6 = [-1, 0, 1]

for i in [test1, test2, test3, test4, test5, test6]:
    assert bubble_sort(i) == sorted(i)

