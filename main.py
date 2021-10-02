from DatabaseFile import *
import cmd
import pickle
import os.path
from os import path

class main(cmd.Cmd):
    print("Welcome to our address book app. type HLP [<command name>] for help")

    # program doesn't check for invalid calls with wrong number of parameters, wrong parameter types, etc
    # create admin account

    def do_HLP(self, command):
        help_command(command)

    def do_LIN(self, line):
        splitline = line.split(" ")
        if len(splitline) == 2:
            database.login(splitline[0], splitline[1])
        else:
            print("Usage: LIN <userID> <password>")
    def do_LOU(self, line):
        database.logout()

    def do_CHP(self, line):
        database.change_password(line)

    def do_ADU(self, line):
        database.add_account(line)

    def do_DEU(self, line):
        database.delete_account(line)

    def do_DAL(self, line):
        database.display_audit_log(line)

    def do_ADR(self, line):
        database.add_record(line)

    def do_DER(self, line):
        database.delete_record(line)

    def do_EDR(self, line):
        database.edit_record(line)

    def do_RER(self, line):
        database.read_record(line)

    def do_IMD(self, line):
        if database.active_user == 0:
            print("No active login session")
        elif database.active_user.admin:
            print("Admin users cannot Import Database")
        else:
            if path.isfile(line) == True:
                try:
                    storageFile = open(line, 'rb')
                    temp = pickle.load(storageFile)
                except pickle.PickleError:
                    print("File " + line + " dose not contain database")  # There was no database stored in the file.
                    return 0
                if type(temp) != list:
                    print("Couldn't read file")
                else:
                    notfound = True
                    for tcontacts in temp:
                        for dcontacts in database.active_user.contacts:
                            if tcontacts.RID == dcontacts.RID:
                                notfound = False
                        if notfound:
                            if(len(database.active_user.contacts) < 256):
                                database.active_user.contacts.append(tcontacts)
                            else:
                                print("Maximum amount of contacts reached you can't add more contacts")
                        notfound = True
                    print("Database imported")
            else:
                print("couldn't find file: " + line)

    def do_EXD(self, line):
        if database.active_user == 0:
            print("No active login session")
        elif database.active_user.admin:
            print("Admin users cannot Export Database")
        elif len(line) == 0:
            print("Usage: Export Database: EXD <Output_file>")
        else:
            storageFile = open(line, 'wb')
            storageFile.seek(0)
            storageFile.truncate()
            pickle.dump(database.active_user.contacts, storageFile)
            storageFile.close()
            print("Database exported")

    def do_EXT(self, line):
        database.logout()
        storageFile = open('DatabaseStorage', 'wb')
        storageFile.seek(0)
        storageFile.truncate()
        pickle.dump(database, storageFile)
        storageFile.close()
        print("Thanks for using our app. See you soon!.")
        return True


def help_command(cmd):
    if cmd == "":
        print("Login: LIN <userID> <password>\n"
              "Logout: LOU\n"
              "Change Password: CHP <old password>\n"
              "Add User: ADU <userID>\n"
              "Delete User: DEU <userID>\n"
              "Display Audit Log: DAL [<userID>]\n"
              "Add Record: ADR <recordID> [<field1=value1> <field2=value2> ...]\n"
              "Delete Record: DER <recordID>\n"
              "Edit Record: EDR <recordID> <field1=value1> [<field2=value2> ...]\n"
              "Read Record: RER [<recordID>] [<fieldname> ...]\n"
              "Import Database: IMD <Input_File>\n"
              "Export Database: EXD <Output_file>\n"
              "Help: HLP [<command name>]\n"
              "Exit: EXT\n")
    elif cmd == "LIN":
        print("Login: LIN <userID> <password>\n")
    elif cmd == "LOU":
        print("Logout: LOU\n")
    elif cmd == "CHP":
        print("Change Password: CHP <old password>\n")
    elif cmd == "ADU":
        print("Add User: ADU <userID\n")
    elif cmd == "DEU":
        print("Delete User: DEU <userID>\n")
    elif cmd == "ADR":
        print("Add Record: ADR <recordID> [<field1=value1> <field2=value2> ...\n")
    elif cmd == "DER":
        print("Delete Record: DER <recordID>\n")
    elif cmd == "EDR":
        print("Edit Record: EDR <recordID> <field1=value1> [<field2=value2> ...]\n")
    elif cmd == "RED":
        print("Read Record: RER [<recordID>] [<fieldname> ...]\n")
    elif cmd == "IMD":
        print("Import Database: IMD <Input_File>\n")
    elif cmd == "EXD":
        print("Export Database: EXD <Output_file>\n")
    elif cmd == "HLP":
        print("Help: HLP [<command name>]\n")
    elif cmd == "EXT":
        print("Exit: EXT\n")
    else:
        print("no such instructions exists.")

if __name__ == "__main__":
    database = Database()
    if path.isfile('DatabaseStorage') == True:
        try:
            storageFile = open('DatabaseStorage', 'rb')
            database = pickle.load(storageFile)
        except pickle.PickleError:
            None # There was no database stored in the file.
    if type(database) != Database:
        database = Database()
    if len(database.dictionary) == 0:
        print("You need to create an admin account to use the app")
        username = input("Choose a username for the admin account: ")
        database.first_admin(username)

    main().cmdloop()
