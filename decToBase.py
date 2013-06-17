def decToBase(n, b, iterCounter = 0):
    '''converts n (base 10) to base b, returns result as a string
    n: int >= 0
    b: 2 <= int <= 16
    iterCounter: default 0.  Change to 1 if you do not want to test input.
    recursive implementation
    testing this method using built in method int('num', base):
        False not in [int(decToBase(i, x),x) == i \
            for i in range(1,50000,37) for x in range(2,16)]
    '''
    #check test conditions only on first iteration
    if iterCounter == 0:
        assert n >= 0 and 2 <= b <= 16 and type(n) in [int, long]

    #base case
    if n == 0:
        return ''
    
    digits = "0123456789ABCDEF"
    return decToBase(n/b, b, 1) + digits[n%b]
