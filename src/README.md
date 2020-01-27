MGNREGA Application
================================

Introduction
----
This is MGNREGA console application. You can read the app doc using this [link](https://docs.google.com/document/d/13SEqYxdvtYwUFO-XHNDG9_7hXKbOunJDsURZevZUAis/edit).

The console application manages the tasks of BDO, GPM and Members.

------
Welcome Page

TBW

------

### Credentials

You will be requiring credentials to access this application :

1. For accessing app as BDO : 


    email : 'v@gmail.com'
    
    password : 'upes@123'
    
2. For accessing app as GPM :

    
    email : 'ruchi@gmail.com'
    
    password : 'r'
    
3. For accessing app as Member :


    email : 'shivam@gmail.com'
    
    password : 's'
    
-----
#Tests
-----
For running tests type command(make sure you are in the project directory) in terminal : 

    coverage run -m pytest TestBDO.py TestGPM.py TestMember.py

-----
#Test Coverage
-----
For viewing test coverage type command(make sure you are in the project directory) in terminal :

    coverage report -m BDO.py GPM.py Member.py