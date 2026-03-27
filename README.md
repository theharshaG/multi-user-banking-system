# multi-user-banking-system

## Banking System (Python Project)

## Overview
This project is a simple command-line Banking System implemented in Python. It allows users to create accounts, log in, deposit and withdraw money, and check account balances. User data is stored in a text file to ensure persistence between program executions.

## Features
Account creation
User login
Deposit functionality
Withdrawal functionality
Balance inquiry
Data persistence using file handling

## Technologies Used
Python
Object-Oriented Programming (OOP)
File Handling
Exception Handling
Project Structure
banking-system/
│
├── main.py
├── bank.txt
└── README.md

## How to Run
instell python(VS code)
Run the program:multi user banking system.py

## How It Works
User data is stored in a text file (bank.txt) in the format:
username,balance
When the program starts, it reads the file and loads the data into a dictionary.
During execution, all operations (deposit, withdrawal) update the in-memory data.
When the program exits, the updated data is written back to the file.

## Future Improvements
Add secure authentication system
Implement graphical user interface
Develop a web-based version using Flask
Add transaction history and logging
Improve error handling and validation

## Author
Harsha G
Learning Python | Embedded Systems | IoT
