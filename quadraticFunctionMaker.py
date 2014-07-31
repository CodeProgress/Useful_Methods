
def make_quadratic_function(a, b, c):
    """returns a function that uses a, b and c as constants in ax^2 + bx + c
    the returned function takes one param: x
    ex:  test    = make_quadratic_function(1,2,3)
         test(4) = 27
    since ((1)(4))^2 + (2)(4) + 3 = 27
    """
    def quad(x, verbose = False):
        axsq = (a*x)**2
        bx   = (b*x)
        if verbose:
            print "a = {}, b = {}, c = {}".format(a, b, c)
            print "ax^2 = {}, bx = {}".format(axsq, bx)
            print "ax^2 + bx + c = {}".format(axsq + bx + c)
        return axsq + bx + c 
    return quad


test = make_quadratic_function(1,2,3)
assert test(1) == 6
assert test(2) == 11
assert test(3) == 18
print test(4, True)
