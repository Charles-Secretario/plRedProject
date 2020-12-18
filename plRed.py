# Secretario, Bejar, Chuapoco
# BES241
# Lab Project
# December 15,2020
# I certify that I have worked on this activity and completed it on my own
# and that I have neither copied the work of another nor have I concealed any
# violation of the Honor Code. I will receive a grade of 5.0 (FAIL) for the course
# and be subject to disciplinary action if I fail to honor this code."
import string
import random


def random_password_letters():
    exceeded_length = True
    while exceeded_length:
        string_length = int(input('Please input the length of your password (the longer the password '
                                  'is, the more security you get): '))
        if string_length < 1 or string_length > 20:
            print('Input the length to less than 20. Please try again.')
        else:
            password_characters = string.ascii_letters
            return ''.join(random.choice(password_characters) for i in range(string_length))


def random_password_numbers():
    exceeded_length = True
    while exceeded_length:
        string_length = int(input('Please input the length of your password (the longer the password '
                                  'is, the more security you get): '))
        if string_length < 1 or string_length > 20:
            print('Input the length to less than 20. Please try again.')
        else:
            password_characters = string.ascii_letters + string.digits
            return ''.join(random.choice(password_characters) for i in range(string_length))


def random_password_punctuations():
    exceeded_length = True
    while exceeded_length:
        string_length = int(input('Please input the length of your password (the longer the password '
                                  'is, the more security you get): '))
        if string_length < 1 or string_length > 20:
            print('Input the length to less than 20. Please try again.')
        else:
            password_characters = string.ascii_letters + string.digits + string.punctuation
            return ''.join(random.choice(password_characters) for i in range(string_length))


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

while True:  # While loop for continuous execution
    print()
    for go in command:      # printing of the commands
        print(f'{go:15}  :  {command[go]}')
    key = str(input('\nPlease input what to do: '))  # user input of what to do

    if key == 'display':  # first command, it will display everything inside key_password
        if key_password:
            print('Username               Application/website     Current Password       Previous Password')
            for main in key_password:
                if len(key_password[main]) > 2:
                    print(f'{main:20}  :  {key_password[main][0]:20} : {key_password[main][1]:20} : {key_password[main][2]:20}')
                else:
                    print(f'{main:20}  :  {key_password[main][0]:20} : {key_password[main][1]:20}')
        else:
            print("You don't have any passwords at the moment. Input 'add' to add one.")  # if user did not input or
            # if dictionary is empty

    elif key == 'add':  # second command
        print()
        for ch in choices:
            print(f'{ch:15}  :  {choices[ch]}')  # printing of choices
        choice = str(input('\nPlease choose what to include: '))  # user input for the inclusions
        if choice == 'letters':
            try:
                # Added a loop that asks the user for an input length repeatedly if input is less than 20 or less
                # than 1.
                new_username = str(input('\nEnter your username/email: '))
                key_password[new_username] = []  # list for a key in the dictionary to store multiple data
                key_password[new_username].append(str(input('Enter the name of the application/website: ')))
                key_password[new_username].append(random_password_letters())
                print('New info has been added!')
                print('Your details are: ', key_password[new_username])
            except ValueError:
                print('Please input a number and try again.')
        elif choice == 'numbers':
            try:
                # Added a loop that asks the user for an input length repeatedly if input is less than 20 or less
                # than 1.
                new_username = str(input('\nEnter your username/email: '))
                key_password[new_username] = []
                key_password[new_username].append(str(input('Enter the name of the application/website: ')))
                key_password[new_username].append(random_password_numbers())
                print('New info has been added!')
                print('Your details are: ', key_password[new_username])
            except ValueError:
                print('Please input a number and try again.')  # execute when string_length is not an integer
        elif choice == 'punctuations':
            try:
                # Added a loop that asks the user for an input length repeatedly if input is less than 20 or less
                # than 1.
                new_username = str(input('\nEnter your username/email: '))
                key_password[new_username] = []
                key_password[new_username].append(str(input('Enter the name of the application/website: ')))
                key_password[new_username].append(random_password_punctuations())
                print('New info has been added!')
                print('Your details are: ', key_password[new_username])
            except ValueError:
                print('Please input a number and try again.')
        else:
            print('Please enter a correct command and try again.')

    elif key == 'change password':  # third command
        print()
        for ch in choices:
            print(f'{ch:15}  :  {choices[ch]}')  # displaying of choices
        choice = str(input('\nPlease choose what to include: '))
        if choice == 'letters':
            try:
                # Added a loop that asks the user for an input length repeatedly if input is less than 20 or less
                # than 1.
                print('Username               Application/website     Password')
                for main in key_password:
                    print(f'{main:20}  :  {key_password[main][0]:20} : {key_password[main][1]:20}')
                key = str(input('\nEnter the username/email of choice : '))
                if key in key_password:
                    key_password[key].append(key_password[key][1])
                    key_password[key][1] = random_password_letters()
                    print('The password has been changed!')
                    print('The new password is: ', key_password[key][1])
                    print('The previous password is: ', key_password[key][2])
                else:
                    print('The username is not in the library. Please try again.')
            except ValueError:
                print('Please input a number and try again.')
        elif choice == 'numbers':
            try:
                # Added a loop that asks the user for an input length repeatedly if input is less than 20 or less
                # than 1.
                print('Username               Application/website     Password')
                for main in key_password:
                    print(f'{main:20}  :  {key_password[main][0]:20} : {key_password[main][1]:20}')
                key = str(input('\nEnter the username/email of choice : '))
                if key in key_password:
                    key_password[key].append(key_password[key][1])
                    key_password[key][1] = random_password_numbers()
                    print('The password has been changed!')
                    print('The new password is: ', key_password[key][1])
                    print('The previous password is: ', key_password[key][2])
                else:
                    print('The username is not in the library. Please try again.')  # execute if key is not in
                    # key_password
            except ValueError:
                print('Please input a number and try again.')
        elif choice == 'punctuations':
            try:
                # Added a loop that asks the user for an input length repeatedly if input is less than 20 or less
                # than 1.
                print('Username               Application/website     Password')
                for main in key_password:
                    print(f'{main:20}  :  {key_password[main][0]:20} : {key_password[main][1]:20}')
                key = str(input('\nEnter the username/email of choice : '))
                if key in key_password:
                    key_password[key].append(key_password[key][1])
                    key_password[key][1] = random_password_punctuations()
                    print('The password has been changed!')
                    print('The new password is: ', key_password[key][1])
                    print('The previous password is: ', key_password[key][2])
                else:
                    print('The username is not in the library. Please try again.')
            except ValueError:
                print('Please input a number and try again.')
        else:
            print('Please enter a correct command and try again.')

    elif key == 'delete':  # fourth command
        try:
            print('\nUsername                 Password')
            for main in key_password:
                print(f'{main:20}  :  {key_password[main][0]:20} : {key_password[main][1]:20}')
            del_key = str(input('\nEnter the username/email that will be deleted: '))
            del (key_password[del_key])  # delete execution
            print('Username/email deleted!')
        except KeyError:
            print('The username does not exist. Please try again.')  # execute if username is not in key_password dict

    elif key == 'exit program':  # fifth command
        print('The program will now exit. Thank you!')
        exit()  # exit the program

    else:
        print('Please input a correct command.')  # execute if user input is not a command
