def sieve(limit):
    """returns a list of all primes less than or equal to limit
    limit: int
    """
    if limit < 2: 
        return []
    primes = [2]
    for i in range(3, limit+1):
        if all(i%p != 0 for p in primes): 
            primes.append(i)
    return primes



def sieve2(limit):
    """returns a list of all primes less than or equal to limit
    limit: int
    twice as fast as the sieve using built in "all" function
    """
    if limit < 2:
        return []
    primes = [2]
    for i in range(3, limit+1):
        flag = True
        for p in primes:
            if i%p == 0:
                flag = False
                break
        if flag:
            primes.append(i)
    return primes