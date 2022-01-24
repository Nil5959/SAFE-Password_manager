import time
import getpass
import os
import ctypes
import sys



#Enter your accounts here

#Delete what in the ""

master_key1 = "1"

#Delete what in the ""
steam_user = "Enter your accounts in the source code"
steam_pass = "Enter your accounts in the source code"
steam_rec = "Enter your accounts in the source code"
paypal_user = "Enter your accounts in the source code"
paypal_pass = "Enter your accounts in the source code"
instagram_user = "Enter your accounts in the source cod"
instagram_password = "Enter your accounts in the source cod"
spotify_user = "Enter your accounts in the source code"
spotify_mail = "Enter your accounts in the source code"
spotify_pass = "Enter your accounts in the source code"
pc_user = "Enter your accounts in the source code"
pc_pass = "Enter your accounts in the source code"
twitter_user = "Enter your accounts in the source code"
twitter_pass = "Enter your accounts in the source code"
ebay_mail = "Enter your accounts in the source code"
ebay_pass = "Enter your accounts in the source code"
gmail_mail = "Enter your accounts in the source code"
gmail_pass = "Enter your accounts in the source code"
















def sys():
    # Disable history (...but also auto-completion :/ )
    if hasattr(sys, '__interactivehook__'):
        del sys.__interactivehook__
    ctypes.windll.kernel32.SetConsoleTitleW("SAFE - Password manager")
def welcome():
    print('\33[93m' + "Unlocking safe ðŸ”“..." + '\x1b[0m')
    time.sleep(2)
    print('\33[92m' + "Safe unlocked ðŸ”“" + '\x1b[0m') #if user and password right say welcome
    time.sleep(1)
    account()
def login_failed():
    print('\33[93m' + "Unlocking safe ðŸ”“..." + '\x1b[0m')
    time.sleep(2)
    print('\33[31m' + 'Failed to unlock safe!' + '\x1b[0m')
    print("Try again in 5 seconds!")
    time.sleep(1)
    print("4 More seconds!")
    time.sleep(1)
    print("3 More seconds!")
    time.sleep(1)
    print("2 More seconds!")
    time.sleep(1)
    print("1 More seconds!")
    time.sleep(1)
    return start()
def account():
    clear()
    safe()
    print("                                     ------\33[90mSTEAM\x1b[0m------\n                                     ------\33[91mGMAIL\x1b[0m------\n                                     ------\33[34mPAYPAL\x1b[0m-----\n                                     ----\33[95mINSTAGRAM\x1b[0m-----\n                                     -----\33[92mSPOTIFY\x1b[0m-----\n                                     -----\33[94mTWITTER\x1b[0m-----\n                                     -------\33[14mEBAY\x1b[0m------\n                                     --------\33[4mPC\x1b[0m-------")  # Gives the list of accounts
    account2 = input('\33[96m' + "Select an account!: " + '\x1b[0m').lower()
    if account2 == "s":
        print("If you meant spotify or steam")
        print("Write \"spotify\" or \"steam\" ")
        input('\33[96m' + "Press enter to return" + '\x1b[0m')
        return account()
    elif account2 == "steam":
        print("Username: "+steam_user+"\nPassword: "+steam_pass+"\nRecovery Code: "+steam_rec)
        input('\33[96m' + "Press enter to return" + '\x1b[0m')
        return account()
    elif account2 == "paypal" or account2 == "p":
        print("Username: "+paypal_user+" \nPassword: "+paypal_pass)
        input('\33[96m' + "Press enter to return" + '\x1b[0m')
        return account()
    elif account2 == "instagram" or account2 == "insta" or account2 == "i":
        print("Username: "+instagram_user+" \nPassword: "+instagram_password)
        input('\33[96m' + "Press enter to return" + '\x1b[0m')
        return account()
    elif account2 == "spotify":
        print("Username: \nEmail: \nPassword: \n##################\nUsername: \nEmail: \nPassword: ")
        input('\33[96m' + "Press enter to return" + '\x1b[0m')
        return account()
    elif account2 == "ebay" or account2 == "e":
        print("Email: "+ebay_mail+"\nPassword: "+ebay_pass)
        input('\33[96m' + "Press enter to return" + '\x1b[0m')
        return account()
    elif account2 == "gmail" or account2 == "g" :
        print("Email: "+gmail_mail+"\nPassword: "+gmail_pass)
        input('\33[96m' + "Press enter to return" + '\x1b[0m')
        return account()
    elif account2 == "twitter" or account2 == "t":
        print("Username: "+twitter_user+" \nPassword: "+twitter_pass)
        input('\33[96m' + "Press enter to return" + '\x1b[0m')
        return account()
    elif account2 == "pc" or account2 == "pc2":
        print("Username: "+pc_user+" \nPassword: "+pc_pass)
        input('\33[96m' + "Press enter to return" + '\x1b[0m')
        return account()
    else:
        print("The account " + account2 + " could not be found")
        input('\33[96m' + "Press enter to return" + '\x1b[0m')
        return account()
def start():

    clear()
    safe()
    master_key = getpass.getpass('\33[91m' + "Don't worry the password is HIDDEN AND ENCRYPTED!\nThe password is 1 if you didnt change it\n" + '\x1b[0m''\33[96m' + "Please enter your master key ðŸ”‘: " + '\x1b[0m')
    if master_key == master_key1:
        welcome()
    else:
        login_failed()
def clear():
    os.system('cls')
def safe():
    print("  ")
    print("  ")
    print("  ")
    print('\33[93m' + "                          " + "Thanks, for using SAFE - Password manager" + '\x1b[0m')
    print("                                   " + '\33[31m' + "THIS WAS MADE BY Nil" + '\x1b[0m')
    print('\33[93m' + "                              " + "All credit goes to me and only me" + '\x1b[0m')
    print("  ")
    print('\33[34m' + "                       000000000    00000000    000000000   000000000          " + '\x1b[0m')
    print('\33[34m' + "                      00000000000  0000000000   000000000   000000000             " + '\x1b[0m')
    print('\33[34m' + "                      000          000    000   000         000      " + '\x1b[0m')
    print('\33[34m' + "                      0000000000   000    000   00000000    000000000           " + '\x1b[0m')
    print('\33[34m' + "                       0000000000  0000000000   00000000    000000000            " + '\x1b[0m')
    print('\33[34m' + "                              000  0000000000   000         000          " + '\x1b[0m')
    print('\33[34m' + "                      00000000000  000    000   000         000000000          " + '\x1b[0m')
    print('\33[34m' + "                       000000000   000    000   000         000000000           " + '\x1b[0m')
    print("  ")
    print("  ")
sys()
start()
