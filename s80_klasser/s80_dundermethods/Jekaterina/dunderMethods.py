class Förnamnet:
    def __init__(self, förnamnet):
        self.förnamnet = förnamnet
    def __str__(self):
        return self.förnamnet

class Efternamnet:
    def __init__(self,efternamnet):
        self.efternamnet = efternamnet
    def __str__(self):
        return self.efternamnet
       

class FullNamnet(Förnamnet, Efternamnet):
    def __add__(self, other):
        self.other = other
        # Förnamnet.__init__(self.Förnamnet, self.Efternamnet)
        # FullNamnet = self.other + self.efternamnet + self.förnamnet
        FullNamnet = other._add__(Förnamnet, Efternamnet)
        return FullNamnet