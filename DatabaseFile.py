from Account import Account
from CheckPassword import *
from passlib.hash import pbkdf2_sha256 # from the passlib library. download with "pip install passlib" in terminal
import datetime
from Contact import Contact


class Database:
    def __init__(self):
        self.dictionary = {}    # Username maps to account
        # self.active_user = Account("0", "0", self) # for pylint error
        self.active_user= 0 # active_user == 0 means that no account is logged in

    def first_admin(self, username):
        username = self.choose_name(username)
        password = self.choose_password()
        passwordHash = pbkdf2_sha256.hash(password)  # storing a salted hash of the password
        new_account = Account(username, passwordHash, self)
        self.dictionary[username] = new_account
        self.dictionary[username].admin = True
        self.active_user = self.dictionary[username]  # user is logged in
        self.dictionary[username].add_log(str(datetime.datetime.now()) + ", AU, " + self.active_user.username)
        self.dictionary[username].add_log(str(datetime.datetime.now()) + ", L1, " + username)
        self.dictionary[username].add_log(str(datetime.datetime.now()) + ", LS, " + username)

    # Only admin can add account
    def add_account(self, username):
        if len(self.dictionary) == 8:
            print("Maximum amount of users reached you can't add more users")
        elif type(self.active_user) == Account and self.active_user.admin:
            username = self.choose_name(username)
            password = self.choose_password()
            passwordHash = pbkdf2_sha256.hash(password)     #storing a salted hash of the password
            new_account = Account(username, passwordHash, self)
            self.dictionary[username] = new_account
            self.active_user = self.dictionary[username]  # user is logged in
            print("Active user now is : " + username)
            self.dictionary[username].add_log(str(datetime.datetime.now()) + ", AU, " + self.active_user.username)
            self.dictionary[username].add_log(str(datetime.datetime.now()) + ", L1, " + username)
            self.dictionary[username].add_log(str(datetime.datetime.now()) + ", LS, " + username)
        else:
            print("Admin account must be active")

    def delete_account(self, username):
        if self.active_user == 0:
            print("Admin account must be active")
        elif not self.active_user.admin:
            print("Admin account must be active")
        elif username in self.dictionary and type(self.active_user) == Account and self.active_user.admin:
            if self.active_user.username == username:
                print("An admin account can't delete it self")
            else:
                del self.dictionary[username]
                self.active_user.add_log(str(datetime.datetime.now()) + ", DU, " + self.active_user.username)
                print("OK")
        else:
            print("User " + username + " does not exist")

    def login(self, username, password):
        # check if an account is already active
        if self.active_user != 0:
            print("An Account is currently active; logout before proceeding")
        # check if the account exists
        else:
            if not self.check_credentials(username, password):
                print("Invalid credentials")
                if username in self.dictionary:
                    self.dictionary[username].add_log(str(datetime.datetime.now()) + ", LF, " + username)
            else:
                self.active_user = self.dictionary[username]
                self.dictionary[username].add_log(str(datetime.datetime.now()) + ", LS, " + self.active_user.username)
                print("OK")

    def logout(self):
        if self.active_user == 0:
            print("No active login session")
        else:
            print("OK")
            self.dictionary[self.active_user.username].add_log(str(datetime.datetime.now()) + ", LO, " + self.active_user.username)
            self.active_user = 0

    def check_credentials(self, username, password):
        # checks if userID exists. Returns index or -1 if it does not exist
        if username in self.dictionary:
            #checks the hash of the password against the stored one, returns a bool value
            return pbkdf2_sha256.verify(password, self.dictionary[username].password)
        else:
            return False

    def change_password(self, old_password):
        # check that the user knows the password before changing it
        if self.active_user == 0:
            print("No active login session")
        elif pbkdf2_sha256.verify(old_password, self.active_user.password) == False:
            print("Invalid credentials")
            self.dictionary[self.active_user.username].add_log(str(datetime.datetime.now()) + ", FPC, " + self.active_user.username)
        else:
            new_pass = input("Create a new password...")
            if check_password(new_pass):
                verify = input("reenter the same password:")
                if verify == new_pass:
                    # store the password as a hash
                    self.active_user.password = pbkdf2_sha256.hash(new_pass)
                    self.dictionary[self.active_user.username].add_log(str(datetime.datetime.now()) + ", SPC, " + self.active_user.username)
                    print("OK")
                else:
                    print("Passwords do not match")

    def add_record(self, line):
        splitline = line.split(" ")
        if "=" in splitline[0]:
            RID = ""
        else:
            RID = splitline[0]
        SN = ""
        GN = ""
        PEM = ""
        WEM = ""
        PPN = ""
        WPN = ""
        SA = ""
        CITY = ""
        STP = ""
        CTY = ""
        PC = ""

        for field in splitline:
            if "SN" in field:
                SNline = field.split("=")
                if len(SNline) > 1 and len(SNline[1]) < 65:
                    SN = SNline[1]
                else:
                    print("SN invalid")
            elif "GN" in field:
                GNline = field.split("=")
                if len(GNline) > 1 and len(GNline[1]) < 65:
                    GN = GNline[1]
                else:
                    print("GN invalid")
            elif "PEM" in field:
                PEMline = field.split("=")
                if len(PEMline) > 1 and self.check_email(PEMline[1]):
                    PEM = PEMline[1]
                else:
                    print("PEM email is invalid")
            elif "WEM" in field:
                WEMline = field.split("=")
                if len(WEMline) > 1 and self.check_email(WEMline[1]):
                     WEM = WEMline[1]
                else:
                    print("WEM email is invalid")
            elif "PPN" in field:
                PPNline = field.split("=")
                if len(PPNline) > 1 and self.check_phone(PPNline[1]):
                    PPN = PPNline[1]
                else:
                    print("PPN field is invalid")
            elif "WPN" in field:
                WPNline = field.split("=")
                if len(WPNline) > 1 and self.check_phone(WPNline[1]):
                    WPN = WPNline[1]
                else:
                    print("WPN field is invalid")
            elif "SA" in field:
                SAline = field.split("=")
                if len(SAline) > 1 and len(SAline[1]) < 65:
                    SA = SAline[1]
                else:
                    print("SA invalid")
            elif "CITY" in field:
                CITYline = field.split("=")
                if len(CITYline) > 1 and len(CITYline[1]) < 65:
                    CITY = CITYline[1]
                else:
                    print("CITY invalid")
            elif "STP" in field:
                STPline = field.split("=")
                if len(STPline) > 1 and len(STPline[1]) < 65:
                    STP = STPline[1]
                else:
                    print("STP invalid")
            elif "CTY" in field:
                CTYline = field.split("=")
                if len(CTYline) > 1 and len(CTYline[1]) < 65:
                    CTY = CTYline[1]
                else:
                    print("CTY invalid")
            elif "PC" in field:
                PCline = field.split("=")
                if len(PCline) > 1 and len(PCline[1]) < 65:
                    PC = PCline[1]
                else:
                    print("PC invalid")

        #check for active login session
        if self.active_user == 0:
            print("No active login session")
        #check for admin user
        elif self.active_user.admin == True:
            print("Administrator not authorized to add contacts")
        #check for no record ID
        elif RID == "":
            print("No recordID")

        elif len(self.active_user.contacts) == 256:
            print("Maximum amount of contacts reached you can't add more contacts")

        #check for valid inputs
        else:
            if len(self.active_user.contacts) == 0:
                self.active_user.contacts.append(Contact(RID, SN, GN, PEM, WEM, PPN, WPN, SA, CITY, STP, CTY, PC))
                print("OK")
            else:
                #check for existing recordID
                notfound = True
                for contact in self.active_user.contacts:
                    if contact.RID == RID:
                        print("Record ID already assigned")
                        notfound = False
                if notfound:
                    self.active_user.contacts.append(Contact(RID, SN, GN, PEM, WEM, PPN, WPN, SA, CITY, STP, CTY, PC))
                    print("OK")

    def edit_record(self, line):
        splitline = line.split(" ")
        if "=" in splitline[0]:
            RID = ""
        else:
            RID = splitline[0]
        SN = ""
        GN = ""
        PEM = ""
        WEM = ""
        PPN = ""
        WPN = ""
        SA = ""
        CITY = ""
        STP = ""
        CTY = ""
        PC = ""

        for field in splitline:
            if "SN" in field:
                SNline = field.split("=")
                if len(SNline) > 1 and len(SNline[1]) < 65:
                    SN = SNline[1]
                else:
                    print("SN invalid")
            elif "GN" in field:
                GNline = field.split("=")
                if len(GNline) > 1 and len(GNline[1]) < 65:
                    GN = GNline[1]
                else:
                    print("GN invalid")
            elif "PEM" in field:
                PEMline = field.split("=")
                if len(PEMline) > 1 and self.check_email(PEMline[1]):
                    PEM = PEMline[1]
                else:
                    print("PEM email is invalid")
            elif "WEM" in field:
                WEMline = field.split("=")
                if len(WEMline) > 1 and self.check_email(WEMline[1]):
                    WEM = WEMline[1]
                else:
                    print("WEM email is invalid")
            elif "PPN" in field:
                PPNline = field.split("=")
                if len(PPNline) > 1 and self.check_phone(PPNline[1]):
                    PPN = PPNline[1]
                else:
                    print("PPN field is invalid")
            elif "WPN" in field:
                WPNline = field.split("=")
                if len(WPNline) > 1 and self.check_phone(WPNline[1]):
                    WPN = WPNline[1]
                else:
                    print("WPN field is invalid")
            elif "SA" in field:
                SAline = field.split("=")
                if len(SAline) > 1 and len(SAline[1]) < 65:
                    SA = SAline[1]
                else:
                    print("SA invalid")
            elif "CITY" in field:
                CITYline = field.split("=")
                if len(CITYline) > 1 and len(CITYline[1]) < 65:
                    CITY = CITYline[1]
                else:
                    print("CITY invalid")
            elif "STP" in field:
                STPline = field.split("=")
                if len(STPline) > 1 and len(STPline[1]) < 65:
                    STP = STPline[1]
                else:
                    print("STP invalid")
            elif "CTY" in field:
                CTYline = field.split("=")
                if len(CTYline) > 1 and len(CTYline[1]) < 65:
                    CTY = CTYline[1]
                else:
                    print("CTY invalid")
            elif "PC" in field:
                PCline = field.split("=")
                if len(PCline) > 1 and len(PCline[1]) < 65:
                    PC = PCline[1]
                else:
                    print("PC invalid")

        # check for active login session
        if self.active_user == 0:
            print("No active login session")
        # check for admin user
        elif self.active_user.admin == True:
            print("Administrator not authorized to add contacts")
        # check for no record ID
        elif RID == "":
            print("No recordID")
        else:
            found = False
            for contact in self.active_user.contacts:
                if contact.RID == RID:
                    if SN != "":
                        contact.SN = SN
                    if GN != "":
                        contact.GN = GN
                    if PEM != "":
                        contact.PEM = PEM
                    if WEM != "":
                        contact.WEM = WEM
                    if PPN != "":
                        contact.PPN = PPN
                    if WPN != "":
                        contact.WPN = WPN
                    if SA != "":
                        contact.SA = SA
                    if CITY != "":
                        contact.CITY = CITY
                    if STP != "":
                        contact.STP = STP
                    if CTY != "":
                        contact.CTY = CTY
                    if PC != "":
                        contact.PC = PC
                    print("OK")
                    found = True
            if not found:
                print("Record ID does not exist")


    def check_email(self, email):
        if "@" in email and "." in email and len(email) < 65:
            return True
        else:
            return False

    def check_phone(self, phone):
        if len(phone) == 11 or len(phone) == 10 and phone.isdigit():
            return True
        else:
            return False


    def read_record(self, record_id):
        #check for active login session
        if self.active_user == 0:
            print("No active login session")
        #check for admin user
        elif self.active_user.admin == True:
            print("Administrator not authorized to display contacts")
        #check for default input
        elif record_id == "":
            for contact in self.active_user.contacts:
                print(contact)
        elif len(self.dictionary) == 7:
            print("Maximum amount of users reached you can't add more users")
        else:
            #check for existing recordID
            contactFound = False
            for contact in self.active_user.contacts:
                if contact.RID == record_id:
                    print(contact)
                    print("OK")
                    contactFound = True
            if contactFound == False:
                print("Record does not exist")

    def delete_record(self, record_id):
        #check for active login session
        if self.active_user == 0:
            print("No active login session")
        #check for admin user
        elif self.active_user.admin == True:
            print("Administrator not authorized to delete contacts")
        #check for no record ID
        elif record_id == "":
            print("No recordID")
        else:
            #check for existing recordID
            contactFound = False
            for contact in self.active_user.contacts:
                if contact.RID == record_id:
                    self.active_user.contacts.remove(contact)
                    print("OK")
                    contactFound = True
            if contactFound == False:
                print("Record does not exist")

    def choose_name(self, attempt):
        username = ""
        # Check username requirements
        while username == "":
            if len(attempt) < 1 or len(attempt) > 16:
                print("This username does not meet length requirements.\n")
                attempt = input("Choose another username: ")
            else:
                username = attempt
                for account in self.dictionary:
                    if account == attempt:
                        print("This username is already associated "
                              "with an account.\n")
                        attempt = input("Choose another username: ")
                        username = ""
        return username

    def choose_password(self):
        password = ""
        # Check password requirements
        while password == "":
            password = input("Please enter a password: ")
            if not (check_password(password)):
                password = ""
        return password

    def display_audit_log(self, userID):
        if userID == "" and self.active_user != 0 and self.active_user.admin:
            for username in self.dictionary:
                print(username + "'s Log:")
                for logEntry in self.dictionary[username].log:
                    print(logEntry)
        elif userID != "" and self.active_user != 0 and self.active_user.admin:
            user = None
            for username in self.dictionary:
                if username == userID:
                    user = self.dictionary[username]
            if(user is None):
                print("user does not exist")
            else:
                print(user.username + "'s Log:")
                for logEntry in user.log:
                    print(logEntry)
        else:
            print("Admin account must be active")