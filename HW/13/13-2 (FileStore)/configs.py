import logging

DB_CONNECTION = {
    "DBname": "FileStore",
    "HOST": "localhost",
    "USER": "postgres",
    "PORT": 5432,
    "PASSWORD": "saf6811"
}

INFO = {
    "name": "Maktab File Store",
    "description": "...",
    "version": "1.0.0",
}

Questions = {
    "user": {
        "First Name": "Only Words",
        "Last Name": "Only Words",
        "Phone Number": "A Valid Phone Number that starts with 09../+989..",
        "National ID Number": "A Number with length of 10",
        "User's Age": "A Number between 1-99",
        "Password": "Anything!",
        "User is a Seller": "User is a Seller or not"
    },
    "file": {
        "File Name": "Anything!",
        "Data Created": "YYYY-MM-DD",
        "Data Modified": "YYYY-MM-DD",
        "Seller ID": "ID of user that is Seller",
        "Other": "Any information about the File"  
    }
}
