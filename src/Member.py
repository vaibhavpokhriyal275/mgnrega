import DBConnection as db
import pandas as pd
import sqlite3

from pip._vendor.distlib.compat import raw_input


class Member:

    def __init__(self):
        self.conn = db.sql_connection()
        self.member_id = None

        self.login()

    def login(self):

        print("\n~~~ Member Login ~~~")
        email = str(raw_input("Enter email: "))
        password = str(raw_input("Enter password: "))

        try:
            cursor = self.conn.execute(
                "SELECT * FROM members where EMAIL='{}' AND PASSWORD='{}' AND MEMBER_STATUS = 1".format(email, password))
            cursor = cursor.fetchone()
            if cursor is None:
                print("\nYou are not authorized to login to this portal. Contact your GPM")
                self.login()

            else:
                self.member_id = cursor[0]
                print('Logged In')
                self.dashboard(email)

        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)

    def dashboard(self, email):
        print('\n\n\nMember Dashboard')
        print('\n\nWelcome {}'.format(email))
        print('\n1. View Account Details')
        print('\n2. File Complaint to GPM/BDO')
        print('\n3. Exit ')
        choice = str(raw_input('\nEnter Choice : '))
        if choice == '1':
            self.view()
        elif choice == '2':
            self.complaint()
        elif choice == '3':
            print('Exitting, Have a nice day')
        else:
            print('Retry, Incorrect Input')

        if choice != '3':
            self.dashboard(email)

    def view(self):
        print('\n\nAccount Details : ')
        try:

            # df = pd.read_sql_query("SELECT * FROM members WHERE ID = {}".format(self.member_id), self.conn)
            details = self.conn.execute("SELECT * FROM members WHERE ID = {}".format(self.member_id))
            print(details)
            return True

        except sqlite3.Error as e:
            print(e)
            return False

    def complaint(self):
        print('\n\nWelcome to Complaint Box')
        print('\n\nEnter the following to file a complaint ')
        subject = input('Subject(Title of your Complaint) : ')
        complaint = input('Complaint(Describe your Issue) : ')
        try:
            self.conn.execute("INSERT INTO complaints(MEMBER_ID, SUBJECT, COMPLAINT, STATUS) \
                              VALUES({}, '{}', '{}', 0)"
                              .format(self.member_id, subject, complaint))
            self.conn.commit()
            print('Complaint Raised Successfully')
            return True
        except sqlite3.Error as e:
            print(e)
            return False
