import sqlite3
import mock
from GPM import GPM


class Test_GPM:

    @mock.patch('GPM.db.sql_connection')
    @mock.patch('GPM.GPM.login', return_value=True)
    @mock.patch('GPM.input')
    def test_gpm_assign_member_success(self, inputs, login, db):
        inputs.side_effect = ['Dummy', 'Dummy', 22, 'M', 'Dummy', 'Dummy', 560034, 'dummy', 'dummy', 'dummy', 1]
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.return_value = True
        assert GPM().gpm_assign_member() == True

    @mock.patch('GPM.db.sql_connection')
    @mock.patch('GPM.GPM.login', return_value=True)
    @mock.patch('GPM.input')
    def test_gpm_assign_member_failure(self, inputs, login, db):
        inputs.side_effect = ['Dummy', 'Dummy', 22, 'M', 'Dummy', 'Dummy', 560034, 'dummy', 'dummy', 'dummy', 1]
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.side_effect = sqlite3.Error
        assert GPM().gpm_assign_member() == False

