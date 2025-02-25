# ATM Banking System

A Python-based ATM (Automated Teller Machine) simulation system using Tkinter for the GUI and MySQL for database management.

## Features

- User Authentication (Login/Register)
- Account Balance Inquiry
- Cash Withdrawal
- Cash Deposit
- Account Information
- Transaction Report Generation
- Multi-language Support (Serbian/English)

## Prerequisites

- Python 3.x
- MySQL Server
- Required Python packages:

  tkinter
  PIL (Python Imaging Library)
  mysql-connector-python

## Installation

1. Clone the repository
2. Install required packages:

   ```bash
   pip install pillow mysql-connector-python
   ```

3. Configure MySQL connection in:

```8:12:user.py
        global mycursor
        mydb=mysql.connector.connect(host="localhost",user="root",password="")
        mycursor=mydb.cursor()
        mycursor.execute("create database if not exists databaza")
        mycursor.execute("use databaza")
```

## Database Structure

The system uses a MySQL database named `databaza` with a table `bank` containing:

- accid (Account ID)
- name (User's Name)
- password (PIN)
- balance (Account Balance)

## Usage

1. Run the main application:

   ```bash
   python atm_projekat.py
   ```

2. Choose between:

   - Login (existing users)
   - Register (new users)
   - About (project information)

3. Main features available after login:
   - Withdraw money
   - Deposit money
   - Check balance
   - Print account statement
   - View account information

## Security Features

- PIN-based authentication
- Encrypted password storage
- Session management
- Transaction validation
- Balance verification before withdrawals

## File Structure

- `atm_projekat.py` - Main application file with GUI implementation
- `user.py` - User class and database operations
- `stringHandler.py` - String encoding handler
- `images/` - Directory containing UI assets
- Generated transaction reports are saved as `atm_[timestamp].txt`

## Transaction Reports

The system generates detailed transaction reports containing:

- Account holder name
- Card number
- Current balance
- Transaction timestamp
- Transaction date

Example report structure can be found in:

```1:6:atm_121023.txt
Ime:Francis Drake
Br.kartice:38757
Stanje racuna:89269RSD
Vreme:12:10:23
Datum:20/08/2022

```

## License

This project is part of a Software Engineering course assignment.

---

Note: This project's interface is primarily in Serbian, with some English elements in the codebase.
