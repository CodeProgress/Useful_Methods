import numpy # used only for testing


def change_probability_by_a_percentage(probability, percentage):
    assert -100 < percentage
    odds = convert_probability_to_odds(probability)
    newOdds = increase_odds_by_a_percentage(odds, percentage)
    newProbability = convert_odds_to_probabilitiy(newOdds)
    return newProbability
    

#helper function
def convert_probability_to_odds(probability):
    '''returns the odds in proportion to one. 
    i.e. X to Y, where Y = 1, this function returns X
    ex: probability=.8, odds = 4:1 --> returns 4.0
    if probability = 1, returns float('Inf')'''
    assert 0 <= probability <= 1, "Probability must be between 0 and 1, inclusive"
    try:
        return probability/(1.-probability)
    except ZeroDivisionError:
        return float('Inf')
    
#helper function
def increase_odds_by_a_percentage(odds, percentage):
    percentAsDecimal = percentage/100.

    return odds * (1.+percentAsDecimal)
    
#helper function
def convert_odds_to_probabilitiy(odds):
    if odds == float('Inf'):
        return 1.0
    return odds/(1.+odds)
            

def test_change_probability_by_a_percentage():
    methodToTest = change_probability_by_a_percentage
    # increase probability
    assert methodToTest(.5, 0) == .5
    assert methodToTest(.6, 100) == .75
    assert methodToTest(.1, 3000) == .775  
    assert methodToTest(1, 3000) == 1.0 
    assert methodToTest(1, 0) == 1.0
    assert methodToTest(1., 7) == 1.0 

    # decrease probability
    assert methodToTest(.5, -75) == .2
    assert methodToTest(.75, -50) == .6
    assert methodToTest(.1, -40) == .0625
    assert methodToTest(1, -10) == 1.0
    assert methodToTest(1., -7) == 1.0
    
    # compare to bayes_approach_change_probability_by_a_percentage
    tolerance = .000000001
    methodToTestAgainst = bayes_approach_change_probability_by_a_percentage
    for prob in numpy.arange(0.1, 1.1, .1):
        for perc in numpy.arange(-99.9,200,.1):
            assert abs(methodToTest(prob, perc) - methodToTestAgainst(prob, perc)) < tolerance
    

def bayes_approach_change_probability_by_a_percentage(probability, percentage):
    return probability/(probability+(((percentage/100.)+1)**-1)*(1-probability))

test_change_probability_by_a_percentage()


