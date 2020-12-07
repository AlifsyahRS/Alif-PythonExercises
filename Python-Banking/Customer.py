from Account import Account


class Customer:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.account = Account()

    # Made an eq function to compare customers. This will be useful in not allowing duplicate accounts.
    def __eq__(self, other):
        if not isinstance(other, Customer):
            return NotImplemented

        return self.fname == other.fname and self.lname == other.lname

    def get_firstname(self):
        return self.fname

    def get_lastname(self):
        return self.lname

    def get_account(self):
        return self.account

    def set_account(self):
        self.account = acc
