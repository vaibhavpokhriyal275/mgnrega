from Member import Member
import mock
import sqlite3


class Test_Member:

    @mock.patch('Member.db.sql_connection')
    @mock.patch('Member.Member.login', return_value=True)
    @mock.patch('Member.input')
    def test_complaints_success(self, inputs, login, db):
        inputs.side_effect = ['Dummy', 'Dummy']
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.return_value = True
        assert Member().complaint() == True

    @mock.patch('Member.db.sql_connection')
    @mock.patch('Member.Member.login', return_value=True)
    @mock.patch('Member.input')
    def test_complaints_failure(self, inputs, login, db):
        inputs.side_effect = ['Dummy', 'Dummy']
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.side_effect = sqlite3.Error
        assert Member().complaint() == False

    @mock.patch('Member.db.sql_connection')
    @mock.patch('Member.Member.login', return_value=True)
    def test_view_success(self, login, db):
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.return_value = True
        assert Member().view() == True

    @mock.patch('Member.db.sql_connection')
    @mock.patch('Member.Member.login', return_value=True)
    def test_view_failure(self, login, db):
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.side_effect = sqlite3.Error
        assert Member().view() == False
