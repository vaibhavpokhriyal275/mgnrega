import DBConnection as db
import sqlite3

from pip._vendor.distlib.compat import raw_input


class BDO:

    def __init__(self):

        self.conn = db.sql_connection()
        self.bdo_id = None
        self.projects = ['', 'Road Construction', 'Sewage Treatment', 'Building Construction']

        self.login()

    def login(self):
        """
        Function for BDO Login
        :return:
        """

        print("\n~~~ BDO Login ~~~")
        email = str(raw_input("Enter email: "))
        password = str(raw_input("Enter password: "))

        try:
            cursor = self.conn.execute(
                "SELECT * FROM bdo where lower(email)='{}' AND password='{}'".format(email, password))
            cursor = cursor.fetchone()
            if cursor is None:
                print("\nEmail & Password does not match!")
                self.login()

            else:
                self.bdo_id = cursor[0]
                print('Logged In')
                self.dashboard(email)

        except sqlite3.Error as e:
            print(type(e).__name__, ": ", e)

    def dashboard(self, email):
        """
        Display Dashboard Options to BDO
        :param email:
        :return:
        """

        print('**** BDO DASHBOARD ****')
        print('\n\nWelcome  {}'.format(email))
        print('\n 1. Create GPM')
        print('\n 2. Update GPM')
        print('\n 3. Delete GPM')
        print('\n 4. Create Project')
        print('\n 5. Update Project')
        print('\n 6. Delete Project')
        print('\n 7. View Unapproved Members')
        print('\n 8. Exit')
        choice = str(input('Please choose option : '))
        if choice == '1':
            self.gpm_create()
        elif choice == '2':
            self.gpm_update()
        elif choice == '3':
            self.gpm_delete()
        elif choice == '4':
            self.project_create()
        elif choice == '5':
            self.project_update()
        elif choice == '6':
            self.project_delete()
        elif choice == '7':
            self.approve_member()
        elif choice == '8':
            print('Exitted')
        else:
            print("Try again.")

        if choice != '8':
            self.dashboard(email)

    def gpm_create(self):
        """
        Creates GPM
        :return:
        """
        print('\n** Creating new GPM **')
        fname = input('First Name : ')
        lname = input('Last Name : ')
        state = input('State : ')
        address = input('Address : ')
        pincode = input('Pincode : ')
        email = input('email : ')
        password = input('Password : ')
        try:
            self.conn.execute("INSERT INTO gpm(BDO_ID, FNAME, NAME, STATE, ADDRESS, PINCODE, EMAIL, PASSWORD) \
                                VALUES({}, '{}', '{}', '{}', '{}', {}, '{}', '{}')"
                              .format(self.bdo_id, fname, lname, state, address, pincode, email, password))

            self.conn.commit()
            print('Created Successfully')
            return True

        except sqlite3.Error as e:
            print(e)
            return False

    def gpm_update(self):

        print('\n*** Updating GPM ***')
        gpm_email = input('Enter GPM\'s email : ')

        gpm = self.conn.execute("SELECT * FROM gpm where EMAIL = '{}' AND BDO_ID = {}".format(gpm_email, self.bdo_id))
        gpm = gpm.fetchone()
        print(gpm)

        print('\n\nEnter the details you want to change or press Enter')
        fname = input('First Name : ') or gpm[2]
        lname = input('Last Name : ') or gpm[3]
        state = input('State : ') or gpm[4]
        address = input('Address : ') or gpm[5]
        pincode = input('PinCode : ') or gpm[6]
        password = input('Password : ') or gpm[8]
        try:
            self.conn.execute("UPDATE GPM \
                          SET \
                          FNAME = '{}', \
                          NAME = '{}', \
                          STATE = '{}',\
                          ADDRESS = '{}', \
                          PINCODE = {}, \
                          PASSWORD = '{}' \
                          WHERE EMAIL = '{}'\
                                 ".format(fname, lname, state, address, pincode, password, gpm_email))
            self.conn.commit()
            print('Updated Successfully')
            return True

        except sqlite3.Error as e:
            print(e)
            return False

    def gpm_delete(self):
        """
        Deletes GPM record by id
        :return:
        """
        print('\n*** Delete GPM ***')
        gpm_id = input('\nEnter email of GPM : ')
        gpm = self.conn.execute("Select * from gpm where EMAIL = '{}' and BDO_ID = {}".format(gpm_id, self.bdo_id))
        gpm = gpm.fetchone()
        print(gpm)
        a = input('Are you sure you want to delete this GPM(Y for Yes/ N for No) ?')
        if a == 'Y' or 'y':
            self.conn.execute("Delete * from gpm where EMAIL = '{}' and BDO_ID = {}".format(gpm_id, self.bdo_id))
            self.conn.commit()
            print('Deleted')
            return True
        elif a == 'N' or 'n':
            self.gpm_Delete()
            return False

    def project_create(self):

        print('\n** Creating new Project **')
        name = input('Project Name : ')
        project = int(input(
            'Specify Project Type(1/2/3) : \n 1 for Road Construction\n 2 for Sewage treatment\n 3 for Building \
            Construction'))
        state = input('State : ')
        member_req = input('Member Estimate : ')
        cost_est = input('Cost Estimate : ')
        start_date_est = input('Start Date Estimate(YYYY/MM/DD) : ')
        end_date_est = input('End Date Estimate(YYYY/MM/DD) : ')

        if project == 1 or 2 or 3:
            project_type = self.projects[project]
            try:
                self.conn.execute("INSERT INTO projects(NAME, TYPE, STATE, MEMBERS_REQ, COST_EST, START_DATE_EST, END_DATE_EST) \
                                            VALUES('{}', '{}', '{}', {}, {}, '{}', '{}')"
                                  .format(name, project_type, state, member_req, cost_est, start_date_est,
                                          end_date_est))

                self.conn.commit()
                print('Created Successfully')

            except sqlite3.Error as e:
                print(e)

        else:
            print('Wrong Choice')

    def project_update(self):
        print('\n\n\n*** Updating Project Details ***\n')

        projects = self.conn.execute("select * from projects")
        projects = projects.fetchone()
        print(projects)
        id = int(input(('\n\n Enter the project id you would like to update : ')))
        state = str(raw_input('Enter State Name : '))

        if projects != None :
            try:
                self.conn.execute("update projects set \
                                    STATE = '{}' where ID = {} ".format(state, id))
                self.conn.commit()
                print('Updated')

            except sqlite3.Error as e:
                print(e)

    def project_delete(self):

        print('\n\n\nDeleting Projects')
        id = int(input('\n\n Enter project id you would like to delete : '))
        try:
            self.conn.execute("Delete * from projects where id = {}".format(id))
            self.conn.commit()
            print('Deleted Successfully')
        except sqlite3.Error as e:
            print(e)

    def approve_member(self):
        print('\n\nUnApproved Members')

        try:
            members = self.conn.execute("SELECT * FROM members WHERE MEMBER_STATUS != 1")
            for x in members: print(x)

            a = int(input('\n\n\nEnter the Member Id which you would like to approve  : '))
            self.conn.execute("UPDATE members SET MEMBER_STATUS = 1 WHERE ID = {}".format(a))
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)



