class ATMCard:
    def __init__(self, defaultPIN, defaultBalance):
        self.defaultPIN = defaultPIN
        self.defaultBalance = defaultBalance
    
    def cekPinAwal(self):
        return self.defaultPIN
    
    def cekSaldoAwal(self):
        return self.defaultBalance
