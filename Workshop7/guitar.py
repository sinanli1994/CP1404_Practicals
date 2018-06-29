class Guitar:
    def __init__(self, name = "", year = 0, cost = 0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)
    "Gibson L-5 CES (1922) : $16,035.40"

    def get_age(self):
        return 2016-self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False

