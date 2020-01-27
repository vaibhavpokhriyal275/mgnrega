import DBConnection as db
import sqlite3

from pip._vendor.distlib.compat import raw_input


class GPM:

    def __init__(self):
        self.conn = db.sql_connection()
        self.gpm_id = None

        self.login()

    def login(self):

        print("\n~~~ GPM Login ~~~")
        email = str(raw_input("Enter email: "))
        password = str(raw_input("Enter password: "))

        try:
            cursor = self.conn.execute(
                "SELECT * FROM gpm where EMAIL='{}' AND PASSWORD='{}'".format(email, password))
            cursor = cursor.fetchone()
            if cursor is None:
                print("\nEmail & Password does not match!")
                self.login()

            else:
                self.gpm_id = cursor[0]
                print('Logged In')
                self.dashboard(email)

        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)

    def dashboard(self, email):

        print('\n\n\n***** GPM Dashboard *****')
        print('\nWelcome {}'.format(email))
        print('\n1. View All Members')
        print('\n2. Assign Member to Project')
        print('\n3. Update Member')
        print('\n4. Delete Member from Project')
        print('\n5. View Complaints')
        print('\n6. Exit')
        choice = str(raw_input('\nEnter Choice : '))
        if choice == '1':
            self.gpm_view_members()
        elif choice == '2':
            self.gpm_assign_member()
        elif choice == '3':
            self.gpm_update_member()
        elif choice == '4':
            self.gpm_delete_member()
        elif choice == '5':
            self.gpm_view_complaints()
        elif choice == '6':
            print('Have a Nice Day')
        else:
            print('Wrong Input, Try Again')

        if choice != '6':
            self.dashboard(email)

    def gpm_view_members(self):

        try:
            print('\n\nApproved Members')
            members = self.conn.execute("Select * from members where MEMBER_STATUS = 1 ")
            for x in members: print(x)

            print('\n\nUnApproved Members')
            members = self.conn.execute("Select * from members where MEMBER_STATUS = 0 ")
            for x in members: print(x)

        except sqlite3.Error as e:
            print(e)

    def gpm_assign_member(self):
        print('Create and Assign Member to project')
        print('\nEnter the following details :')
        fname = input('\nFirst Name:')
        lname = input('\nLast Name: ')
        age = input('\nAge : ')
        gender = input('\nGender(M/F) : ')
        state = input('\nState : ')
        address = input('\nAddress : ')
        pincode = input('\nPincode : ')
        email = input('\nEmail : ')
        password = input('\nPassword : ')
        place = input('\nPlace : ')
        wage_status = 0
        project_id = input('\nProject Id : ')

        try:
            self.conn.execute("INSERT INTO members(GPM_ID, FNAME, LNAME, AGE, GENDER, STATE, ADDRESS, PINCODE, EMAIL, \
                              PASSWORD, PLACE, WAGE_STATUS, PROJECT_ID, MEMBER_STATUS ) \
                              VALUES({}, '{}', '{}', {}, '{}', '{}', '{}', {}, '{}', '{}', '{}', {}, {}, 0)"
                              .format(self.gpm_id, fname, lname, age, gender, state, address, pincode, email, password,
                                      place, wage_status, project_id))
            self.conn.commit()
            print('Member Assigned to Project')
            return True

        except sqlite3.Error as e:
            print(e)
            return False

    def gpm_update_member(self):
        print('JMD')


    def gpm_delete_member(self):
        print('Delete Member')

    def gpm_view_complaints(self):
        print('View Complaints')
        complaints = self.conn.execute("SELECT ID as Member_ID, SUBJECT, COMPLAINT FROM complaints WHERE STATUS = 0")
        for x in complaints: print(x)

        complaint_id = int(input('\n\nEnter the complaint id which you would like to resolve : '))
        try :
            self.conn.execute("UPDATE complaints \
                              SET STATUS = 1 \
                              WHERE ID = {}".format(complaint_id))
            self.conn.commit()
            print('Resolved Successfully')
        except sqlite3.Error as e:
            print(e)
