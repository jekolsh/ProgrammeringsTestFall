import unittest
from enkelKlass import *

person = Person()
kvinna = Kvinna()
man = Man()

assert(isinstance(person, Person))

assert(isinstance(kvinna, Kvinna))
assert(str(kvinna) == "Kvinnor är snygga och snälla")
assert(kvinna.__str__() == "Kvinnor är snygga och snälla")
assert(isinstance(kvinna, Person))

assert(isinstance(man, Man))
assert(str(man) == "Män är starka och modiga")
assert(man.__str__() == "Män är starka och modiga")
assert(isinstance(man, Person))
