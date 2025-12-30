class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, account_number, inital_balance, interest_rate):
        super().__init__(account_number, inital_balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
        self.balance += self.balance * self.interest_rate


bankAccount = Account(123456, 1200.24)
savingsAccount = SavingsAccount(56789, 1000.00, 0.0355)

bankAccount.deposit(500.00)
bankAccount.withdraw(100.00)
savingsAccount.apply_interest()
bankAccount.get_balance()
savingsAccount.get_balance()




