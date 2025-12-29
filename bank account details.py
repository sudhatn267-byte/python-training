class Account:
    def __init__(self, balance, accno):
        self.balance = balance
        self.accno = accno

    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} is debited, balance is {self.getbal()}")
        else:
            print("Insufficient funds")

    def credit(self, amount):
        self.balance += amount
        print(f"{amount} is credited, balance is {self.getbal()}")

    def getbal(self):
        return self.balance


acc1 = Account(1000, "accno123")
acc1.credit(500)
acc1.debit(200)
