from Customer import Customer


class Bank:
    customer_number = 0
    current_customer = None

    def __init__(self, bank_name, customers, user_log):
        self.bank_name = bank_name
        self.customers = customers
        # I added a new dictionary called user_log that will track the password of each user.
        self.user_log = user_log

# add_customer now can check whether or not a particular user is already in the customers list.
    def add_customer(self, fname, lname, pin):
        new_acc = Customer(fname, lname)
        if new_acc not in self.customers:
            self.customers.append(new_acc)
            self.user_log[f"{fname} {lname}"] = pin
            self.customer_number += 1
            return True
        else:
            return False

    def getnumof_cust(self):
        return self.customer_number

    def get_customer(self, fname, lname):
        my_customer = Customer(fname, lname)
        if my_customer in self.customers:
            return my_customer
        else:
            return False
