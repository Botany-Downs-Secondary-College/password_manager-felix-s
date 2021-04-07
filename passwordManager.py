#passwordManager
#creates and displays passwords

#variables and lists
masterAccountsList = [["test", "12345"], ["test2", "123456"]]
accountDetailsDict = {"test":{"testa":["aa","aaa"], "testb":["bb","bbb"]}, "test2":{'t1':['11','111'], 't2':['22','222']}}

def options(mode):
    print("Choose a mode by entering a number: ")
    for i in mode:
        print(i)
    else:
        options = input()
    return options

def signUp():
    while True:
        try:
            age = float(input("How old are you? "))
            if age < 13:
                print('Sorry. You do not meet the age requirement to use this program.')
                exit()
            else:
                addMasterUsername = input("What is the username of this account? ")
                addMasterPassword = input("What is the password of this account? ")
                masterAccountsList.append([addMasterUsername, addMasterPassword])
                accountDetailsDict[addMasterUsername] = {}
                print("Account Created!")
                break
        except ValueError:
            print("Please enter an integer.")

def passwordManager(username):
    print('Welcome, {}'.format(username))
    while True:
        optionsTwo = options(["1. Store new account details", "2. View Accounts", "3. Remove an Account", "4. exit"])
        if optionsTwo == '1':
            def addAccountDetails():
                addUsername = input('Please enter the username of this account: ')
                addPassword = input('Please enter the password of this account: ')
                addPurpose = input('What are these account details for?')
                accountDetailsDict[username][addPurpose] = [addUsername, addPassword]
            addAccountDetails()
        elif optionsTwo == '2':
            def viewAccountDetails():
                print('Here are the account details you have stored: ')
                for infoOne, infoTwo in accountDetailsDict[username].items():
                    print("{}\nUsername: {}\nPassword: {}".format(infoOne, infoTwo[0], infoTwo[1]))
            viewAccountDetails()
        elif optionsTwo == '3':
            def removeAccountDetails():
                print("Name the account you would like to remove. Type 'cancel' to exit")
                for i, val in enumerate(accountDetailsDict[username].keys(), start=1):
                    print(i, ")", val)
                removeInput = input()
                for x in accountDetailsDict[username].keys():
                    if x == removeInput:
                        del accountDetailsDict[username][x]
                        print('Details deleted successfully!')
                        break
                    elif removeInput == "cancel":
                        continue
                    else:
                        print('Those account details do not exist')
                        break
            removeAccountDetails()
        elif optionsTwo == '4':
            print('bai bai')
            exit()
        else:
            print('Please pick from the options displayed.')

#main
print("Hi, this program will allow you to create, store, and view usernames and passwords you have registered. \nYou must be 13 or older to use this program.")
while True:
    optionsOne = options(["1. Sign up", "2. Login", "3. exit"])
    if optionsOne == "1":
        signUp()
    elif optionsOne == "2":
        MasterUsername = input("Username: ")
        MasterPassword = input("Password: ")
        for info in masterAccountsList:
            if MasterUsername == info[0] and MasterPassword == info[1]:
                passwordManager(MasterUsername)
            else:
                continue
        else:
            print("Incorrect login details")
    elif optionsOne == "3":
        print("bai bai")
        exit()
    else:
        print("Please pick from the options displayed")