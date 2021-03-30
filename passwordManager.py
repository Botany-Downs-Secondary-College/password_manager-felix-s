#passwordManager
#creates and displays passwords

#variables and lists
masterAccountsList = [["test", "12345"], ["test2", "123456"]]
accountDetailsDict = {"test":{"testa":["aa","aaa"], "testb":["bb","bbb"]}, "test2": [['test1','11','111'], ['test2','22','222'],['master','test2','123456']]}

#test


#main
print("Hi, this program will allow you to craate, store, and view usernames and passwords you have registered. \nYou must be 13 or older to use this program.")
while True:
    print("Choose a mode by entering a number: ")
    print("1. Sign up")
    print("2. Login")
    print("3. exit")
    optionsOne = input()
    if optionsOne == "1":
        age = int(input("How old are you? "))
        if age < 13:
            print('Sorry. You do not meet the age requirement to use this program.')
            exit()
        else:
            addMasterUsername = input("What is the username of this account? ")
            addMasterPassword = input("What is the password of this account? ")
            masterAccountsList.append([addMasterUsername, addMasterPassword])
            accountDetailsDict[addMasterUsername] = []
            print("Account Created!")
    elif optionsOne == "2":
        MasterUsername = input("Username: ")
        MasterPassword = input("Password: ")
        for info in masterAccountsList:
            if MasterUsername == info[0] and MasterPassword == info[1]:
                print('Welcome, {}'.format(MasterUsername))
                while True:
                    print("Choose a mode by entering a number: ")
                    print("1. Store new account details")
                    print("2. View Accounts")
                    print("3. Remove an Account")
                    print("4. exit")
                    optionsTwo = input()
                    if optionsTwo == '1':
                        addUsername = input('Please enter the username of this account: ')
                        addPassword = input('Please enter the password of this account: ')
                        addPurpose = input('What are these account details for?')
                        accountDetailsDict[MasterUsername].append([addPurpose, addUsername, addPassword])
                    elif optionsTwo == '2':
                        print('Here are the account details you have stored: ')
                        for infoOne, infoTwo in accountDetailsDict[MasterUsername].items():
                            print("{}\nUsername: {}\nPassword: {}".format(infoOne, infoTwo[0], infoTwo[1]))
                    elif optionsTwo == '3':
                        print("Name the account you would like to remove. Type 'cancel' to exit")
                        for i, val in enumerate(accountDetailsDict[MasterUsername].keys(), start=1):
                            print(i,")", val)
                        removeInput = input()
                        for x in accountDetailsDict[MasterUsername].keys():
                            if x == removeInput:
                                del accountDetailsDict[MasterUsername][x]
                                print('Details deleted successfully!')
                                break
                            elif removeInput == "cancel":
                                continue
                            else:
                                print('Those account details do not exist')
                                break
                    elif optionsTwo == '4':
                        print('bai bai')
                        exit()
                    else:
                        print('Please pick from the options displayed.')
            else:
                continue
        else:
            print("Incorrect login details")

    elif optionsOne == "3":
        print("bai bai")
        exit()
    else:
        print("Please pick from the options displayed")


