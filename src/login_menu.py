from BDO import BDO
from GPM import GPM
from Member import Member
import DBConnection as db


class Run:

    def __init__(self):
        self.conn = db.sql_connection()
        if self.conn is None:
            print("Error while connecting with database")
            exit("Retry after sometime!!!")
        else:

            self.setup_admin()
            self.create_tables()

    def setup_admin(self):
        """
        Create table for BDO(Admin) if not exists and insert one row with given pre-details of admin.
        :return:
        """
        # enable foreign key constraint
        self.conn.execute("PRAGMA foreign_keys = ON")

        c = self.conn.cursor()
        c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='bdo'")

        # if the count is not 1, then create table bdo and add 1st Admin
        if c.fetchone()[0] != 1:
            c.execute('''CREATE TABLE bdo
            (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            FNAME VARCHAR(20) NOT NULL,
            LNAME VARCHAR(20) NOT NULL,
            EMAIL VARCHAR(50) NOT NULL,
            PASSWORD VARCHAR(16) NOT NULL);''')

            c.execute("INSERT INTO bdo(ID, FNAME, LNAME, EMAIL, PASSWORD) VALUES(1, 'Madhur', 'Mittal', "
                      "'madhurmittal275@gmail.com', 'Maddy')")
            self.conn.commit()

    def create_tables(self):
        """
        Create tables only if they don't exist in database.
        :return:
        """
        # create table gpm if not exist
        self.conn.execute('''CREATE TABLE if not exists gpm
        (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        BDO_ID INTEGER NOT NULL,
        FNAME VARCHAR(20) NOT NULL,
        NAME VARCHAR(20) NOT NULL,
        STATE VARCHAR(15) NOT NULL,
        ADDRESS VARCHAR(50) NOT NULL,
        PINCODE INT NOT NULL,
        EMAIL VARCHAR(40) UNIQUE NOT NULL,
        PASSWORD VARCHAR(16) NULL,
        FOREIGN KEY(BDO_ID) REFERENCES bdo(ID));''')

        # create table projects if not exist
        self.conn.execute('''CREATE TABLE if not exists projects
        (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NAME VARCHAR(20) UNIQUE NOT NULL,
        TYPE VARCHAR(25) NOT NULL,
        STATE VARCHAR(15) NOT NULL,
        MEMBERS_REQ INT NOT NULL,
        COST_EST FLOAT NOT NULL,
        START_DATE_EST VARCHAR(10) NOT NULL,
        END_DATE_EST VARCHAR(10) NOT NULL);''')

        # create table members if not exist
        self.conn.execute('''CREATE TABLE if not exists members
        (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        GPM_ID INTEGER NOT NULL,
        FNAME VARCHAR(20) NOT NULL,
        LNAME VARCHAR(20) NOT NULL,
        AGE INT NOT NULL,
        GENDER VARCHAR(6) NOT NULL,
        STATE VARCHAR(15) NOT NULL,
        ADDRESS VARCHAR(50) NOT NULL,
        PINCODE INT NOT NULL,
        EMAIL VARCHAR(40) UNIQUE NOT NULL,
        PASSWORD VARCHAR(16) NULL,
        PLACE VARCHAR(20) NOT NULL,
        DAYS_WORKED INT NULL,
        WAGE FLOAT NULL,
        WAGE_STATUS INTEGER NULL,
        PROJECT_ID INTEGER REFERENCES projects(ID) NOT NULL,
        MEMBER_STATUS INTEGER NULL,
        FOREIGN KEY(GPM_ID) REFERENCES gpm(ID));''')

        # create table complaints if not exist
        self.conn.execute('''CREATE TABLE if not EXISTS complaints
        (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        MEMBER_ID INTEGER REFERENCES members(ID) NOT NULL,
        SUBJECT VARCHAR(50) NOT NULL,
        COMPLAINT VARCHAR(500) NOT NULL,
        STATUS INTEGER NOT NULL);''')

    def login_menu(self):
        """ Display Login options for users to choose.

        :return:
        """
        print("\n**** Welcome To MGNREGA APP ****")
        print("1. Login as BDO \n2. Login as GPM \n3. Login as Member\n4. Exit")
        choice = str(input("Choose: "))

        if choice == '1':
            BDO()
        elif choice == '2':
            GPM()
        elif choice == '3':
            Member()
        elif choice == '4':
            print("\nExiting...")

        else:
            print("\nWrong Input! Try again.")

        if choice != '4':
            self.login_menu()
