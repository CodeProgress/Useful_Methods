def binarySearch(aList, item):
    '''returns the index of item in aList if item is in aList, -1 otherwise
    aList:  sorted list of numbers
    item: a number
    '''

    low = 0
    high = len(aList) - 1

    while low <= high:
	    
        mid = low + (high-low)/2

        if item < aList[mid]:
            high = mid - 1

        elif item > aList[mid]:
            low = mid + 1

        else:
            return mid
    
    return -1
	


#Tests:

testListOne = range(100000)

assert binarySearch(testListOne, 58786) == 58786


testListTwo = [1,3,6,7,8,10,20,50,77,90,100,101,200,512,900,1000,1001]

assert binarySearch(testListTwo, 1) == 0
assert binarySearch(testListTwo, 3) == 1
assert binarySearch(testListTwo, 7) == 3
assert binarySearch(testListTwo, 100) == 10

assert binarySearch(testListTwo, 2) == -1
assert binarySearch(testListTwo, 1002) == -1
assert binarySearch(testListTwo, 0) == -1
assert binarySearch(testListTwo, 199) == -1


testListThree = [1.1,1.2, 1.3, 1.4, 1.5, 2.3, 9.9, 10.0]

assert binarySearch(testListThree, 1.1) == 0
assert binarySearch(testListThree, 1.2) == 1
assert binarySearch(testListThree, 10.0) == 7
#Note: Function will not differentiate between float and int
assert binarySearch(testListThree, 10) == 7


testListFour = [1,1,1,1,1]

#Note: if there are multiple occurrences, function does not find first occurrence
#it will just return a value that is not -1
assert binarySearch(testListFour, 1) != -1
assert binarySearch(testListFour, 2) == -1