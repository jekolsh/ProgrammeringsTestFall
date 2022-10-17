import unittest
from arv import Fisk
from arv import Gädda
from arv import Aborre

enFisk = Fisk()
enGädda = Fisk()
enAborre = Aborre()

assert(type(enFisk) == Fisk)
assert(isinstance(enGädda, Fisk))
assert(isinstance(enAborre, Fisk))
assert(type(enGädda) == Gädda)