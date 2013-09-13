def peekAheadIter(iterable):
    '''Creates an iterator out of iterable and yields tuples of form: (item, next item)
    the final iteration will yield (last item, None)
    example: 
    >>>for i in peekAheadIter(range(5)): print i
    (0, 1)
    (1, 2)
    (2, 3)
    (3, 4)
    (4, None)
    '''
    iterator = iter(iterable)
    cur = iterator.next()
    for peek in iterator:
        yield (cur, peek)
        cur = peek
    yield (cur, None)