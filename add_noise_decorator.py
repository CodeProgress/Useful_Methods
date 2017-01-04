import random


def add_noise(get_value):
    def inner(*args, **kwargs):
        noise = (random.random()*2)-1
        return get_value(*args, **kwargs) + noise
    return inner

@add_noise
def random_value(low, high):
    return random.randint(low, high)
    

print random_value(1, 10)
