import sqlite3
import mock
from gpm import GPM


class Test_GPM:

    @mock.patch('gpm.db.sql_connection')
    @mock.patch('gpm.GPM.login', return_value=True)
    @mock.patch('gpm.input')
    def test_login_success(self, inputs, login, db):
        inputs.side_effect = ['test@test', 'test']
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.return_value.fetchone.return_value = ['test@test', 'test']
        assert GPM().login() is True

    @mock.patch('gpm.db.sql_connection')
    @mock.patch('gpm.GPM.login', return_value=True)
    @mock.patch('gpm.input')
    def test_gpm_assign_member_success(self, inputs, login, db):
        inputs.side_effect = ['Dummy', 'Dummy', 22, 'M', 'Dummy', 'Dummy', 560034, 'dummy', 'dummy', 'dummy', 1]
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.return_value = True
        assert GPM().gpm_assign_member() is True

    @mock.patch('gpm.db.sql_connection')
    @mock.patch('gpm.GPM.login', return_value=True)
    @mock.patch('gpm.input')
    def test_gpm_assign_member_failure(self, inputs, login, db):
        inputs.side_effect = ['Dummy', 'Dummy', 22, 'M', 'Dummy', 'Dummy', 560034, 'dummy', 'dummy', 'dummy', 1]
        db_mock = mock.Mock()
        db.return_value = db_mock
        db_mock.execute.side_effect = sqlite3.Error
        assert GPM().gpm_assign_member() is False

