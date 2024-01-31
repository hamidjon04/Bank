IDs = [i for i in range(1000, 10000)]
class Mijoz:
    def __init__(self, name, nomer):
        self.name = name
        self.ID = IDs.pop(0)
        self.__balance = 0
        self.nomer = nomer
        self.kredit = 0

    def getBalance(self):
        return self.__balance
    
    def depozit(self, summa):
        self.__balance += summa * 1.1
    
    def setBalance(self, summa):
        self.__balance += summa

        