from DatabaseFile import *
from passlib.hash import pbkdf2_sha256 # from the passlib library
import datetime
from Contact import Contact

# Creating an account object with username and password
class Account:
    def __init__(self, username, password, database):
        self.username = username
        self.password = password
        self.contacts = []
        self.database = database
        self.admin = False
        self.log = []
    
    # add a function to add to the log
    def add_log(self, logline):
        if len(self.log) == 64:
            del self.log[0]
            self.log.append(logline)
        else:
            self.log.append(logline)