def simpleSieve(limit):
    '''returns a list of all primes <= limit
    limit: positive integer
    sacrifices speed for readability
    '''
    sieve = [0 for x in xrange(limit + 1)]
    primes = []
    for posPrime in xrange(2, limit + 1):
        if sieve[posPrime] != 0:
            continue
        primes.append(posPrime)
        for multiple in xrange(posPrime*2, limit + 1, posPrime):
            sieve[multiple] = 1
    return primes
