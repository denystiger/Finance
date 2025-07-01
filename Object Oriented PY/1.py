account0Name = ''
account0Balance = ''
account0Password = ''
account1Name = ''
account1Balance = 0
account1Password = ''
nAccounts = 0

def newAccount(accountNumber, name, balance, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        account0Name = name
        account0Password = password
        account0Balance = balance
    if accountNumber == 1:
        account1Name = name
        account1Password = password
        account1Balance = balance
def show():
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if account0Name != '':
        print('Account 0')
        print('      Name', account0Name)
        print('      Balance', account0Balance)
        print('      Password', account0Password)
        print()
        if account1Name != '': print('Account 1')
        print(' Name', account1Name)
        print(' Balance:', account1Balance)
        print(' Password:', account1Password)
        print()
def getBalance(accountNumber, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if password !=account0Password:
            print('Incorrect password')
            return None
        return account0Balance
    if accountNumber ==0:
        if password != account1Password:
            print('Incorrect password')
            return None
        return account1Balance
    





