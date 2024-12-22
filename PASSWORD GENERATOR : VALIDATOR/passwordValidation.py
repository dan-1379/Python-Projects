import random
import sys

print(
"""
_______________________________________________________________________________________

######                                                   
#     #   ##    ####   ####  #    #  ####  #####  #####  
#     #  #  #  #      #      #    # #    # #    # #    # 
######  #    #  ####   ####  #    # #    # #    # #    # 
#       ######      #      # # ## # #    # #####  #    # 
#       #    # #    # #    # ##  ## #    # #   #  #    # 
#       #    #  ####   ####  #    #  ####  #    # #####  
                                                    
_______________________________________________________________________________________
PLEASE SELECT FROM THE OPTIONS BELOW
    1. PASSWORD GENERATOR
    2. PASSWORD VALIDATOR
    3. Quit
_______________________________________________________________________________________
"""
)

while True:
    ask_option = int(input("\nEnter your option: "))

    #option 1 - password generator
    if ask_option == 1:
        print(
            """
    -------------------------------------------------------------------------------------
    PASSWORD GENERATOR
    -------------------------------------------------------------------------------------
            """
        )
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@£$%^&**()_-?/~"

        character_length = int(input("Enter the character length of your desired passsord: "))
        
        if len(str(character_length)) <= 12:
            new_password = ""

            for character in range(character_length):
                new_password += random.choice(characters)

            print(f"Your new password of {character_length} characters is: \n\n\t{new_password} \n")
            print(
                """
_______________________________________________________________________________________
                """
            )

        else:
            print("Password needs to be at least 12 characters\n")

    #option 2 - password validator
    elif ask_option == 2:
        print(
            """
    -------------------------------------------------------------------------------------
    PASSWORD VALIDATOR
    -------------------------------------------------------------------------------------
    REQUIREMENTS:
        AT LEAST 12 CHARACTERS
        AT LEAST 1 UPPERCASE
        AT LEAST 1 NUMBER
        AT LEAST 1 SYMBOL
            """
        )

        ask_password = input("Enter your password: ").strip()

        uppercase_count = 0
        lowercase_count = 0
        number_count = 0
        symbol_count = 0

        MIN_PASSWORD_LENGTH = 12
        MIN_UPPERCASE = 1
        MIN_LOWERCASE = 1
        MIN_NUMBERS = 1
        MIN_SYMBOLS = 1

        password_length = len(ask_password)
        symbols = "!@£$%^&**()_-?/~"


        for character in ask_password:
            if character.isnumeric():
                number_count += 1
            
            elif character.isupper():
                uppercase_count += 1

            elif character.islower():
                lowercase_count += 1

            elif character in symbols:
                symbol_count += 1

        if uppercase_count > 0 and number_count > 0 and symbol_count > 0:
            print(
                f"""
                YOUR PASSWORD: {ask_password} has:
                    {password_length} characters,
                    {uppercase_count} uppercase characters,
                    {lowercase_count} lowercase characters,
                    {number_count} numbers,
                    {symbol_count} symbols

                GOOD PASSWORD
_______________________________________________________________________________________               
                """
                )
        
        else:
            print(
                f"""
                YOUR PASSWORD: {ask_password} has:
                    {password_length} characters,
                    {uppercase_count} uppercase characters,
                    {number_count} numbers,
                    {symbol_count} symbols

                NOT GOOD PASSWORD
                
                FOR A MORE SECURE PASSWORD PLEASE INCLUDE:
                """
            )
            if MIN_PASSWORD_LENGTH > password_length:
                print(f"\t\t{MIN_PASSWORD_LENGTH - password_length} more characters required")
            
            if MIN_UPPERCASE > uppercase_count:
                print(f"\t\t{MIN_UPPERCASE - uppercase_count} more uppercase required")

            if MIN_LOWERCASE > lowercase_count:
                print(f"\t\t{MIN_LOWERCASE - lowercase_count} more lowercase required")

            if MIN_NUMBERS > number_count:
                print(f"\t\t{MIN_NUMBERS - number_count} more numbers required")

            if MIN_SYMBOLS > symbol_count:
                print(f"\t\t{MIN_SYMBOLS - symbol_count} more symbols required")

    elif ask_option == 3:
        sys.exit()
        
    else:
        print(f"{ask_option} is not an option. Please try again.")