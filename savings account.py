
class Account:
    def __init__(self, balance, accno):
        self.balance = balance
        self.accno = accno

    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} debited, balance is {self.getbal()}")
        else:
            print("Insufficient funds")

    def credit(self, amount):
        self.balance += amount
        print(f"{amount} credited, balance is {self.getbal()}")

    def getbal(self):
        return self.balance


class SavingAccount(Account):
    def __init__(self, interest):
        self.interest = interest
        super().__init__(1000, "acc123")

    def interestrate(self):
        interest_amount = self.balance * (self.interest / 100)
        self.balance += interest_amount
        print("Balance after interest:", self.getbal())


# Object creation
acc1 = SavingAccount(5)
acc1.credit(500)
acc1.interestrate()
