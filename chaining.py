class User:		
    def __init__(self, name, balance):
        self.name = name
        self.account_balance = balance
    
    def make_deposit(self, amount):
        self.account_balance += amount

        return self

    def make_withdraw(self, amount):
        if(self.account_balance - amount) < 0:
            print("insufficient funds in the account")
        else:    
            self.account_balance -= amount

        return self

    def display_user_balance(self):
        print(f"{self.name}'s balance: {self.account_balance}")

        return self
    

hanson = User("Hanson",0)
tony = User("Tony",0)
rogers = User("Captin",0)


hanson.make_deposit(600).make_deposit(400).make_deposit(1020).make_withdraw(650).display_user_balance()

tony.make_deposit(1000).make_deposit(1000).make_withdraw(500).make_withdraw(600).display_user_balance()

rogers.make_deposit(3000).make_withdraw(2000).make_withdraw(500).make_withdraw(600).display_user_balance()
