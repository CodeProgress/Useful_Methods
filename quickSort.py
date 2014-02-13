
import random

def quick_sort(aList, rand = False):

    #base case
    if len(aList) < 2:
        return aList
    
    #pick pivot value
    if rand:
        randIndex = random.randint(0, len(aList)-1)
        pivotVal  = aList[randIndex]
    else:
        pivotVal = aList[0]
    
    #separate values by comparing to pivot value
    smaller  = []
    larger   = []
    equal    = []
    
    for i in aList:
        if    i < pivotVal: smaller.append(i)
        elif  i > pivotVal: larger.append(i)
        else              : equal.append(i)
    
    #quicksort the lists of smaller and larger vals and join everything together
    return quick_sort(smaller) + equal + quick_sort(larger)

 

######## Tests ########

test1 = random.sample(xrange(10000), 10000)
test2 = []
test3 = [0]
test4 = [1]
test5 = [-1]
test6 = [-1, 0, 1]

for i in [test1, test2, test3, test4, test5, test6]:
    assert quick_sort(i) == sorted(i)

