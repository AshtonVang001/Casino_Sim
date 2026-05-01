from blackJackRules import Rules

class Simulation(Rules):
    def __init__ (self, test):
        self.test = test


    r = Rules()
    r.money = int(input("Enter your buy in: "))

