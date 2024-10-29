# Dependencies
from functools import reduce
# The Data
s = {1, 2, 3, 4}
# The One-Liner
ps = lambda s: reduce(lambda P, x: P + [subset | {x} for subset in P], s, [set()])
# The Result
print(ps(s))