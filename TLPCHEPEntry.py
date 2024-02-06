# TLPCHEPEntry
# This is specialised software for LRT/VCT's TLP system.
# This is to be used to automate some of the CHEP entry process.
#
# Author: Rory Ribarits
# Contact: rory.ribarits@hotmail.com

import re


def readEnv():
    # Check if .env file exists
    try:
        # Read the variables from the env file
        with open(".env", "r") as f:
            for line in f.readlines():
                try:
                    key, value = line.split('=')

                    if "EMAIL" == key:
                        email = value

                    if "PASSWORD" == key:
                        password = value
                except ValueError:
                    # Syntax error
                    pass
    except FileNotFoundError:
        print("Please enter login details for e-mail address that receives the CHEP Transfer OUT.")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        check = True

        # Loops until the email passes the RegEx
        while check:
            email = input("Username: ")
            if re.fullmatch(regex, email):
                check = False
            else:
                print("Check the spelling of the e-mail address and try again.")

        password = input("Password: ")

        # Writes the e-mail address and password into the env file
        with open(".env", "w") as f:
            f.write("EMAIL=" + email + " \n")
            f.write("PASSWORD=" + password + " \n")

        readEnv()

    # Removes the newline after the email and password
    email = email.rstrip()
    password = password.rstrip()

    return email, password


def tlpCHEPEntry():
    # Opening text
    print("TLP CHEP Entry")
    print("DESCRIPTION")

    email, password = readEnv()
    print("Please enter the start and end date of the CHEP transfers you wish to enter.")
    print("Format: DD/MM/YYYY")
    startDate = input("Start date: ")
    endDate = input("End date: ")

    # Open e-mail and start obtaining CHEP transfer OUT


if __name__ == '__main__':
    tlpCHEPEntry()
