import time

def time_it(func):
  def wrapper(*args):
      start = time.clock()
      func(*args)
      return time.clock() - start
  return wrapper


@time_it
def naive_exp(base, exp):
    if exp == 0:
        return 1
    return base * naive_exp(base, exp -1)

@time_it
def fast_exp(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        return fast_exp(base, exp/2)**2
    return base * fast_exp(base, exp -1)

@time_it
def built_in_exp(base, exp):
    return base**exp
    
print sum(naive_exp(x,x) for x in range(300))
print sum(fast_exp(x,x) for x in range(300))
print sum(built_in_exp(x,x) for x in range(300))
