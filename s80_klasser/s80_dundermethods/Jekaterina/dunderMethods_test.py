import unittest
from dunderMethods import *

förnamn = Förnamnet("Albus")
efternamn = Efternamnet("Dumbledore")
fullnamn = FullNamnet()

assert(str(förnamn) == "Albus")
assert(str(efternamn) == "Dumbledore")
assert(fullnamn.__add__() == "Albus Dumbledore")

efternamn + förnamn
