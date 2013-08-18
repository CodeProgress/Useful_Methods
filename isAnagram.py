from collections import Counter
def isAnagram(x, y, caseSen = False):
    '''returns True if x and y are anagrams - False otherwise
    x, y: strings
    caseSen: Boolean, default False (not case sensitive) 
    set to True to make comparison case sensitive
    '''
    if len(x) != len(y): return False #saves time for trivial cases

    if caseSen:    
        return Counter(x) == Counter(y)

    return Counter(x.lower()) == Counter(y.lower())