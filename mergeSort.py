#merge sort, annotated

#for testing
import random

#main function
def merge_sort(aList):
    """returns a new list with the values in aList sorted low to high
    recursively slices aList into two lists and applies merge(left, right)
    """
    
    #base case
    if len(aList) < 2: 
        return aList
    
    #else split into two lists
    middle = len(aList) / 2
    left   = merge_sort(aList[:middle])
    right  = merge_sort(aList[middle:])
    
    #merge these two lists
    return merge(left, right)

#helper function
def merge(left, right):
    """returns a sorted list of the values within left and right
    left, right:  sorted lists
    """
    result = []        #New list to hold merged values
    LP     = 0         #Left  Pointer
    RP     = 0         #Right Pointer
    
    #keep comparing values until one list is completely scanned
    while LP < len(left) and RP < len(right):

        #get values from each list to compare
        leftVal  = left[LP]
        rightVal = right[RP]
        
        #compare values
        if leftVal < rightVal:
            result.append(leftVal)
            LP += 1
        else:
            result.append(rightVal)
            RP += 1 
            
    #one list will be scanned before the other, simply add its remaining vals
    #(done to both lists for simplicity, since list.append([]) has no effect)
    result += left[LP:]
    result += right[RP:]

    return result
    


######## Tests ########

test1 = random.sample(xrange(10000), 10000)
test2 = []
test3 = [0]
test4 = [1]
test5 = [-1]
test6 = [-1, 0, 1]

for i in [test1, test2, test3, test4, test5, test6]:
    assert merge_sort(i) == sorted(i)

