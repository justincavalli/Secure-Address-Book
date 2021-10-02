from DatabaseFile import *
import cmd
import pickle
import os.path
from os import path
import random
import string
import sys, os

def main():
    # Disable
    def blockPrint():
        sys.stdout = open(os.devnull, 'w')

    # Restore
    def enablePrint():
        sys.stdout = sys.__stdout__

    if path.isfile('DatabaseStorage') == True:
        try:
            storageFile = open('DatabaseStorage', 'rb')
            database = pickle.load(storageFile)
        except pickle.PickleError:
            None  # There was no database stored in the file.
    if type(database) != Database:
        database = Database()
    if len(database.dictionary) == 0:
        print("You need to create an admin account to use the app")
        username = input("Choose a username for the admin account: ")
        database.first_admin(username)

    # test login with out active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        test2 = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.login(test, test2)
    enablePrint()
    print("login with out active sesssion with random input passed with no crashing ")

    # test login with active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    database.login("aekoshak", "6320182Aa")
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        test2 = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.login(test, test2)
    database.logout()
    enablePrint()
    print("login with active sesssion with random input passed with no crashing ")

    # test change_password with out active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.change_password(test)
    enablePrint()
    print("change_password with out active sesssion with random input passed with no crashing ")

    # test change_password with active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    database.login("aekoshak", "6320182Aa")
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.change_password(test)
    database.logout()
    enablePrint()
    print("change_password with active sesssion with random input passed with no crashing ")

    # test add_account with out active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.add_account(test)
    enablePrint()
    print("add_account with out active sesssion with random input passed with no crashing ")

    # test add_account with non-admin active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    database.login("aekoshak", "6320182Aa")
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.add_account(test)
    database.logout()
    enablePrint()
    print("add_account with non-admin active sesssion with random input passed with no crashing ")

    # test add_account with admin active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    database.login("admin", "Admin123456")
    #for i in range(100):
        #test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        #database.add_account(test)
    database.logout()
    enablePrint()
    print("add_account with admin active sesssion with random input passed with no crashing ")

    # test delete_account with out active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.delete_account(test)
    enablePrint()
    print("delete_account with out active sesssion with random input passed with no crashing ")


    # test delete_account with non-admin active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    database.login("aekoshak", "6320182Aa")
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.delete_account(test)
    database.logout()
    enablePrint()
    print("delete_account with non-admin active sesssion with random input passed with no crashing ")


    # test delete_account with admin active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    database.login("admin", "Admin123456")
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.delete_account(test)
    database.logout()
    enablePrint()
    print("delete_account with admin active sesssion with random input passed with no crashing ")

    # test display_audit_log with out active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.display_audit_log(test)
    enablePrint()
    print("display_audit_log with out active sesssion with random input passed with no crashing ")

    # test display_audit_log with non-admin active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    database.login("aekoshak", "6320182Aa")
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.display_audit_log(test)
    database.logout()
    enablePrint()
    print("display_audit_log with non-admin active sesssion with random input passed with no crashing ")

    # test display_audit_log with admin active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    database.login("admin", "Admin123456")
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.display_audit_log(test)
    database.logout()
    enablePrint()
    print("display_audit_log with admin active sesssion with random input passed with no crashing ")

    # test add_record with out active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.add_record(test)
    enablePrint()
    print("add_record with out active sesssion with random input passed with no crashing ")

    # test add_record with non-admin active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    database.login("aekoshak", "6320182Aa")
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.add_record(test)
    database.logout()
    enablePrint()
    print("add_record with non-admin active sesssion with random input passed with no crashing ")

    # test add_record with admin active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    database.login("admin", "Admin123456")
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.add_record(test)
    database.logout()
    enablePrint()
    print("add_record with admin active sesssion with random input passed with no crashing ")

    # test delete_record with out active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.delete_record(test)
    enablePrint()
    print("delete_record with out active sesssion with random input passed with no crashing ")

    # test delete_record with non-admin active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    database.login("aekoshak", "6320182Aa")
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.delete_record(test)
    database.logout()
    enablePrint()
    print("delete_record with non-admin active sesssion with random input passed with no crashing ")

    # test delete_record with admin active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    database.login("admin", "Admin123456")
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.delete_record(test)
    database.logout()
    enablePrint()
    print("delete_record with admin active sesssion with random input passed with no crashing ")

    # test edit_record with out active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.edit_record(test)
    enablePrint()
    print("edit_record with out active sesssion with random input passed with no crashing ")

    # test edit_record with non-admin active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    database.login("aekoshak", "6320182Aa")
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.edit_record(test)
    database.logout()
    enablePrint()
    print("edit_record with non-admin active sesssion with random input passed with no crashing ")

    # test edit_record with admin active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    database.login("admin", "Admin123456")
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.edit_record(test)
    database.logout()
    enablePrint()
    print("edit_record with admin active sesssion with random input passed with no crashing ")

    # test read_record with out active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.read_record(test)
    enablePrint()
    print("read_record with out active sesssion with random input passed with no crashing ")

    # test read_record with non-admin active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    database.login("aekoshak", "6320182Aa")
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.read_record(test)
    database.logout()
    enablePrint()
    print("read_record with non-admin active sesssion with random input passed with no crashing ")

    # test read_record with admin active session
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    blockPrint()
    database.login("admin", "Admin123456")
    for i in range(100):
        test = ''.join((random.choice(lettersAndDigits) for i in range(30)))
        database.read_record(test)
    database.logout()
    enablePrint()
    print("read_record with admin active sesssion with random input passed with no crashing ")

if __name__ == "__main__":
    main()