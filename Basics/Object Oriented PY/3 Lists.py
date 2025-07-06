accountsList = []
def newAccount (aName, aBalance, aPassword) :
    global accountsList
    newAccountDict = {'name': aName, 'balance' : aBalance,
    'password' :aPassword}
    accountsList. append (newAccountDict) 2
def show(accountNumbeer):
    global accountsList
    print('Account', accountNumber)
    thisAccountDict = accountsList[accountNumbeer]
    print('     Name, thisAcc')

def show(accountNumber):

    global accountsList

    print('Account', accountNumber)
    thisAccountDict = accountsList[accountNumber]
    print('
    print(' Name', thisAccountDict [ 'name']) Balance: '
    , thisAccountDict['balance'])
    print('
    Password: ', thisAccountDict['
    password
    ' ])
    print()


