import string
import random

print('--------------------------------------------------------')
print("    Password Generator with Account Password Manager    ")
print('--------------------------------------------------------')
print('Please be reminded to change your passwords periodically')

key_password = {}  # Dictionary for the accounts and passwords

command = {'display': 'To display your accounts and passwords in your library',  # dictionary for displaying of commands
           'add': 'To add usernames/emails to your library.',
           'change password': 'To change the password of your usernames/emails in your library.',
           'delete': 'To delete usernames/emails from the library.',
           'exit program': 'To exit the program.'}

choices = {'letters': 'For letters only',  # Dictionary for displaying what to include in the passwords
           'numbers': 'For letters with numbers',
           'punctuations': 'For letters with numbers and punctuations'}

while True:
    print()
    for go in command:
        print(f'{go:15}  :  {command[go]}')
    key = str(input('\nPlease input what to do: '))   # Printing of commands

    if key == 'display':
        if key_password:
            print('Username                 Password')    # Display command to display the dictionary
            for main in key_password:
                print(f'{main:20}  :  {key_password[main]}')
        else:
            print("You don't have any passwords at the moment. Input 'add' to add one.")   # If dictionary is empty

    elif key == 'add':  # Adding of accounts
        print()
        for ch in choices:  # displaying of choices
            print(f'{ch:15}  :  {choices[ch]}')
        choice = str(input('\nPlease choose what to include: '))  # user input for the choices
        if choice == 'letters':   # if choice is letters, execute
            try:
                def random_password(string_length=int(input('Please input the length of your password (the longer the '
                                                            'password is, the more security you get): '))):
                    password_characters = string.ascii_letters
                    return ''.join(random.choice(password_characters) for i in range(string_length))
                new_username = str(input('\nEnter your username/email: '))
                key_password[new_username] = random_password()
                if key_password[new_username] == '':    # if length is 0
                    print('You did not put a password. Please try again')
                    del (key_password[new_username])
                    pass
                elif len(key_password[new_username]) > 20:     # if length is greater than 20
                    print('Input a length that is less than 20. Please try again.')
                    del(key_password[new_username])     # delete the input if length is greater than 20
                    pass
                else:
                    print('New info has been added!')  # printing of password
                    print('The password is: ', key_password[new_username])
            except ValueError:
                print('Please input a number and try again.')
        elif choice == 'numbers':
            try:
                def random_password(string_length=int(input('Please input the length of your password (the longer the '
                                                            'password is, the more security you get): '))):
                    password_characters = string.ascii_letters + string.digits
                    return ''.join(random.choice(password_characters) for i in range(string_length))
                new_username = str(input('\nEnter your username/email: '))
                key_password[new_username] = random_password()
                if key_password[new_username] == '':
                    print('You did not put a password. Please try again')
                    del (key_password[new_username])
                    pass
                elif len(key_password[new_username]) > 20:
                    print('Input a length that is less than 20. Please try again.')
                    del (key_password[new_username])
                    pass
                else:
                    print('New info has been added!')
                    print('The password is: ', key_password[new_username])
            except ValueError:
                print('Please input a number and try again.')
        elif choice == 'punctuations':
            try:
                def random_password(string_length=int(input('Please input the length of your password (the longer the '
                                                            'password is, the more security you get): '))):
                    password_characters = string.ascii_letters + string.digits + string.punctuation
                    return ''.join(random.choice(password_characters) for i in range(string_length))
                new_username = str(input('\nEnter your username/email: '))
                key_password[new_username] = random_password()
                if key_password[new_username] == '':
                    print('You did not put a password. Please try again')
                    del (key_password[new_username])
                    pass
                elif len(key_password[new_username]) > 20:
                    print('Input a length that is less than 20. Please try again.')
                    del (key_password[new_username])
                    pass
                else:
                    print('New info has been added!')
                    print('The password is: ', key_password[new_username])
            except ValueError:
                print('Please input a number and try again.')
        else:
            print('Please enter a correct command and try again.')

    elif key == 'change password':
        for ch in choices:
            print(f'{ch:15}  :  {choices[ch]}')
        choice = str(input('\nPlease choose what to include: '))
        if choice == 'letters':
            try:
                def random_password(string_length=int(input('Please input the length of your password (the longer the '
                                                            'password is, the more security you get): '))):
                    password_characters = string.ascii_letters
                    return ''.join(random.choice(password_characters) for i in range(string_length))
                print('\nUsername                 Password')
                for main in key_password:
                    print(f'{main:20}  :  {key_password[main]}')
                key = str(input('Enter the username/email of choice : '))
                if key in key_password:
                    key_password[key] = random_password()
                    if key_password[key] == '':
                        print('You did not put a password. Your password will now be deleted.')
                        print('Please add a new account')
                        del(key_password[key])
                        pass
                    elif len(key_password[key]) > 20:
                        print('You did not put a password. Your password will now be deleted.')
                        print('Please add a new account')
                        pass
                        del (key_password[key])
                    else:
                        key_password[key] = random_password()
                        print('The password has been changed!')
                        print('The new password is: ', key_password[key])
                else:
                    print('The username is not in the library. Please try again.')
            except ValueError:
                print('Please input a number and try again.')
        elif choice == 'numbers':
            try:
                def random_password(string_length=int(input('Please input the length of your password (the longer the '
                                                            'password is, the more security you get): '))):
                    password_characters = string.ascii_letters + string.digits
                    return ''.join(random.choice(password_characters) for i in range(string_length))
                print('\nUsername                 Password')
                for main in key_password:
                    print(f'{main:20}  :  {key_password[main]}')
                key = str(input('Enter the username/email of choice : '))
                if key in key_password:
                    key_password[key] = random_password()
                    if key_password[key] == '':
                        print('You did not put a password. Your password will now be deleted.')
                        print('Please add a new account')
                        del (key_password[key])
                        pass
                    elif len(key_password[key]) > 20:
                        print('You did not put a password. Your password will now be deleted.')
                        print('Please add a new account')
                        del (key_password[key])
                        pass
                    else:
                        print('The password has been changed!')
                        print('The new password is: ', key_password[key])
                else:
                    print('The username is not in the library. Please try again.')
            except ValueError:
                print('Please input a number and try again.')
        elif choice == 'punctuations':
            try:
                def random_password(string_length=int(input('Please input the length of your password (the longer the '
                                                            'password is, the more security you get): '))):
                    password_characters = string.ascii_letters + string.digits + string.punctuation
                    return ''.join(random.choice(password_characters) for i in range(string_length))
                print('\nUsername                 Password')
                for main in key_password:
                    print(f'{main:20}  :  {key_password[main]}')
                key = str(input('Enter the username/email of choice : '))
                if key in key_password:
                    key_password[key] = random_password()
                    if key_password[key] == '':
                        print('You did not put a password. Your password will now be deleted.')
                        print('Please add a new account')
                        del (key_password[key])
                        pass
                    elif len(key_password[key]) > 20:
                        print('You did not put a password. Your password will now be deleted.')
                        print('Please add a new account')
                        del (key_password[key])
                        pass
                    else:
                        print('The password has been changed!')
                        print('The new password is: ', key_password[key])
                else:
                    print('The username is not in the library. Please try again.')
            except ValueError:
                print('Please input a number and try again.')
        else:
            print('Please enter a correct command and try again.')

    elif key == 'delete':
        try:
            print('\nUsername                 Password')
            for main in key_password:
                print(f'{main:20}  :  {key_password[main]}')
            del_key = str(input('\nEnter the username/email that will be deleted: '))
            del(key_password[del_key])
            print('Username/email deleted!')
        except KeyError:
            print('The username does not exist. Please try again.')

    elif key == 'exit program':
        print('The program will now exit. Thank you!')
        exit()

    else:
        print('Please input a correct command.')
