
def fact(x):
    """fact_recursive rewritten using a while True loop
    to avoid reaching max recursion depth
    tail recursion optimization
    """
    ans = 1
    while True:
        if x <= 1:
            return ans
        x, ans = x - 1, x * ans

def fact_recursive(x):
    if x <= 1:
        return 1
    return x * fact_recursive(x - 1)

def fact_iter(x):
    ans = 1
    while x > 1:
        ans *= x
        x -= 1
    return ans

assert fact(10000) == fact_iter(10000)

#fact_recursive( 10000 )
#will reach max recursion depth after 1000 calls 
#unless depth manually changed:
#import sys
#sys.setrecursionlimit( newMaxDepth )
