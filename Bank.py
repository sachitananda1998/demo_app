class account():
    def __init__(self,name,account_number,balance):
        self.name=name
        self.account_number=account_number
        self.balance=balance

    def deposit(self,amount):
        try:
            self.balance=self.balance + amount
            return "Your updated balance is "+str(self.balance)
        except:
            print("Invalid amount to be deposited")
    
    def withdrawl(self,amount):
        if self.balance >= amount:
            self.balance=self.balance - amount
            return "Your updated balance is "+str(self.balance)
        else:
            return False

    def transfer(self,account,amount):
        if self.withdraw(amount):
            account.deposit(amount)
        else:
            print("Unable to withdraw the amount")