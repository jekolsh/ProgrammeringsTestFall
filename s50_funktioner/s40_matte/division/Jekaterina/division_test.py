import unittest
from division_func import division

assert(callable(division))
assert(division(12, 2) == 6)
assert(division(10, 5) == 2)
assert(division(21, 3) == 7)