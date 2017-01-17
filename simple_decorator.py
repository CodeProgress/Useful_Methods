def simple_decorator(afunc):
    def wrapper(*args):
        print "Wrapped top!"
        afunc(*args)
        print "Wrapped bottom"
    return wrapper

@simple_decorator
def test(message):
    print message

test("Hello!")
