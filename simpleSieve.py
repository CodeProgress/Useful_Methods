def simpleSieve(limit):
    '''returns a list of all primes <= limit
    limit: positive integer
    sacrifices speed for readability
    '''
    limit += 1
    knownPrimes = [0 for x in xrange(limit)]
    primes = []
    for posPrime in xrange(2, limit):
        if not knownPrimes[posPrime]:
            primes.append(posPrime)
            for primeMultiple in xrange(posPrime, limit, posPrime):
                knownPrimes[primeMultiple] = 1
    return primes
    
