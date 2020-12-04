class Account:
    # class variable
    noOfAccounts = 0

    def __init__(self, balance=1000):
        self.balance = balance  # instance variable

    def getBalance(self):
        return self.balance

    def deposit(self, amt):
        if amt > 0:
            self.balance = self.balance + amt
            return True
        else:
            return False

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance = self.balance - amt
            return True
        else:
            return False


if __name__ == '__main__':
    new_account = Account()
    while True:
        inp_mainscreen = input(
            "\nThis is a banking system coded in Python. Please choose one of the following options: \n1. Add Account \n2. Deposit \n3. Withdraw \n4. Balance Inquiry \n5. Quit\nYour input: ")
        if inp_mainscreen == '1':
            create_fname, create_lname = input(
                "Input your first and last name with a space in between (e.g. John Doe): ").split()
            print(
                f"Created a new account for {create_fname} {create_lname} with balance of {new_account.getBalance()}.")
        elif inp_mainscreen == '2':
            inp_deposit = eval(input(
                "Please input the amount of money you would like to deposit to your account: "))
            if new_account.deposit(inp_deposit) == True:
                print(
                    f"Transaction successful. Your balance is now {new_account.getBalance()}.")
            else:
                print("Transaction error.")
        elif inp_mainscreen == '3':
            inp_withdraw = eval(input(
                "Please input the amount of money you would like to withdraw to your account: "))
            if new_account.withdraw(inp_withdraw) == True:
                print(
                    f"Transaction successful. Your balance is now {new_account.getBalance()}.")
            else:
                print("Transaction error.")
        elif inp_mainscreen == '4':
            print(
                f"Your account currently has a balance of {new_account.getBalance()}.")
        elif inp_mainscreen == '5':
            print("Program has been terminated.")
            break
        else:
            print("Invalid input.")
