
import random

def radix_sort(aList, base = 10):
    """sorts aList in place and returns it.
    aList:  list of positive ints
    """
    #handle trivial cases
    if len(aList) < 2:
        return aList
    
    #build a list of lists, with indices 0-9
    nums = [[] for x in range(base)]
    
    #values for mod and integer division used to isolate place digits
    size = base
    div  = 1
    
    #ending condition, when size is an order of magnitude higher than max val
    maxNumDigits = len(str(max(aList)))
    
    while len(str(size)) <= maxNumDigits + 1:

        for i in aList:
            #isolate digit in the "divs" place (ones place, tens place...)
            x = (i % size)/div
            
            #append the whole number to the xth index of nums
            nums[x].append(i)
        
        #join together all lists in nums, order matters!
        aList = reduce(lambda x, y: x + y, nums)           
        
        #reset nums
        nums = [[] for x in range(base)]
        
        #increase size and div by order of magnitude
        size *= base
        div  *= base

    return aList
    

######## Tests ########

test1 = random.sample(xrange(10000), 10000)
test2 = []
test3 = [0]
test4 = [1]
test5 = [1,2,3,4]

for i in [test1, test2, test3, test4, test5]:
    assert radix_sort(i) == sorted(i)


