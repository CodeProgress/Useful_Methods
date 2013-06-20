def fibMemo(x, fibDict = {}):
    '''returns Fibonacci sequence recursively using memoization
    x: int <= 995 (for higher, set recursion limit > x)
    This is for educational purposes
    in real life fib would be implemented iteratively
    '''
    if x == 0: return 0
    if x == 1: return 1

    if x in fibDict:
        return fibDict[x]
    
    fibDict[x] = fibMemo(x-1) + fibMemo(x-2)
    
    return fibMemo(x, fibDict)
