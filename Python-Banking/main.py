from Bank import Bank
from time import sleep

myBank = Bank("Not BCA", [], {})


def main():
    print("This is a menu-driven terminal banking system")
    while True:
        user_choice = input(
            f"\nWelcome to {myBank.bank_name}. Please choose one of the following options:\n1. Create an Account\n2. Login to Account\n3. Account Inquiry \n4. Deposit\n5. Withdraw\n6. Balance Inquiry\n7. Quit the program\nYour Choice: ")
        if user_choice == '1':
            inp_fname, inp_lname = input(
                "Please input your first and last name and separate them with a space (e.g. John Doe): ").split(" ")
            inp_pword = input("Please input a password for your account: ")
            if myBank.add_customer(inp_fname, inp_lname, inp_pword) == True:
                print(
                    f"Customer with name {inp_fname} {inp_lname} successfully registered. Please login with your account")
            else:
                print("User already exists")
        elif user_choice == '2':
            login_fname, login_lname = input(
                "Please input the first and last name you used to register into this program (e.g. John Doe): ").split(" ")
            login_pword = input("Please input the password of this user: ")
            if myBank.get_customer(login_fname, login_lname) != False:
                if myBank.user_log[f"{login_fname} {login_lname}"] == login_pword:
                    myBank.current_customer = myBank.get_customer(
                        login_fname, login_lname)
                    print(
                        f"Successful Login. Welcome {login_fname} {login_lname}.")
                else:
                    print("Incorrect password.")
            else:
                print("User doesn't exist.")
                print("User doesn't exist.")
        elif user_choice == '3':
            if myBank.current_customer == None:
                print("You are currently not logged into an account.")
            else:
                print(
                    f"You are currrently logged in as {myBank.current_customer.get_firstname()} {myBank.current_customer.get_lastname()}.")
        elif user_choice == '4':
            if myBank.current_customer == None:
                print("You are currently not logged into an account.")
            else:
                amt_deposit = eval(input(
                    "Please input the amount of money you would like to deposit to your account: "))
                if myBank.current_customer.get_account().deposit(amt_deposit) == True:
                    print(
                        f"Transaction successful. You now have {myBank.current_customer.get_account().getBalance()} in your balance.")
                else:
                    print("Transaction error.")
        elif user_choice == '5':
            if myBank.current_customer == None:
                print("You are currently not logged into an account.")
            else:
                amt_withdraw = eval(input(
                    "Please input the amount of money you would like to withdraw from your account: "))
                if myBank.current_customer.get_account().withdraw(amt_withdraw) == True:
                    print(
                        f"Transaction successful. You now have {myBank.current_customer.get_account().getBalance()} in your balance.")
                else:
                    print("Transaction error.")
        elif user_choice == '6':
            if myBank.current_customer == None:
                print("You are currently not logged into an account.")
            else:
                print(
                    f"You currently have {myBank.current_customer.get_account().getBalance()} in your account")
        elif user_choice == '7':
            print("Program has been terminated.")
            break
        else:
            print("Invalid input. Please try again.")

        """
        # Admin commands. Not in user menu. I just used this to find errors within my program.
        elif user_choice == '!customers_list':
            print(myBank.customers)
        else:
            print("Invalid input. Please try again.")
        
        elif user_choice == '!show_userlog
            print(myBank.user_log)
        """

        # Added a loading mechanism to give time for the users to read the details of their transaction.
        sleep(0.8)
        print("Loading...")
        sleep(2)


if __name__ == '__main__':
    main()
