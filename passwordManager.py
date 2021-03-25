#passwordManager
#creates and displays passwords

#variables and lists
accountsList = []

#main
print("Hi, this program will allow you to craate, store, and view usernames and passwords you have registered. \nYou must be 13 or older to use this program.")
name = input("What is your name? ")
age = int(input("How old are you? "))
if age < 13:
    print('Sorry {}. You do not meet the age requirement to use this program.'.format(name))
    exit()
else:
    print('Hello {}'.format(name))
    while True:
        print("Choose a mode by entering a number")
        print("1. Store new account details")
        print("2. View Accounts")
        print("3. Remove an Account")
        print("4. exit")
        options = input()
        if options == '1':
            addUsername = input('Please enter the username of this account: ')
            addPassword = input('Please enter the password of this account: ')
            accountsList.append([addUsername, addPassword])
        elif options == '2':
            print('Choose what account you would like to remove.')
            print(accountsList)
        elif options == '3':
            print("This option is not implemented yet.")
        elif options == '4':
            print('bai bai')
            exit()
        else:
            print('Please pick from the options displayed.')