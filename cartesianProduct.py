import Queue
import itertools

def search_space(iterable, length):
    '''returns the Cartesian product of iterable as a generator, repeat = length
    search_space('ab',2) -> [('a', 'a'), ('a', 'b'), ('b', 'a'), ('b', 'b')]
    implemented as modified version of BFS, using a deque
    equivalent to itertools.product(iterable, repeat = length) EXCEPT it builds
    the queue in memory and therefore is much less efficient
    '''
    if len(iterable) == 0:
        return ()

    q = Queue.deque()

    for i in iterable:
        q.append((i,))

    while True:
        x = q.popleft()
        if len(x) == length:
            q.appendleft(x)
            break
        for i in iterable:
            q.append(x+(i,))
    
    return (x for x in q)


assert [x for x in search_space('ab',2)] == \
        [x for x in itertools.product('ab', repeat=2)]

assert [x for x in search_space([1,2,3], 3)] == \
        [x for x in itertools.product([1,2,3], repeat=3)]

assert [x for x in search_space(['a','b','c'], 4)] == \
        [x for x in itertools.product(['a','b','c'], repeat=4)]

assert [x for x in search_space('',2)] == \
        [x for x in itertools.product('', repeat=2)]