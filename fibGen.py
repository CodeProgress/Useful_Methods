def fibGen():
    '''Generator, yields Fibonacci sequence: 0,1,1,2,3,5,8...
    '''
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
