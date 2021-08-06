import atm_card

class Customer:
    def __init__(self, id, custPIN = 1234, custBalance = 100000):
        self.id = id
        self.pin = custPIN
        self.balance = custBalance
    
    def checkId(self):
        return self.id
    
    def checkPIN(self):
        return self.pin
    
    def checkBalance(self):
        return self.balance
    
    def withdrawBalance(self, nominal):
        self.balance -= nominal

    def depositBalance(self, nominal):
        self.balance += nominal
    



    