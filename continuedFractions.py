
import itertools

def continued_fraction(repList, depth = 20):
    """returns the decimal approximation of a repeated fraction to a depth
    if depth > len(repList), cycle continues back at repList[1] and repeats list
    
    repList:  list representation for repeating patterns ex: [1,2]
              or generator for infinite patterns
              
    depth: int < 1000 (or new recursion depth limit)
    """
    if depth <= 0: return 0
    
    if type(repList) == list:
        if len(repList) == 1: return 0
        if len(repList) == 1: return repList[0]
        firstTerm      = repList[0]
        repeatedTerms  = repList[1:]
        gen            = itertools.cycle(repeatedTerms)
        
    else:
        try:
            gen       = repList
            firstTerm = gen.next()
        except:
            raise ValueError("repList must be a list or generator")

    return  firstTerm + c_f_helper(gen, depth - 1)

def c_f_helper(gen, depth):
    if depth == 0:
        return 1./gen.next()

    return 1./(gen.next() + c_f_helper(gen, depth - 1))


def test(tolerance = 10**-8):
    def e_terms_gen():
        start = 2
        yield start
        while True: 
            yield 1
            yield start
            yield 1
            start += 2
    
    e           = e_terms_gen()
    root2       = [1,2]
    goldenRatio = [1,1]
    pi          = [3,7,15,1,292,1,1,1,2,1,3,1] #continues.. digit pattern random
    root19      = [4,2,1,3,1,2,8]
    
    assert abs(continued_fraction(e)           - 2.718281828459045) < tolerance
    assert abs(continued_fraction(root2)       - 2**.5)             < tolerance
    assert abs(continued_fraction(goldenRatio) - ((1+5**.5) /2))    < tolerance
    assert abs(continued_fraction(pi, len(pi)) - 3.141592653589793) < tolerance
    assert abs(continued_fraction(root19)      - 19**.5)            < tolerance


test()

