# Secure Address Book Application


## 1. Introduction
### 1.1 Purpose 
The purpose of this document is to present a detailed description of the Address Book Machine. It will explain the purpose and features of the address book, the interfaces of the software and hardware, what they will do, and the constraints under which they must operate. This document is intended for users of the address book.

### 1.2 Document Conventions
This document was created based on the IEEE template for system requirements specification documents.

### 1.3 Intended Audience and Reading Suggestions
* Typical Users: Anyone who wants to keep contact information in one place.
* Professional Users: Companies and organizations who want to keep track of client and/or employee contact information.
* Programmers: Developers and programmers fixing bugs.
* Our professor: The guy who will give us a grade on this.

### 1.4 Product Scope
The address book machine is a tool that users can use to store contact information. Users can add, delete, or edit contacts in their address book.

### 1.5 References
No references used.

## 2. Overall Description
### 2.1 Product Perspective
This product is intended for personal use to store contact information of friends, family, and other acquaintances, or for companies to use to store contact information on clients. This product for anyone who would like to store contact information that is accessible over wifi or their cellular network.

### 2.2 Product Functions
* record_add: Add contact information
* record_del: Delete contact information
* record_get: Access contact information
* Access through wifi and cellular networks

### 2.3 User Classes and Characteristics
* Typical Users: Anyone who wants to keep contact information in one place.
* Professional Users: Companies and organizations who want to keep track of client and/or employee contact information
* Programmers: Developers and programmers fixing bugs

### 2.4 Operating Environment
Linux OS

### 2.5 Design and Implementation Constraints
The address book machine runs on Linux, it can be accessed through cellular networks and over wifi. Information is backed up on the cloud. There is a limit of 256 users being created on the machine. Each user is allowed a maximum of 5 addresses stored.

### 2.6 User Documentation
There is a printed user manual that comes with the Address Book Machine.

### 2.7 Assumptions and Dependencies
The address book machine is Linux based, and therefore requires Linux to run. The address book also requires a cellular network connection or a wifi connection. It also requires access to the cloud to store backup data.

## 3. External Interface Requirements
### 3.1 User Interfaces
The address book machine uses a terminal screen for command inputs.

### 3.2 Hardware Interfaces
The known minimum hardware requirements for the address book is a device with cellular network service or the ability to connect to wifi. The address book machine device comes with all the necessary hardware requirements, and the memory is able to hold 5 contact entries per user.

### 3.3 Software Interfaces
The address book machine requires a Linux based system.

### 3.4 Communications Interfaces
The address book machine requires cellular network service or a wifi connection. It also requires access to the cloud to back up the data contained in the address book.

## 4. System Features
This section demonstrates the Address Book Machine’s most prominent features and explains how they can be used by the user.

### 4.1 Add an Address
Users will be able to add a new address to their stored address book. </br>

Through access to the on-screen terminal, users will add a new address to their address book.This is of high priority as it is one of the main functions of the machine. This is done by typing the command “ADD <name>,<address>”</br>

Example of adding an address: </br>
ADD Brenton Kearney, 5998 Alcala Park Way</br>
New address added successfully.</br>

### 4.2 Edit an Address

Users will be able to edit an existing address in their stored address book. </br>

Through access to the on-screen terminal, users will edit an existing address from the address book. This is a high priority function of the machine. This is done by typing the command “EDIT <name>, <new address information>”. If an address under that name does not exist the user will be notified.</br>

Example of editing an address:</br>
	EDIT Justin Cavalli, 5997 Alcala Park Way
	Address updated successfully

### 4.3 Delete an Address

Users will be able to delete an existing address in their stored address book.</br>

Through access to the on-screen terminal, users will edit an existing address from the address book. This is a high priority function of the machine. This is done by typing the command “DEL <name>”. If an address under that name does not exist, the user will be notified.</br>

Example of editing an address:</br>
	DEL Noelle Tuchscherer
	Address deleted successfully


### 4.4 View all of the user’s addresses

Users will be able to print out all of their addresses to the terminal.</br>

Through access to the on-screen terminal, users will be able to print all of their stored addresses to the terminal. This is a high priority function of the machine. This is done by typing the command “DUMP”.</br>

Example of printing out user addresses:</br>
	DUMP
	Rachel Valdez, 5994 Alcala Park Way
	Mark Heckman, BEC 318


### 4.5 Access the database remotely

Users will be able to access their stored address book remotely from their own devices.</br>

Users can access their address book information by logging in remotely through either wifi connection or over the cellular network. This is a high priority function of the machine. This is done by logging in remotely on the Address Book Machine app on one’s computer or cell phone.</br>


### 4.6 Add a new account

The administrator will be able to add a new login account for a new user.</br>

The administrator only has the privileges to create a new account with access to the Address Book Machine. This is a high priority function of the machine. This is done by the administrator typing “NACC” followed by the new user typing “<username>,<password>”.</br>

Example of adding an account:</br>
	NACC
	Enter your username,password below:
	myUsername,myPassword
	New account created successfully


### 4.7 Delete an existing account

The administrator will be able to delete an existing account of a user.</br>

The administrator only has the privileges to delete an existing account with access to the Address Book Machine. This is a high priority function of the machine. This is done by the administrator typing “DACC,<name of user>”</br>

Example of deleting an account:</br>
	DACC,Abdulqader Koshak
	New account deleted successfully


## 5. Other Nonfunctional Requirements
### 5.1 Performance Requirements
The Address Book Machine must be setup with access to the internet in order for the machine to successfully backup the address book data to the cloud. Without internet connection the information will not be backed up in case of damage to the device, updates will not be available, and the data will not be remotely accessible to the users.

### 5.2 Safety Requirements
To ensure that no users lose their data while using the address book machine, the developer team updates the Address Book Machine regularly through wifi connections and the data is stored on the cloud.

### 5.3 Security Requirements
The Address Book Machine requires users to login with a username, password, and 2-factor authentication in the form of an authenticator app. Only the user and other users they authorize will be allowed to access that user’s address book. There is also a designated administrator account with access to all address books if necessary.

### 5.4 Software Quality Attributes
The Address Book Machine provides users with a simple interface to interact with their address book. It is available to the users 24 hours a day, 7 days a week when the Address Book Machine is connected and backed up to the internet. The use of the machine is easy to learn and use.

### 5.5 Business Rules
Users can access their addresses alone, unauthorized users will not be able to access other users’ addresses. Only the administrator can add or delete accounts to the Address Book Machine. The administrator can also access all addresses stored when necessary.
