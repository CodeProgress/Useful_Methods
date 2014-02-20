
#use @time_it to time a function

import time

def time_it(func):
  def wrapper(*args):
      start = time.clock()
      func(*args)
      return time.clock() - start

  return wrapper


@time_it
def factorial_1(x):
    if x <= 1:
        return 1
    return reduce(lambda x, y: x*y, xrange(1, x+1))

@time_it
def factorial_2(x):
    if x <= 1:
        return 1
    result = 1
    while x > 1:
        result *= x
        x -= 1
    return result

print factorial_1(10000)
print factorial_2(10000)


