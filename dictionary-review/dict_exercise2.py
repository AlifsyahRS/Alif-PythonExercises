
user_info = {'Alif': 'kY342jd', 'user1': 'helloworld'}
inp_username, inp_password = input("Please input a username\n"), input(
    "\nPlease input the password\n")


def accept_login(users, username, password):
    if username in users.keys() and password == users[username]:
        return True
    else:
        return False


if __name__ == '__main__':
    if accept_login(user_info, inp_username, inp_password) == True:
        print("\nUser authorized. Welcome", inp_username)
    else:
        print("\nInvalid username or password.")
