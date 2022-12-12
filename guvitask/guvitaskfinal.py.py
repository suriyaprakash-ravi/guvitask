#!/usr/bin/env python
# coding: utf-8

# In[7]:


import re


def validate_email(email):
    if re.search(r'@.+\.', email):
        if not re.search(r'@\.', email):
            if not re.search(r'^[^A-Za-z0-9]', email):
                return True
    return False
validate_email('surya@gmail.com')

def validate_password(password):
    if len(password) >= 5 and len(password) <= 16:
       if re.search(r'[^A-Za-z0-9]', password) and re.search(r'[0-9]', password) and re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
            return True
    return False
validate_password('Sura@09')

def register_user(email, password):
    if validate_email(email):
        if validate_password(password):
            with open('usersdetails2.txt', 'x'):
                f=open('userdetails2.txt','a')
                f.write(email + ',' + password + '\n')
                print('Registration successful!')
        else:
            print('Invalid password!')
    else:
        print('Invalid email!')

register_user('surya@gmail.com','Sura@09')

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    with open('userdetails2.txt', "r") as f:
        for line in f:
            line = line.strip()
            stored_email, stored_password = line.split(",")
            if email == stored_email and password == stored_password:
                print("Login successful.")
                return
    print("Login failed. Invalid username or password.")
login()

def retrieve_password(email):
    with open('userdetails2.txt', 'r') as f:
        for line in f:
            line = line.strip()
            stored_email, stored_password = line.split(",")
            if email == stored_email:
                return stored_password
    return None
retrieve_password('surya@gmail.com')


# In[ ]:




