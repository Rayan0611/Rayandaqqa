class BankAccount:
    def __init__(self, name, balance, password):
        # Creating the account with name, balance, and password
        self.name = name
        self.balance = balance
        self.password = password

    def verify_password(self, pw):
        # A method to verify password
        if pw == self.password:
            return True
        else:
            print("Incorrect password.")
            return False

    def deposit(self, amount, pw):
        # Deposit the money if amount is positive and password is correct
        if not self.verify_password(pw):
            return
        if amount <= 0:
            print("Cannot deposit negative or zero amount.")
        else:
            self.balance += amount
            print(f"Deposited ${amount} successfully.")

    def withdraw(self, amount, pw):
        # Withdraw the money if amount is within balance and the password is correct
        if not self.verify_password(pw):
            return
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount} successfully.")

    def get_balance(self):
        # Return current balance
        return self.balance

    def show_info(self):
        # Display account info 
        print("Account Info:")
        print(f"Name: {self.name}")
        print(f"Balance: ${self.balance}")
        print(f"Password: {self.password}")


# Testing 

# John
john = BankAccount("John", 500, "my_password")
john.withdraw(200, "my_password")       # should work
print("Balance:", john.get_balance())   # show balance

john.deposit(-700, "my_password")       # should deny
john.deposit(700, "my_password")        # should work
print("Balance:", john.get_balance())   # show balance
john.show_info()                        # show account info

print("\n-----------------\n")

# Diane
diane = BankAccount("Diane", 2000, "get_money_money")
diane.deposit(400, "wrong_password")    # wrong password
diane.deposit(400, "get_money_money")   # correct deposit
print("Balance:", diane.get_balance())  # show balance

diane.withdraw(2500, "get_money_money") # too much - deny
diane.withdraw(1700, "get_money_money") # allowed
print("Balance:", diane.get_balance())  # show balance
diane.show_info()                       # show account info
