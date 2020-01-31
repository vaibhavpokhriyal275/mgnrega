import DBConnection as db
import sqlite3


class BDO:
    """
    Class which handles operations accessible to BDO(Block Development Officer).
    """

    def __init__(self):

        self.conn = db.sql_connection()
        self.bdo_id = None
        self.projects = ['Road Construction', 'Sewage Treatment', 'Building Construction']

    def login(self):
        """
        Function for BDO Login.
        :return:
        """

        print("\n~~~ BDO Login ~~~")

        try:

            email = input("Enter email: ")
            password = input("Enter password: ")
            result = self.conn.execute(
                "SELECT * FROM bdo where lower(email)='{}' AND password='{}'".format(email, password)).fetchone()
            if result is None:
                print("\nEmail & Password does not match!")

            else:
                self.bdo_id = result[0]
                print('Logged In')
                self.dashboard(email)
            return True

        except Exception as e:
            print(type(e), e)
            return False

    def dashboard(self, email):
        """
        Display Dashboard Options to BDO.
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
        choice = input('Please choose option : ')
        if choice == '1':
            self.gpm_create()
            return 1
        elif choice == '2':
            self.gpm_update()
            return 2
        elif choice == '3':
            self.gpm_delete()
            return 3
        elif choice == '4':
            self.project_create()
            return 4
        elif choice == '5':
            self.project_update()
            return 5
        elif choice == '6':
            self.project_delete()
            return 6
        elif choice == '7':
            self.member_approve()
            return 7
        else:
            print('Exit')
            return False

    def gpm_create(self):
        """
        Creates GPM.
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
        """
        Update GPM details by GPM email.
        :return:
        """

        print('\n*** Updating GPM ***')

        try:
            gpm = self.gpm_view()
            print(gpm)
            email = gpm[7]

            print('\n\nEnter the updated details ')
            fname = input('First Name : ')
            lname = input('Last Name : ')
            state = input('State : ')
            address = input('Address : ')
            password = input('Password : ')

            self.conn.execute("UPDATE GPM \
                          SET \
                          FNAME = '{}', \
                          NAME = '{}', \
                          STATE = '{}',\
                          ADDRESS = '{}', \
                          PASSWORD = '{}' \
                          WHERE EMAIL = '{}'\
                                 ".format(fname, lname, state, address, password, email))
            self.conn.commit()
            print('Updated Successfully')
            return True

        except Exception as e:
            print(e)
            return False

    def gpm_delete(self):
        """
        Deletes GPM record by ID.
        :return:
        """
        print('\n*** Delete GPM ***')
        gpm = self.gpm_view()
        email = gpm[7]
        a = input('Are you sure you want to delete this GPM(Y for Yes) ?')
        if a == 'Y':
            self.conn.execute("Delete from gpm where EMAIL = '{}' and BDO_ID = {}".format(email, self.bdo_id))
            self.conn.commit()
            print('Deleted')
            return True
        else:
            print('GPM Not Deleted')
            return False

    def project_create(self):
        """
        Create new Project.
        :return:
        """
        print('\n** Creating new Project **')
        name = input('Project Name : ')
        project = int(input(
            'Specify Project Type(1/2/3) : \n 1 for Road Construction\n 2 for Sewage treatment\n 3 for Building \
            Construction')) + 1
        print(project)
        state = input('State : ')
        member_req = input('Member Estimate : ')
        cost_est = input('Cost Estimate : ')
        start_date_est = input('Start Date Estimate(YYYY/MM/DD) : ')
        end_date_est = input('End Date Estimate(YYYY/MM/DD) : ')
        a = [0, 1, 2]
        if a.count(project) != 0:
            project_type = self.projects[project]
            try:
                self.conn.execute("INSERT INTO projects(NAME, TYPE, STATE, MEMBERS_REQ, COST_EST, START_DATE_EST, END_DATE_EST) \
                                            VALUES('{}', '{}', '{}', {}, {}, '{}', '{}')"
                                  .format(name, project_type, state, member_req, cost_est, start_date_est,
                                          end_date_est))

                self.conn.commit()
                print('Created Successfully')
                return True

            except sqlite3.Error as e:
                print(e)
                return False

        else:
            print('Wrong Choice')
            return False

    def project_update(self):
        """
        Update project based on ID.
        :return:
        """
        print('\n\n\n*** Updating Project Details ***\n')
        self.projects_view()

        try:

            project_id = int(input('\n\n Enter the project id you would like to update : '))
            state = input('Enter State Name : ')
            self.conn.execute("update projects set \
                                        STATE = '{}' where ID = {} ".format(state, project_id))
            self.conn.commit()
            print('Updated')
            return True

        except Exception as e:
            print(e)
            return False

    def project_delete(self):
        """
        Delete Project by ID.
        :return:
        """

        print('\n\n\nDeleting Projects')

        try:
            self.projects_view()
            id = int(input('\n\n Enter project id you would like to delete : '))
            self.conn.execute("Delete from projects where id = {}".format(id))
            self.conn.commit()
            print('Deleted Successfully')
            return True
        except Exception as e:
            print(e)
            return False

    def member_approve(self):
        """
        Change member_status to approved.
        :return:
        """
        print('\n\nUnApproved Members')

        try:
            if self.member_view_unapproved():
                a = int(input('\n\n\nEnter the Member Id which you would like to approve  : '))
                self.conn.execute("UPDATE members SET MEMBER_STATUS = 1 WHERE ID = {}".format(a))
                self.conn.commit()
                return True
        except Exception as e:
            print(e)
            return False

    def gpm_view(self):
        """
        Returns details of GPM by email.
        :return:
        """
        try:
            gpm_email = input('Enter GPM\'s email : ')
            gpm = self.conn.execute(
                "SELECT * FROM gpm where EMAIL = '{}' AND BDO_ID = {}".format(gpm_email, self.bdo_id)).fetchone()
            print(gpm)
            return gpm
        except Exception as e:
            print(e)
            return False

    def projects_view(self):
        """
        Prints list of Projects.
        :return:
        """
        try:
            projects = self.conn.execute("select * from projects").fetchall()
            print(projects)
            return True
        except Exception as e:
            print(e)
            return False

    def member_view_unapproved(self):
        """
        Prints list of Unapproved Members.
        :return:
        """
        try:
            members = self.conn.execute("SELECT * FROM members WHERE MEMBER_STATUS != 1").fetchall()
            if members is not None:
                print(members)
                return True
            else:
                print('No Members to Display')
                return False
        except Exception as e:
            print(e)
            return False
