from DatabaseFile import *
from passlib.hash import pbkdf2_sha256 # from the passlib library
import datetime
from Contact import Contact

# to do:
# check for valid inputs
# implement maximums on contacts and per user and amount of users

class Account:
    def __init__(self, username, password, database):
        self.username = username
        self.password = password
        self.contacts = []
        self.database = database
        self.admin = False
        self.log = []

    def add_log(self, logline):
        if len(self.log) == 64:
            del self.log[0]
            self.log.append(logline)
        else:
            self.log.append(logline)

#Dr. Heckman, if you read this, what is the best pop tart flavor? Smore or Brown Sugar? No other options.